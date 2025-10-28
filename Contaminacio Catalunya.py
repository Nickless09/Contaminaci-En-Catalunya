import streamlit as st
import pandas as pd
import folium
from folium.plugins import HeatMap
from streamlit_folium import st_folium

st.title("Contaminació Catalunya - Test File 1")

# -------------------------
# GitHub raw CSV URL (must be raw!)
base_url = "https://raw.githubusercontent.com/Nickless09/Contaminaci-En-Catalunya/main/dat/"
file_names = [
    "Qualitat_de_l_aire_part1.csv",
    "Qualitat_de_l_aire_part2.csv",
    "Qualitat_de_l_aire_part3.csv",
]  # 👈 add more filenames as needed
# -------------------------
# Define function BEFORE calling it
@st.cache_data(show_spinner=True)
def load_csv(url):
    df = pd.read_csv(url, encoding="UTF-8")
    # Compute average contamination
    hour_cols = [f"{h:02d}h" for h in range(1, 25)]
    if all(col in df.columns for col in hour_cols):
        df["AVG_CONTAM"] = df[hour_cols].mean(axis=1)
    df = df.dropna(subset=["LATITUD", "LONGITUD", "AVG_CONTAM"])
    return df

# -------------------------
# Call the function AFTER defining it
df = load_csv(csv_url)

st.write(f"Loaded {len(df)} rows from CSV.")

# -------------------------
# Create Folium heatmap
map_center = [df["LATITUD"].mean(), df["LONGITUD"].mean()]
m = folium.Map(location=map_center, zoom_start=10)

heat_data = df[["LATITUD", "LONGITUD", "AVG_CONTAM"]].values.tolist()
HeatMap(heat_data, radius=15).add_to(m)

st_folium(m, width=700, height=500)
