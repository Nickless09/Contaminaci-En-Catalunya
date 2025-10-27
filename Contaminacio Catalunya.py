import pandas as pd
import streamlit as st
import folium
from folium.plugins import HeatMap
from streamlit_folium import st_folium

st.set_page_config(page_title="Air Quality in Catalunya", layout="wide")

st.title("Air Quality Heatmap in Catalunya")

# --- Lazy load CSV to avoid freezing Streamlit ---
if st.button("Load Heatmap"):
    with st.spinner("Loading data... this may take a while for large files"):
        # Dropbox link to CSV (ensure ?dl=1 for direct download)
        url = url = "https://ucb38c8600ec903e63a36f443768.dl.dropboxusercontent.com/cd/0/get/C0DlDq7sFDvonygGZBaeakWzQ2wN3wV2niarOEo9UcLC8AAacSkS3_tdSo3gVqBm26j9Z4GaKggj7g4kbUaBm7eCWmtB80m9CIufiPAzgCWEuNAlaGMygpbU5CjRQi5GxNKQbkw7E8MKTeYBIuvIrVpfK6bSOKIEQaRMdYvYR5ouww/file?_download_id=383459632035761521941075124236586397510915882434811952999394567254&_log_download_success=1#"

        try:
            # For safety, limit to 50k rows if CSV is huge
            df = pd.read_csv(url, encoding="UTF-8", nrows=50000)
        except Exception as e:
            st.error(f"Error loading CSV: {e}")
            st.stop()

        st.success(f"Loaded {len(df)} rows")

        # Compute average contamination
        hour_cols = [f"{h:02d}h" for h in range(1, 25)]
        df["AVG_CONTAM"] = df[hour_cols].mean(axis=1)

        # Drop rows with missing coordinates
        df = df.dropna(subset=["LATITUD", "LONGITUD", "AVG_CONTAM"])

        # Show first few rows
        st.dataframe(df.head())

        # Create Folium map
        map_center = [df["LATITUD"].mean(), df["LONGITUD"].mean()]
        m = folium.Map(location=map_center, zoom_start=10)

        heat_data = df[["LATITUD", "LONGITUD", "AVG_CONTAM"]].values.tolist()
        HeatMap(heat_data, radius=15).add_to(m)

        st_folium(m, width=700, height=500)

else:
    st.info("Click the button above to load the heatmap.")
