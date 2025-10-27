import pandas as pd
import streamlit as st
import folium
from folium.plugins import HeatMap
from streamlit_folium import st_folium
import requests
import io

st.set_page_config(page_title="Air Quality in Catalunya", layout="wide")
st.title("Air Quality Heatmap in Catalunya")

# --- Dropbox CSV URL ---
url = "https://www.dropbox.com/s/o6wm4aavblw2j1azoymex/Qualitat_de_l_aire.csv?dl=1"

# --- Download CSV content ---
@st.cache_data(show_spinner=True)
def download_csv(url):
    r = requests.get(url)
    r.raise_for_status()  # Ensure download was successful
    return io.StringIO(r.text)

csv_data = download_csv(url)

# --- Process CSV in chunks ---
chunk_size = 10000
chunks = []
for chunk in pd.read_csv(csv_data, chunksize=chunk_size, encoding="UTF-8", on_bad_lines='skip'):
    # Keep only rows with coordinates
    chunk = chunk.dropna(subset=["LATITUD", "LONGITUD"])
    
    # Compute average contamination for existing hour columns
    hour_cols = [f"{h:02d}h" for h in range(1, 25) if f"{h:02d}h" in chunk.columns]
    if hour_cols:
        chunk["AVG_CONTAM"] = chunk[hour_cols].mean(axis=1)
        chunk = chunk.dropna(subset=["AVG_CONTAM"])
    chunks.append(chunk)

# --- Concatenate all processed chunks ---
df = pd.concat(chunks, ignore_index=True)
st.success(f"Loaded {len(df)} rows")

# --- Preview data ---
st.dataframe(df.head())

# --- Create Folium map ---
if not df.empty:
    map_center = [df["LATITUD"].mean(), df["LONGITUD"].mean()]
    m = folium.Map(location=map_center, zoom_start=10)

    heat_data = df[["LATITUD", "LONGITUD", "AVG_CONTAM"]].values.tolist()
    HeatMap(heat_data, radius=15).add_to(m)

    st_folium(m, width=700, height=500)
else:
    st.warning("No valid data to display on the map.")
