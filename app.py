import streamlit as st
from supabase import create_client

# Configuración básica
url = "https://ibqsxnnogdxffzahlmub.supabase.co"
key = "TU_KEY_QUE_PEGASTE_ANTES"
supabase = create_client(url, key)

st.title("📍 Mi App de Ahorro")
st.write("¡Bienvenido a tu radar de precios!")

# Buscador de ejemplo
busqueda = st.text_input("¿Qué producto buscas?")
if st.button("Buscar"):
    st.success(f"Buscando {busqueda} cerca de ti...")

# Botón de cámara (esto es lo que la hace funcional)
st.divider()
st.camera_input("📸 Escanea un ticket para actualizar")
