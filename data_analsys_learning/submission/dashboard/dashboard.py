import streamlit as st
import pandas as pd
# !pip install seaborn
import seaborn as sns

import matplotlib.pyplot as plt

# Load the data
prsa_df = pd.read_csv('./main_data.csv')
# No,year,month,day,hour,PM2.5,PM10,SO2,NO2,CO,O3,TEMP,PRES,DEWP,RAIN,wd,WSPM,station

# Create a list of months
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
# Sidebar filters include all year or specific year
year = st.sidebar.selectbox('Year', ['All'] + list(prsa_df['year'].unique()))
if year != 'All':
    prsa_df = prsa_df[prsa_df['year'] == year]

# Display header
st.title("Visualisasi Data Kualitas Udara pada Nongzhanguan")


st.subheader(" Tingkat Polusi Udara di Nongzhanguan")
with st.container():
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("PM2.5 Levels by Month")
        fig1, ax1 = plt.subplots(figsize=(5, 4))
        sns.lineplot(x=prsa_df['month'], y=prsa_df['PM2.5'], marker='o', color='b', ax=ax1)
        ax1.set_title('PM2.5 Levels by Month')
        ax1.set_xticks(range(1, 13))
        ax1.set_xticklabels(months)
        ax1.set_xlabel('Month')
        ax1.set_ylabel('PM2.5 Levels')
        ax1.grid(True)
        st.pyplot(fig1)
    with col2:
        st.subheader("PM10 Levels by Month")
        fig2, ax2 = plt.subplots(figsize=(5, 4))
        sns.lineplot(x=prsa_df['month'], y=prsa_df['PM10'], marker='o', color='b', ax=ax2)
        ax2.set_title('PM10 Levels by Month')
        ax2.set_xticks(range(1, 13))
        ax2.set_xticklabels(months)
        ax2.set_xlabel('Month')
        ax2.set_ylabel('PM10 Levels')
        ax2.grid(True)
        st.pyplot(fig2)
    with col3:
        st.subheader("SO2 Levels by Month")
        fig3, ax3 = plt.subplots(figsize=(5, 4))
        sns.lineplot(x=prsa_df['month'], y=prsa_df['SO2'], marker='o', color='b', ax=ax3)
        ax3.set_title('SO2 Levels by Month')
        ax3.set_xticks(range(1, 13))
        ax3.set_xticklabels(months)
        ax3.set_xlabel('Month')
        ax3.set_ylabel('SO2 Levels')
        ax3.grid(True)
        st.pyplot(fig3)

with st.container():
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("NO2 Levels by Month")
        fig4, ax4 = plt.subplots(figsize=(5, 4))
        sns.lineplot(x=prsa_df['month'], y=prsa_df['NO2'], marker='o', color='b', ax=ax4)
        ax4.set_title('NO2 Levels by Month')
        ax4.set_xticks(range(1, 13))
        ax4.set_xticklabels(months)
        ax4.set_xlabel('Month')
        ax4.set_ylabel('NO2 Levels')
        ax4.grid(True)
        st.pyplot(fig4)
    with col2:
        st.subheader("CO Levels by Month")
        fig5, ax5 = plt.subplots(figsize=(5, 4))
        sns.lineplot(x=prsa_df['month'], y=prsa_df['CO'], marker='o', color='b', ax=ax5)
        ax5.set_title('CO Levels by Month')
        ax5.set_xticks(range(1, 13))
        ax5.set_xticklabels(months)
        ax5.set_xlabel('Month')
        ax5.set_ylabel('CO Levels')
        ax5.grid(True)
        st.pyplot(fig5)
    with col3:
        st.subheader("O3 Levels by Month")
        fig6, ax6 = plt.subplots(figsize=(5, 4))
        sns.lineplot(x=prsa_df['month'], y=prsa_df['O3'], marker='o', color='b', ax=ax6)
        ax6.set_title('O3 Levels by Month')
        ax6.set_xticks(range(1, 13))
        ax6.set_xticklabels(months)
        ax6.set_xlabel('Month')
        ax6.set_ylabel('O3 Levels')
        ax6.grid(True)
        st.pyplot(fig6)

st.markdown(
    """
    Tren ini menunjukkan pola musim yang jelas pada musim dingin yang memiliki tingkat polusi yang lebih tinggi kecuali untuk O3, peningkatan O3 di bulan-bulan panas mungkin disebabkan oleh intensitas sinar matahari yang lebih tinggi.
    """
)

st.subheader("Korelasi antara Hujan dan Tingkat Polusi Udara")
col1, col2 = st.columns(2)
with col1:
    st.subheader("Scatter Plot of Rain vs PM2.5")
    fig4, ax4 = plt.subplots(figsize=(5, 4))
    sns.scatterplot(x=prsa_df['RAIN'], y=prsa_df['PM2.5'], color='blue', ax=ax4)
    ax4.set_title('Scatter Plot of Rain vs PM2.5')
    ax4.set_xlabel('Rain')
    ax4.set_ylabel('PM2.5')
    ax4.grid(True)
    st.pyplot(fig4)

with col2:
    st.subheader("Scatter Plot of rain vs PM10")
    fig5, ax5 = plt.subplots(figsize=(5, 4))
    sns.scatterplot(x=prsa_df['RAIN'], y=prsa_df['PM10'], color='blue', ax=ax5)
    ax5.set_title('Scatter Plot of Rain vs PM10')
    ax5.set_xlabel('Rain')
    ax5.set_ylabel('PM10')
    ax5.grid(True)
    st.pyplot(fig5)

st.markdown(
    """
    Dari scatter plot di atas, menunjukkan korelasi antara hujan dan tingkat materi partikulat di atmosfer (PM2.5 dan
    PM10). Ini mungkin disebabkan oleh fakta bahwa hujan dapat membersihkan udara dari partikel-partikel
    polutan.
    """
)