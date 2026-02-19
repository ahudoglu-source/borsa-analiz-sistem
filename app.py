streamlit
yfinance
pandas
plotly
import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

# Sayfa Ayarları
st.set_page_config(page_title="Borsa Analiz Paneli", layout="wide", page_icon="📈")

# Stil Düzenlemesi
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .stMetric {
        background-color: #1e2130;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #31333f;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 Borsa İstanbul Pro Analiz Portalı")
st.sidebar.header("🛠️ İşlem Paneli")

# Kullanıcı Girişleri
hisse = st.sidebar.text_input("Hisse Kodu (Örn: UCAYM, THYAO, SASA)", "UCAYM").upper()
ticker = f"{hisse}.IS"
periyot = st.sidebar.selectbox("Zaman Aralığı", ["1mo", "3mo", "6mo", "1y", "2y"], index=3)

# Veri Çekme Fonksiyonu
@st.cache_data
def veri_indir(t):
    return yf.download(t, period=periyot)

data = veri_indir(ticker)

if not data.empty:
    # Teknik Göstergeler
    data['MA20'] = data['Close'].rolling(window=20).mean()
    data['MA50'] = data['Close'].rolling(window=50).mean()
