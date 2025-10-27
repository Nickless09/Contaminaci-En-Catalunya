# streamlit_app.py
import streamlit as st
import pandas as pd
import folium
from folium.plugins import HeatMap
from streamlit_folium import st_folium
import os

st.set_page_config(page_title="Air Quality Heatmap", layout="wide")
st.title("Air Quality Heatmap")

# --- Upload CSV ---
uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, encoding="UTF-8")
    
    # Check required columns
    required_cols = ["LATITUD", "LONGITUD"] + [f"{h:02d}h" for h in range(1, 25)]
    if not all(col in df.columns for col in required_cols):
        st.error(f"The CSV must contain the columns: {required_cols}")
        st.stop()
    
    # Compute average contamination
    hour_cols = [f"{h:02d}h" for h in range(1, 25)]
    df["AVG_CONTAM"] = df[hour_cols].mean(axis=1)
    
    # Drop rows with missing values
    df = df.dropna(subset=["LATITUD", "LONGITUD", "AVG_CONTAM"])
    
    # --- Create Folium map ---
    map_center = [df["LATITUD"].mean(), df["LONGITUD"].mean()]
    m = folium.Map(location=map_center, zoom_start=10)
    
    # Heatmap data: [lat, lon, weight]
    heat_data = df[["LATITUD", "LONGITUD", "AVG_CONTAM"]].values.tolist()
    HeatMap(heat_data, radius=15).add_to(m)
    
    # Display map in Streamlit
    st_folium(m, width=700, height=500)
else:
    st.info("Please upload a CSV file to visualize the heatmap.")
