import streamlit as st
import pandas as pd
import folium
from folium.plugins import HeatMap
from streamlit_folium import st_folium

# ------------------- Load Data -------------------
@st.cache_data
def load_data():
    return pd.read_csv("dat/Qualitat_de_l_aire.csv", encoding="UTF-8")

df = load_data()

# ------------------- Compute Average Contamination -------------------
hour_cols = [f"{h:02d}h" for h in range(1, 25)]
df["AVG_CONTAM"] = df[hour_cols].mean(axis=1)
df = df.dropna(subset=["LATITUD", "LONGITUD", "AVG_CONTAM"])

# ------------------- Create Folium Map -------------------
map_center = [df["LATITUD"].mean(), df["LONGITUD"].mean()]
m = folium.Map(location=map_center, zoom_start=10)

heat_data = df[["LATITUD", "LONGITUD", "AVG_CONTAM"]].values.tolist()
HeatMap(heat_data, radius=15).add_to(m)

# ------------------- Streamlit -------------------
st.title("🌫️ Air Quality Heatmap")
st.write("Heatmap of average contamination in Catalunya")

# Display Folium map in Streamlit
st_folium(m, width=700, height=500)
