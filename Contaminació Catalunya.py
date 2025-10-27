import pandas as pd
import streamlit as st
import folium
from folium.plugins import HeatMap
from streamlit_folium import st_folium

# --- Load CSV directly from Gofile ---
url = "https://store6.gofile.io/download/web/b693ad0d-08fd-46b7-a0a5-0299ca3a2630/Qualitat_de_l_aire.csv"
df = pd.read_csv(url, encoding="UTF-8")

st.dataframe(df.head())  # To quickly check the data


# Compute average contamination
hour_cols = [f"{h:02d}h" for h in range(1, 25)]
df["AVG_CONTAM"] = df[hour_cols].mean(axis=1)

# Drop rows with missing coordinates
df = df.dropna(subset=["LATITUD", "LONGITUD", "AVG_CONTAM"])

# Create Folium map
map_center = [df["LATITUD"].mean(), df["LONGITUD"].mean()]
m = folium.Map(location=map_center, zoom_start=10)

heat_data = df[["LATITUD", "LONGITUD", "AVG_CONTAM"]].values.tolist()
HeatMap(heat_data, radius=15).add_to(m)

# Show map in Streamlit
st_folium(m, width=700, height=500)
