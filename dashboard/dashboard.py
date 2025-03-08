import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# oleh Saftana Fitri
@st.cache_data
def load_data():
    df = pd.read_csv("all_data.csv")
    df['season'] = df['season'].replace({1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'})
    df['yr'] = df['yr'].replace({0: 2011, 1: 2012})
    df['weekday'] = df['weekday'].replace({0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday'})
    return df

df = load_data()

# Sidebar filter
st.sidebar.header("Filter Data")
year = st.sidebar.selectbox("Pilih Tahun", df['yr'].unique())

# Filter data sesuai input pengguna
filtered_df = df[(df['yr'] == year)]

st.title("📊 Dashboard Penyewaan Sepeda")
st.subheader(f"Jumlah Penyewaan Sepeda pada Tahun {year}")

# Tabs untuk berbagai visualisasi
tabs = st.tabs(["📊 Bulan", "🌍 Musim", "📅 Harian", "⏳ Tren Waktu"])

with tabs[0]:
    st.subheader("Jumlah Penyewaan Sepeda Berdasarkan Bulan")
    fig = px.bar(filtered_df, x='mnth', y='cnt', color='cnt', labels={'mnth': 'Bulan', 'cnt': 'Jumlah Penyewaan'},
                 title="Penyewaan Sepeda per Bulan", color_continuous_scale='blues')
    fig.update_layout(xaxis=dict(tickmode='array', tickvals=list(range(1, 13)), 
                                 ticktext=['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Agu', 'Sep', 'Okt', 'Nov', 'Des']))
    st.plotly_chart(fig)

with tabs[1]:
    st.subheader("Persentase Penyewaan Sepeda Berdasarkan Musim")
    season_counts = df.groupby("season")['cnt'].sum().reset_index()
    fig2 = px.pie(season_counts, names='season', values='cnt', title="Distribusi Penyewaan Sepeda per Musim",
                  color_discrete_sequence=px.colors.qualitative.Set3)
    st.plotly_chart(fig2)

with tabs[2]:
    st.subheader("Jumlah Penyewaan Sepeda Berdasarkan Hari")
    daily_counts = df.groupby("weekday")['cnt'].sum().reset_index()
    fig3 = px.bar(daily_counts, x='weekday', y='cnt', title="Penyewaan Sepeda per Hari",
                  labels={'weekday': 'Hari', 'cnt': 'Jumlah Penyewaan'}, color='cnt', color_continuous_scale='thermal')
    st.plotly_chart(fig3)

with tabs[3]:
    st.subheader("Tren Penyewaan Sepeda Sepanjang Hari")

    time_series = df.groupby(['yr', 'hr'])['cnt'].sum().reset_index()

    fig4 = px.line(
        time_series, 
        x='hr', 
        y='cnt', 
        color='yr', 
        markers=True,
        labels={'hr': 'Jam', 'cnt': 'Jumlah Penyewaan', 'yr': 'Tahun'},
        title="Tren Penyewaan Sepeda per Jam"
    )

    fig4.update_layout(
        xaxis=dict(
            tickmode='array', 
            tickvals=list(range(0, 24)), 
            ticktext=[f"{h}:00" for h in range(0, 24)]  
        )
    )
    st.plotly_chart(fig4)


