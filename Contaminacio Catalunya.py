import streamlit as st
import pandas as pd
import folium
from folium.plugins import HeatMap
from streamlit_folium import st_folium

st.title("Contaminació Catalunya Heatmap")

# -------------------------
# GitHub base URL
base_url = "https://raw.githubusercontent.com/Nickless09/air_quality_heatmap/main/dat/Qualitat_de_l_aire_part{}.csv"
num_files = 70
# -------------------------

@st.cache_data(show_spinner=True)
def load_csv_from_github(file_index):
    """Load a single CSV from GitHub and compute AVG_CONTAM"""
    url = base_url.format(file_index)
    try:
        df = pd.read_csv(url, encoding="UTF-8")
        hour_cols = [f"{h:02d}h" for h in range(1, 25)]
        if all(col in df.columns for col in hour_cols):
            df["AVG_CONTAM"] = df[hour_cols].mean(axis=1)
        return df
    except Exception as e:
        st.warning(f"Could not load file {url}: {e}")
        return pd.DataFrame()  # empty dataframe on error

# Load all CSVs
dfs = [load_csv_from_github(i) for i in range(1, num_files + 1)]
full_df = pd.concat(dfs, ignore_index=True)
full_df = full_df.dropna(subset=["LATITUD", "LONGITUD", "AVG_CONTAM"])

st.write(f"Loaded {len(full_df)} rows from {len(dfs)} CSV files.")

# -------------------------
# Create Folium heatmap
# -------------------------
map_center = [full_df["LATITUD"].mean(), full_df["LONGITUD"].mean()]
m = folium.Map(location=map_center, zoom_start=10)

heat_data = full_df[["LATITUD", "LONGITUD", "AVG_CONTAM"]].values.tolist()
HeatMap(heat_data, radius=15).add_to(m)

st_folium(m, width=700, height=500)
