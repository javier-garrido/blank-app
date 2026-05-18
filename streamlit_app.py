import streamlit as st
import joblib
import plotly.express as px

# 1. Configuración de la web
st.set_page_config(page_title="Tomato Digital Twin", layout="wide")
st.title("🍅 Simulador de Vida Útil Postcosecha (Digital Twin)")