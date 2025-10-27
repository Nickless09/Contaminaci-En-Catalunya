import streamlit as st
import pandas as pd
import folium
from folium.plugins import HeatMap
from streamlit_folium import st_folium
import os

st.title("Air Quality Heatmap")

folder_path = "dat"

# Load CSVs dynamically
dfs = []
for i in range(1, 71):
    file_path = os.path.join(folder_path, f"Qualitat_de_l_aire_part{i}.csv")
    if os.path.exists(file_path):
        df = pd.read_csv(file_path, encoding="UTF-8")
        hour_cols = [f"{h:02d}h" for h in range(1, 25)]
        if all(col in df.columns for col in hour_cols):
            df["AVG_CONTAM"] = df[hour_cols].mean(axis=1)
            dfs.append(df)

full_df = pd.concat(dfs, ignore_index=True)
full_df = full_df.dropna(subset=["LATITUD", "LONGITUD", "AVG_CONTAM"])

st.write(f"Loaded {len(full_df)} rows from {len(dfs)} CSV files.")

# Folium heatmap
map_center = [full_df["LATITUD"].mean(), full_df["LONGITUD"].mean()]
m = folium.Map(location=map_center, zoom_start=10)
heat_data = full_df[["LATITUD", "LONGITUD", "AVG_CONTAM"]].values.tolist()
HeatMap(heat_data, radius=15).add_to(m)

st_folium(m, width=700, height=500)
