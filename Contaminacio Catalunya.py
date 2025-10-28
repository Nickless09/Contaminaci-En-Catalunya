import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import folium
from folium.plugins import HeatMap
from streamlit_folium import st_folium

# ----------------------------------
# 🌟 Page configuration
st.set_page_config(
    page_title="Contaminació Catalunya",
    page_icon="🌍",
    layout="wide",
)

# ----------------------------------
# 🧭 Title and Description
st.title("🌍 Contaminació de l'Aire a Catalunya")
st.markdown("""
Aquest panell interactiu mostra dades de **qualitat de l'aire a Catalunya**, 
incloent la contaminació mitjana per hora, mes i any.  
Explora el mapa, les tendències i les estadístiques interactives.
""")

# ----------------------------------
# 🗂️ Load multiple CSV files from GitHub
base_url = "https://raw.githubusercontent.com/Nickless09/Contaminaci-En-Catalunya/main/dat/"
file_names = [f"Qualitat_de_l_aire_part{i}.csv" for i in range(2, 5)]  # adjust range as needed
urls = [base_url + name for name in file_names]

@st.cache_data(show_spinner=False)
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
            st.warning(f"⚠️ Error carregant {url}: {e}")
    if dfs:
        return pd.concat(dfs, ignore_index=True)
    else:
        return pd.DataFrame(columns=["LATITUD", "LONGITUD", "AVG_CONTAM"])

# ----------------------------------
# 💫 Loading animation while data loads
with st.spinner("Carregant dades des de GitHub... això pot trigar uns segons ⏳"):
    df = load_multiple_csvs(urls)

if df.empty:
    st.error("❌ No s'han pogut carregar dades. Comprova que les rutes siguin correctes i públiques.")
    st.stop()

st.success("✅ Dades carregades correctament!")

# ----------------------------------
# 📊 Summary Metrics
st.markdown("### 📈 Resum de Dades")
col1, col2, col3 = st.columns(3)
col1.metric("🔢 Files carregades", f"{len(df):,}")
col2.metric("📍 Estacions", df["NOM_ESTACIO"].nunique() if "NOM_ESTACIO" in df else "N/A")
col3.metric("🌫️ Mitjana contaminació", f"{df['AVG_CONTAM'].mean():.2f}")

# ----------------------------------
# ⚙️ Filters (Sidebar)
st.sidebar.header("⚙️ Filtres")
tile_option = st.sidebar.selectbox(
    "🗺️ Tipus de mapa:",
    ["OpenStreetMap", "Stamen Terrain", "Stamen Toner", "CartoDB positron", "CartoDB dark_matter"]
)

contam_range = st.sidebar.slider(
    "🌫️ Filtra per nivell de contaminació:",
    min_value=float(df["AVG_CONTAM"].min()),
    max_value=float(df["AVG_CONTAM"].max()),
    value=(float(df["AVG_CONTAM"].min()), float(df["AVG_CONTAM"].max()))
)
df = df[df["AVG_CONTAM"].between(*contam_range)]

# ----------------------------------
# 🧭 Tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "🗺️ Heatmap",
    "⏰ Contaminació per Hora",
    "📆 Contaminació per Mes / Any",
    "📋 Dades i Descàrrega"
])

# ----------------------------------
# 🗺️ TAB 1: Heatmap
with tab1:
    st.subheader("🗺️ Mapa de Contaminació (Folium Heatmap)")

    map_center = [df["LATITUD"].mean(), df["LONGITUD"].mean()]
    m = folium.Map(location=map_center, zoom_start=8, tiles=tile_option)
    heat_data = df[["LATITUD", "LONGITUD", "AVG_CONTAM"]].values.tolist()
    HeatMap(heat_data, radius=15).add_to(m)

    st_folium(m, width=900, height=550)

# ----------------------------------
# ⏰ TAB 2: Hourly Contamination
with tab2:
    st.subheader("📈 Mitjana de Contaminació per Hora del Dia")

    hour_cols = [f"{h:02d}h" for h in range(1, 25)]
    valid_hour_cols = [col for col in hour_cols if col in df.columns]

    if valid_hour_cols:
        avg_per_hour = df[valid_hour_cols].mean()
        data_hour = pd.DataFrame({
            'Hour': list(range(1, len(valid_hour_cols) + 1)),
            'Average Contamination': avg_per_hour.values
        })

        plt.figure(figsize=(12, 6))
        sns.barplot(x='Hour', y='Average Contamination', data=data_hour, palette='viridis')
        plt.title('Average Contamination by Hour of the Day')
        plt.xlabel('Hour of the Day')
        plt.ylabel('Average Contamination')
        st.pyplot(plt)
    else:
        st.warning("No s'han trobat dades horàries al CSV.")

