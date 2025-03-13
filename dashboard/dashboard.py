import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("all_data.csv")
    return df

df = load_data()

# Mapping untuk hari dan bulan agar urut
day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
month_order = ["January", "February", "March", "April", "May", "June", 
               "July", "August", "September", "October", "November", "December"]
season_order = ["Fall", "Spring", "Summer", "Winter"]
# Pastikan kolom 'weekday' dan 'mnth' memiliki label yang benar


month_mapping = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June",
                 7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}


df["mnth"] = df["mnth"].map(month_mapping)

# Ubah 'mnth' dan 'weekday' menjadi kategori dengan urutan yang benar
df["mnth"] = pd.Categorical(df["mnth"], categories=month_order, ordered=True)
df["weekday"] = pd.Categorical(df["weekday"], categories=day_order, ordered=True)
df["season"] = pd.Categorical(df["season"], categories=season_order, ordered=True)

# Title
st.title("Dashboard Penyewaan Sepeda")

# Sidebar
st.sidebar.header("Filter")
tahun = st.sidebar.multiselect("Pilih Tahun", df['yr'].unique(), default=df['yr'].unique())
musim = st.sidebar.multiselect("Pilih Musim", df['season'].unique(), default=df['season'].unique())

# Filter Data
df_filtered = df[(df['yr'].isin(tahun)) & (df['season'].isin(musim))]

# Visualisasi Penyewaan Sepeda per Bulan
st.subheader("Jumlah Penyewaan Sepeda per Bulan")
df_monthly = df_filtered.groupby(["yr", "mnth"])["cnt"].sum().reset_index()
plt.figure(figsize=(10, 5))
sns.lineplot(data=df_monthly, x='mnth', y='cnt', hue='yr', marker="o")
plt.xlabel("Bulan")
plt.ylabel("Jumlah Penyewa")
plt.xticks(rotation=45)
st.pyplot(plt)

# Visualisasi Penyewaan Sepeda per Hari
st.subheader("Penyewaan Sepeda berdasarkan Hari")
df_per_hari = df_filtered.groupby("weekday", as_index=False)["cnt"].sum()
plt.figure(figsize=(10, 5))
sns.barplot(data=df_per_hari, x='weekday', y='cnt', palette="pastel")
plt.xlabel("Hari")
plt.ylabel("Jumlah Penyewa")
st.pyplot(plt)

# Visualisasi Penyewaan Sepeda per Jam
st.subheader("Penyewaan Sepeda berdasarkan Jam")
df_per_jam = df_filtered.groupby("hr", as_index=False)["cnt"].sum()
plt.figure(figsize=(10, 5))
sns.barplot(data=df_per_jam, x='hr', y='cnt', palette="Set3")
plt.xlabel("Jam dalam Sehari")
plt.ylabel("Jumlah Penyewa")
st.pyplot(plt)

# Hitung rata-rata penyewaan per jam
df_avg_per_hour = df_filtered.groupby("hr")["cnt"].mean().reset_index()

# Tambahkan kategori berdasarkan rata-rata penyewaan
def kategori_cluster(value):
    if value < 100:
        return "low"
    elif 100 <= value < 250:
        return "moderate"
    else:
        return "high"

df_avg_per_hour["Kategori"] = df_avg_per_hour["cnt"].apply(kategori_cluster)

# Visualisasi Penyewaan Sepeda per Jam berdasarkan Cluster
st.subheader("Penyewaan Sepeda per Jam berdasarkan 3 Cluster")
plt.figure(figsize=(10, 5))
sns.barplot(data=df_avg_per_hour, x='hr', y='cnt', hue="Kategori", palette={"low": "purple", "moderate": "blue", "high": "pink"})
plt.xlabel("Jam dalam Sehari")
plt.ylabel("Rata-rata Penyewaan Sepeda")
plt.legend(title="Kategori")
st.pyplot(plt)

# Visualisasi Penyewaan Sepeda berdasarkan Musim
st.subheader("Jumlah Penyewaan Sepeda berdasarkan Musim")
df_per_musim = df_filtered.groupby("season", as_index=False)["cnt"].sum()
plt.figure(figsize=(10, 5))
sns.barplot(data=df_per_musim, x='season', y='cnt', palette="muted")
plt.xlabel("Musim")
plt.ylabel("Jumlah Penyewa")
st.pyplot(plt)

# Footer
st.markdown("---")
st.markdown("**Dibuat oleh: Saftana Fitri**")
