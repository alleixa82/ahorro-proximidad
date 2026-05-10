import streamlit as st
from supabase import create_client
import pandas as pd

# CONFIGURACIÓN TÉCNICA - VERIFICADA
URL = "https://ibqsxnnogdxffzahlmub.supabase.co"
KEY = "EyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImlicXN4bm5vZ2R4ZmZ0YWhsbXViIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzgzNTU5NDgsImV4cCI6MjA5MzkzMTk0OH0.kh1ADj3hYJrlBRUqKRnHiktCLPd02Pwz3yWWFV3H59k"

# Inicialización segura del cliente
@st.cache_resource
def get_supabase():
    return create_client(URL, KEY)

supabase = get_supabase()

# INTERFAZ
st.set_page_config(page_title="Ahorro Proximidad v1.0", layout="centered")
st.title("📍 Ahorro de Proximidad")

tab1, tab2 = st.tabs(["🔍 Buscar Chollos", "📸 Subir Ticket"])

with tab1:
    st.subheader("Buscador de precios reales")
    producto = st.text_input("¿Qué buscas?", "Aceite")
    
    if st.button("Ejecutar Búsqueda"):
        try:
            # Consulta ultra-simple a la tabla de tiendas para validar conexión
            query = supabase.table("tiendas").select("*").execute()
            
            if query.data:
                st.success(f"📡 Conexión exitosa. {len(query.data)} tiendas detectadas.")
                df = pd.DataFrame(query.data)
                st.dataframe(df[['nombre', 'direccion']]) # Mostramos tabla limpia
            else:
                st.warning("La base de datos respondió, pero no hay tiendas creadas.")
                
        except Exception as e:
            st.error(f"Fallo técnico de conexión: {str(e)}")

with tab2:
    st.info("Saca una foto a tu ticket de compra para actualizar los precios de la zona.")
    st.camera_input("Cámara")

st.caption("v1.0.2 - Conectado a Supabase Cloud")