# ----------------------------------
# 📆 TAB 3: Yearly & Monthly Plots
with tab3:
    st.subheader("📆 Contaminació Mitjana per Any i Mes")

    # Generate mock year/month data if not available
    if "DATA" in df.columns:
        df["DATA"] = pd.to_datetime(df["DATA"], errors='coerce')
        df["Year"] = df["DATA"].dt.year
        df["Month"] = df["DATA"].dt.month
    else:
        st.info("No s'ha trobat una columna de data. Generant dades simulades per exemple.")
        np.random.seed(42)
        df["Year"] = np.random.choice([2021, 2022, 2023, 2024], len(df))
        df["Month"] = np.random.randint(1, 13, len(df))

    yearly_avg = df.groupby("Year", as_index=False)["AVG_CONTAM"].mean()
    monthly_avg = df.groupby("Month", as_index=False)["AVG_CONTAM"].mean()

    fig, axes = plt.subplots(1, 2, figsize=(14, 4))

    # --- Yearly plot ---
    norm = mcolors.Normalize(vmin=yearly_avg["AVG_CONTAM"].min(), vmax=yearly_avg["AVG_CONTAM"].max())
    colors = plt.cm.coolwarm(norm(yearly_avg["AVG_CONTAM"]))
    sns.barplot(x="Year", y="AVG_CONTAM", data=yearly_avg, ax=axes[0], palette=colors)
    axes[0].set_title("Average Contamination by Year")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Average Contamination")

    # --- Monthly plot ---
    norm_month = mcolors.Normalize(vmin=monthly_avg["AVG_CONTAM"].min(), vmax=monthly_avg["AVG_CONTAM"].max())
    colors_month = plt.cm.Greens(norm_month(monthly_avg["AVG_CONTAM"]))
    sns.barplot(x="Month", y="AVG_CONTAM", data=monthly_avg, ax=axes[1], palette=colors_month)
    axes[1].set_title("Average Contamination by Month")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Average Contamination")
    axes[1].set_xticks(range(12))
    axes[1].set_xticklabels(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])

    plt.tight_layout()
    st.pyplot(fig)

# ----------------------------------
# 📋 TAB 4: Data and Download
with tab4:
    st.subheader("📋 Dades Brutes")
    st.dataframe(df.head(100))

    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("📥 Descarrega dades filtrades", csv, "filtered_data.csv", "text/csv")

# ----------------------------------
# 🪶 Footer
st.markdown("---")
st.caption("Dades de qualitat de l'aire — Desenvolupat amb ❤️ per SemGr")





# import streamlit as st
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
# import matplotlib.colors as mcolors  # ✅ This is what fixes your error
# import folium
# from folium.plugins import HeatMap
# from streamlit_folium import st_folium

# st.title("🌍 Contaminació En Catalunya")

# # -------------------------
# # 🔗 GitHub raw CSV URLs
# base_url = "https://raw.githubusercontent.com/Nickless09/Contaminaci-En-Catalunya/main/dat/"
# file_names = [f"Qualitat_de_l_aire_part{i}.csv" for i in range(2, 5)]  # 👈 change to range(1, 71) for all 70 files
# urls = [base_url + name for name in file_names]

# # -------------------------
# # Cached CSV loader
# @st.cache_data(show_spinner=True)
# def load_multiple_csvs(url_list):
#     dfs = []
#     for url in url_list:
#         try:
#             df = pd.read_csv(url, encoding="UTF-8")
#             hour_cols = [f"{h:02d}h" for h in range(1, 25)]
#             if all(col in df.columns for col in hour_cols):
#                 df["AVG_CONTAM"] = df[hour_cols].mean(axis=1)
#             df = df.dropna(subset=["LATITUD", "LONGITUD", "AVG_CONTAM"])
#             dfs.append(df)
#         except Exception as e:
#             st.warning(f"⚠️ Could not read {url}: {e}")
#     if dfs:
#         return pd.concat(dfs, ignore_index=True)
#     else:
#         return pd.DataFrame(columns=["LATITUD", "LONGITUD", "AVG_CONTAM"])

# # -------------------------
# # ✅ Load all CSVs (note the correct function call!)
# df = load_multiple_csvs(urls)

# if df.empty:
#     st.error("No data could be loaded. Check that your CSV URLs are correct and public.")
# else:
#     # st.success(f"Loaded {len(df)} rows from {len(urls)} CSV files.")

#     # -------------------------
#     # Create Folium heatmap
#     map_center = [df["LATITUD"].mean(), df["LONGITUD"].mean()]
#     m = folium.Map(location=map_center, zoom_start=9)

#     heat_data = df[["LATITUD", "LONGITUD", "AVG_CONTAM"]].values.tolist()
#     HeatMap(heat_data, radius=15).add_to(m)

#     st_folium(m, width=700, height=500)

#  # -------------------------
#     # 📊 Average Contamination by Hour
#     st.subheader("📈 Mitjana de Contaminació per Hora del Dia")

#     hour_cols = [f"{h:02d}h" for h in range(1, 25)]
#     valid_hour_cols = [col for col in hour_cols if col in df.columns]

#     if valid_hour_cols:
#         avg_per_hour = df[valid_hour_cols].mean()
#         data = pd.DataFrame({
#             'Hour': list(range(1, len(valid_hour_cols) + 1)),
#             'Average Contamination': avg_per_hour.values
#         })

