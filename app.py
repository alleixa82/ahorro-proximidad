import streamlit as st
from supabase import create_client

# Credenciales directas (ya verificadas)
URL = "https://ibqsxnnogdxffzahlmub.supabase.co"
KEY = "EyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImlicXN4bm5vZ2R4ZmZ0YWhsbXViIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzgzNTU5NDgsImV4cCI6MjA5MzkzMTk0OH0.kh1ADj3hYJrlBRUqKRnHiktCLPd02Pwz3yWWFV3H59k"

# Conectar
supabase = create_client(URL, KEY)

st.title("📍 Ahorro de Proximidad")

st.write("Pulsa el botón para ver si la base de datos responde.")

if st.button("Ver tiendas"):
    try:
        # Traemos las tiendas de Supabase
        res = supabase.table("tiendas").select("*").execute()
        
        if res.data:
            st.success(f"✅ ¡Conectado! Hay {len(res.data)} tiendas.")
            for t in res.data:
                st.info(f"Tienda: {t['nombre']}")
        else:
            st.warning("Conectado, pero no hay tiendas creadas.")
            
    except Exception as e:
        st.error(f"Error: {e}")

st.divider()
st.camera_input("Escanear Ticket")


