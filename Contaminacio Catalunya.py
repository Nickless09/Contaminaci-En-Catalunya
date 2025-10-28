import streamlit as st
import pandas as pd
import folium
from folium.plugins import HeatMap
from streamlit_folium import st_folium

st.title("🌍 Contaminació Catalunya - Heatmap combinat")

# -------------------------
# 🔗 List of GitHub raw CSV URLs
base_url = "https://raw.githubusercontent.com/Nickless09/Contaminaci-En-Catalunya/main/dat/"
file_names = [
    "Qualitat_de_l_aire_part2.csv",
    "Qualitat_de_l_aire_part2.csv",
    "Qualitat_de_l_aire_part3.csv",
    "Qualitat_de_l_aire_part4.csv",
    "Qualitat_de_l_aire_part5.csv",
]  # 👈 add more filenames as needed

urls = [base_url + name for name in file_names]

# -------------------------
# Cached CSV loader
@st.cache_data(show_spinner=True)
def load_multiple_csvs(url_list):
    dfs = []
    for url in url_list:
        try:
            df = pd.read_csv(url, encoding="UTF-8")
            hour_cols = [f"{h:02d}h" for h in range(1, 25)]
            if all(col in df.columns for col in hour_cols):
                df["AVG_CONTAM"] = df[hour_cols].mean(axis=1)
            df = df.dropna(subset=["LATITUD", "LONGITUD", "AVG_CONTAM"])
            dfs.append(df)
        except Exception as e:
            st.warning(f"⚠️ Could not read {url}: {e}")
    if dfs:
        return pd.concat(dfs, ignore_index=True)
    else:
        return pd.DataFrame(columns=["LATITUD", "LONGITUD", "AVG_CONTAM"])

# -------------------------
# Load all CSVs
df = load_multiple_csvs(urls)

if df.empty:
    st.error("No data could be loaded. Check that your CSV URLs are correct and public.")
else:
    st.success(f"Loaded {len(df)} rows from {len(urls)} CSV files.")

    # -------------------------
    # Create Folium heatmap
    map_center = [df["LATITUD"].mean(), df["LONGITUD"].mean()]
    m = folium.Map(location=map_center, zoom_start=9)

    heat_data = df[["LATITUD", "LONGITUD", "AVG_CONTAM"]].values.tolist()
    HeatMap(heat_data, radius=15).add_to(m)

    st_folium(m, width=700, height=500)
