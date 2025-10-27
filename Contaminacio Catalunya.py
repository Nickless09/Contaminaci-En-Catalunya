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
        url = "https://www.dropbox.com/scl/fi/o6wm4aavblw2j1azoymex/Qualitat_de_l_aire.csv?dl=1"
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