#         plt.figure(figsize=(12, 6))
#         sns.barplot(x='Hour', y='Average Contamination', data=data, palette='viridis')
#         plt.title('Average Contamination by Hour of the Day')
#         plt.xlabel('Hour of the Day')
#         plt.ylabel('Average Contamination')
#         plt.xticks(rotation=0)

#         st.pyplot(plt)
#     else:
#         st.warning("No hourly data found in the loaded CSVs.")
        
# # -------------------------
# # 📅 Average Contamination by Year and Month
# st.subheader("📅 Mitjana Anual i Mensual de Contaminació")

# if "DATA" in df.columns:
#     df["DATA"] = pd.to_datetime(df["DATA"], errors="coerce")
#     df["Year"] = df["DATA"].dt.year
#     df["Month"] = df["DATA"].dt.month

#     yearly_avg = df.groupby("Year", as_index=False)["AVG_CONTAM"].mean()
#     monthly_avg = df.groupby("Month", as_index=False)["AVG_CONTAM"].mean()

#     fig, axes = plt.subplots(1, 2, figsize=(14, 4))

#     # --- Yearly plot ---
#     norm = mcolors.Normalize(vmin=yearly_avg["AVG_CONTAM"].min(), vmax=yearly_avg["AVG_CONTAM"].max())
#     cmap = plt.cm.coolwarm
#     colors = cmap(norm(yearly_avg["AVG_CONTAM"]))

#     sns.barplot(x="Year", y="AVG_CONTAM", data=yearly_avg, ax=axes[0], palette=colors)
#     axes[0].set_title("Average Contamination by Year")
#     axes[0].set_xlabel("Year")
#     axes[0].set_ylabel("Average Contamination")

#     year_labels = yearly_avg["Year"].astype(str).str[-2:]
#     axes[0].set_xticks(range(len(year_labels)))
#     axes[0].set_xticklabels(year_labels, rotation=45)

#     # --- Monthly plot ---
#     norm_month = mcolors.Normalize(vmin=monthly_avg["AVG_CONTAM"].min(), vmax=monthly_avg["AVG_CONTAM"].max())
#     colors_month = plt.cm.Greens(norm_month(monthly_avg["AVG_CONTAM"]))

#     sns.barplot(x="Month", y="AVG_CONTAM", data=monthly_avg, ax=axes[1], palette=colors_month)
#     axes[1].set_title("Average Contamination by Month")
#     axes[1].set_xlabel("Month")
#     axes[1].set_ylabel("Average Contamination")
#     axes[1].set_xticks(range(12))
#     axes[1].set_xticklabels(
#         ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

#     plt.tight_layout()
#     st.pyplot(fig)
# else:
#     st.warning("No 'DATA' column found — unable to calculate yearly/monthly averages.")






# import streamlit as st
# import pandas as pd
# import folium
# from folium.plugins import HeatMap
# from streamlit_folium import st_folium

# st.title("🌍 Contaminació Catalunya")

# # -------------------------
# # 🔗 List of GitHub raw CSV URLs
# base_url = "https://raw.githubusercontent.com/Nickless09/Contaminaci-En-Catalunya/main/dat/"
# file_names = [
#     "Qualitat_de_l_aire_part2.csv",
#     "Qualitat_de_l_aire_part2.csv",
#     "Qualitat_de_l_aire_part3.csv",
#     "Qualitat_de_l_aire_part4.csv",
#     "Qualitat_de_l_aire_part5.csv",
# ]  # 👈 add more filenames as needed

# urls = [base_url + name for name in file_names]

# # -------------------------
# # Cached CSV loader
# @st.cache_data(show_spinner=True)
# def load_multiple_csvs(url_list):
#     dfs = []
#     for url in url_list:
#         try:
#             df = pd.read_csv(url, encoding="UTF-8")
#             hour_cols = [f"{h:02d}h" for h in range(1, 25)]
#             if all(col in df.columns for col in hour_cols):
#                 df["AVG_CONTAM"] = df[hour_cols].mean(axis=1)
#             df = df.dropna(subset=["LATITUD", "LONGITUD", "AVG_CONTAM"])
#             dfs.append(df)
#         except Exception as e:
#             st.warning(f"⚠️ Could not read {url}: {e}")
#     if dfs:
#         return pd.concat(dfs, ignore_index=True)
#     else:
#         return pd.DataFrame(columns=["LATITUD", "LONGITUD", "AVG_CONTAM"])

# # -------------------------
# # Load all CSVs
# df = load_multiple_csvs(urls)

# if df.empty:
#     st.error("No data could be loaded. Check that your CSV URLs are correct and public.")
# else:
#     st.success(f"Loaded {len(df)} rows from {len(urls)} CSV files.")

#     # -------------------------
#     # Create Folium heatmap
#     map_center = [df["LATITUD"].mean(), df["LONGITUD"].mean()]
#     m = folium.Map(location=map_center, zoom_start=9)

#     heat_data = df[["LATITUD", "LONGITUD", "AVG_CONTAM"]].values.tolist()
#     HeatMap(heat_data, radius=15).add_to(m)

#     st_folium(m, width=700, height=500)
