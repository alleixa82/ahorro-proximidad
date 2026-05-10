import streamlit as st
from supabase import create_client

# Limpiamos la URL y la KEY de cualquier espacio invisible
URL = "https://ibqsxnnogdxffzahlmub.supabase.co".strip()
KEY = "EyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImlicXN4bm5vZ2R4ZmZ0YWhsbXViIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzgzNTU5NDgsImV4cCI6MjA5MzkzMTk0OH0.kh1ADj3hYJrlBRUqKRnHiktCLPd02Pwz3yWWFV3H59k".strip()

# Conectar
try:
    supabase = create_client(URL, KEY)
except Exception as e:
    st.error(f"Error al inicializar cliente: {e}")

st.title("📍 Ahorro de Proximidad")

if st.button("Ver tiendas"):
    try:
        # Traemos las tiendas
        res = supabase.table("tiendas").select("*").execute()
        
        if res.data:
            st.success(f"✅ ¡Conectado! Hay {len(res.data)} tiendas.")
            for t in res.data:
                st.info(f"Tienda: {t['nombre']}")
        else:
            st.warning("Conectado, pero la tabla está vacía.")
            
    except Exception as e:
        st.error(f"Error de red: {e}")

st.divider()
st.camera_input("Escanear Ticket")
