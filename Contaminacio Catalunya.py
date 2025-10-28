import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors  # ✅ This is what fixes your error
import folium
from folium.plugins import HeatMap
from streamlit_folium import st_folium

st.title("🌍 Contaminació Catalunya")

# -------------------------
# 🔗 GitHub raw CSV URLs
base_url = "https://raw.githubusercontent.com/Nickless09/Contaminaci-En-Catalunya/main/dat/"
file_names = [f"Qualitat_de_l_aire_part{i}.csv" for i in range(2, 5)]  # 👈 change to range(1, 71) for all 70 files
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
    # if dfs:
    #     return pd.concat(dfs, ignore_index=True)
    # else:
    #     return pd.DataFrame(columns=["LATITUD", "LONGITUD", "AVG_CONTAM"])

# -------------------------
# ✅ Load all CSVs (note the correct function call!)
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

 # -------------------------
    # 📊 Average Contamination by Hour
    st.subheader("📈 Mitjana de Contaminació per Hora del Dia")

    hour_cols = [f"{h:02d}h" for h in range(1, 25)]
    valid_hour_cols = [col for col in hour_cols if col in df.columns]

    if valid_hour_cols:
        avg_per_hour = df[valid_hour_cols].mean()
        data = pd.DataFrame({
            'Hour': list(range(1, len(valid_hour_cols) + 1)),
            'Average Contamination': avg_per_hour.values
        })

        plt.figure(figsize=(12, 6))
        sns.barplot(x='Hour', y='Average Contamination', data=data, palette='viridis')
        plt.title('Average Contamination by Hour of the Day')
        plt.xlabel('Hour of the Day')
        plt.ylabel('Average Contamination')
        plt.xticks(rotation=0)

        st.pyplot(plt)
    else:
        st.warning("No hourly data found in the loaded CSVs.")
        
# -------------------------
# 📅 Average Contamination by Year and Month
st.subheader("📅 Mitjana Anual i Mensual de Contaminació")

if "DATA" in df.columns:
    df["DATA"] = pd.to_datetime(df["DATA"], errors="coerce")
    df["Year"] = df["DATA"].dt.year
    df["Month"] = df["DATA"].dt.month

    yearly_avg = df.groupby("Year", as_index=False)["AVG_CONTAM"].mean()
    monthly_avg = df.groupby("Month", as_index=False)["AVG_CONTAM"].mean()

    fig, axes = plt.subplots(1, 2, figsize=(14, 4))

    # --- Yearly plot ---
    norm = mcolors.Normalize(vmin=yearly_avg["AVG_CONTAM"].min(), vmax=yearly_avg["AVG_CONTAM"].max())
    cmap = plt.cm.coolwarm
    colors = cmap(norm(yearly_avg["AVG_CONTAM"]))

    sns.barplot(x="Year", y="AVG_CONTAM", data=yearly_avg, ax=axes[0], palette=colors)
    axes[0].set_title("Average Contamination by Year")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Average Contamination")

    year_labels = yearly_avg["Year"].astype(str).str[-2:]
    axes[0].set_xticks(range(len(year_labels)))
    axes[0].set_xticklabels(year_labels, rotation=45)

    # --- Monthly plot ---
    norm_month = mcolors.Normalize(vmin=monthly_avg["AVG_CONTAM"].min(), vmax=monthly_avg["AVG_CONTAM"].max())
    colors_month = plt.cm.Greens(norm_month(monthly_avg["AVG_CONTAM"]))

    sns.barplot(x="Month", y="AVG_CONTAM", data=monthly_avg, ax=axes[1], palette=colors_month)
    axes[1].set_title("Average Contamination by Month")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Average Contamination")
    axes[1].set_xticks(range(12))
    axes[1].set_xticklabels(
        ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

    plt.tight_layout()
    st.pyplot(fig)
else:
    st.warning("No 'DATA' column found — unable to calculate yearly/monthly averages.")






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
