import pandas as pd
import streamlit as st
import folium
from folium.plugins import HeatMap
from streamlit_folium import st_folium
import requests
import io

st.set_page_config(page_title="Air Quality in Catalunya", layout="wide")
st.title("Air Quality Heatmap in Catalunya")

# --- Dropbox raw CSV link ---
url = "https://www.dropbox.com/s/o6wm4aavblw2j1azoymex/Qualitat_de_l_aire.csv?dl=1"

# --- Download CSV content ---
@st.cache_data(show_spinner=True)
def download_csv(url):
    r = requests.get(url)
    r.raise_for_status()
    # Read CSV from bytes stream
    return pd.read_csv(io.StringIO(r.text), encoding="UTF-8")

# --- Load CSV ---
try:
    df = download_csv(url)
    st.success(f"Loaded {len(df)} rows")
except Exception as e:
    st.error(f"Error loading CSV: {e}")
    st.stop()

# --- Compute average contamination ---
hour_cols = [f"{h:02d}h" for h in range(1, 25)]
df["AVG_CONTAM"] = df[hour_cols].mean(axis=1)

# --- Drop rows with missing coordinates ---
df = df.dropna(subset=["LATITUD", "LONGITUD", "AVG_CONTAM"])

# --- Show preview ---
st.dataframe(df.head())

# --- Create Folium map ---
map_center = [df["LATITUD"].mean(), df["LONGITUD"].mean()]
m = folium.Map(location=map_center, zoom_start=10)

heat_data = df[["LATITUD", "LONGITUD", "AVG_CONTAM"]].values.tolist()
HeatMap(heat_data, radius=15).add_to(m)

# --- Display map ---
st_folium(m, width=700, height=500)
