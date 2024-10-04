import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Judul Dashboard
st.title("Bike Sharing Analysis Dashboard")

# Load Dataset
@st.cache_data
def load_data():
    day_df = pd.read_csv('day.csv')
    hour_df = pd.read_csv('hour.csv')
    day_df['dteday'] = pd.to_datetime(day_df['dteday'])
    hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])
    return day_df, hour_df

day_df, hour_df = load_data()

# Sidebar untuk memilih analisis
st.sidebar.title("Pilih Analisis")
option = st.sidebar.selectbox("Pilih opsi analisis:", 
                                ["Pola Penggunaan Sepeda", 
                                 "Total Penyewaan Berdasarkan Musim dan Hari Kerja"])

# Analisis pola penggunaan sepeda
if option == "Pola Penggunaan Sepeda":
    st.subheader("Pola Penggunaan Sepeda Berdasarkan Waktu")
    
    # Berdasarkan Jam
    st.write("### Berdasarkan Jam")
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=hour_df, x='hr', y='cnt')
    plt.title('Jumlah Penyewaan Sepeda Berdasarkan Jam')
    plt.xlabel('Jam')
    plt.ylabel('Jumlah Penyewaan')
    plt.xticks(range(0, 24))
    st.pyplot(plt)
    plt.clf()

    # Berdasarkan Hari dalam Seminggu
    st.write("### Berdasarkan Hari")
    plt.figure(figsize=(12, 6))
    sns.barplot(data=day_df, x='weekday', y='cnt', estimator=sum)
    plt.title('Jumlah Penyewaan Sepeda Berdasarkan Hari dalam Seminggu')
    plt.xlabel('Hari (0=Senin, 6=Minggu)')
    plt.ylabel('Jumlah Penyewaan')
    plt.xticks([0, 1, 2, 3, 4, 5, 6], ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu'])
    st.pyplot(plt)
    plt.clf()

    # Berdasarkan Bulan
    st.write("### Berdasarkan Bulan")
    plt.figure(figsize=(12, 6))
    sns.barplot(data=day_df, x='mnth', y='cnt', estimator=sum)
    plt.title('Jumlah Penyewaan Sepeda Berdasarkan Bulan')
    plt.xlabel('Bulan')
    plt.ylabel('Jumlah Penyewaan')
    plt.xticks(range(0, 12), ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Agt', 'Sep', 'Okt', 'Nov', 'Des'])
    st.pyplot(plt)
    plt.clf()

# Analisis total penyewaan berdasarkan musim dan hari kerja
elif option == "Total Penyewaan Berdasarkan Musim dan Hari Kerja":
    st.subheader("Total Penyewaan Berdasarkan Musim dan Hari Kerja")
    
    # Total Penyewaan Berdasarkan Musim
    st.write("### Total Penyewaan Berdasarkan Musim")
    season_counts = day_df.groupby('season')['cnt'].sum().reset_index()
    season_counts = season_counts.sort_values(by='cnt', ascending=False)
    
    # Tampilkan hasil di Streamlit
    st.write("Total penyewaan berdasarkan musim:")
    st.write(season_counts)

    # Visualisasi total penyewaan berdasarkan musim
    plt.figure(figsize=(12, 6))
    sns.barplot(data=season_counts, x='season', y='cnt')
    plt.title('Total Penyewaan Sepeda Berdasarkan Musim')
    plt.xlabel('Musim (1: Musim Dingin, 2: Musim Semi, 3: Musim Panas, 4: Musim Gugur)')
    plt.ylabel('Jumlah Penyewaan')
    plt.xticks([0, 1, 2, 3], ['Musim Dingin', 'Musim Semi', 'Musim Panas', 'Musim Gugur'])
    st.pyplot(plt)
    plt.clf()

    # Total Penyewaan Berdasarkan Hari Kerja
    st.write("### Total Penyewaan Berdasarkan Hari Kerja")
    workingday_counts = day_df.groupby('workingday')['cnt'].sum().reset_index()
    workingday_counts = workingday_counts.sort_values(by='cnt', ascending=False)

    # Ubah nilai 0 dan 1 menjadi keterangan 'Tidak' dan 'Ya'
    workingday_counts['workingday'] = workingday_counts['workingday'].replace({0: 'Tidak', 1: 'Ya'})
    
    # Tampilkan hasil di Streamlit
    st.write("\nTotal penyewaan berdasarkan hari kerja:")
    st.write(workingday_counts)

    # Visualisasi total penyewaan berdasarkan hari kerja
    plt.figure(figsize=(12, 6))
    sns.barplot(data=workingday_counts, x='workingday', y='cnt')
    plt.title('Total Penyewaan Sepeda Berdasarkan Hari Kerja')
    plt.xlabel('Hari Kerja')
    plt.ylabel('Jumlah Penyewaan')
    st.pyplot(plt)
    plt.clf()
