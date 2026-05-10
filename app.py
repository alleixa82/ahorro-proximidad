import streamlit as st
from supabase import create_client

# CREDENCIALES VERIFICADAS POR GEMINI
URL = "https://ibqsxnnogdxffzahlmub.supabase.co"
KEY = "EyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImlicXN4bm5vZ2R4ZmZ0YWhsbXViIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzgzNTU5NDgsImV4cCI6MjA5MzkzMTk0OH0.kh1ADj3hYJrlBRUqKRnHiktCLPd02Pwz3yWWFV3H59k"

# Conexión global
supabase = create_client(URL, KEY)

st.title("📍 Ahorro de Proximidad")

producto = st.text_input("¿Qué buscas?", "Aceite")

if st.button("Buscar"):
    try:
        # Consulta sencilla para probar conexión
        res = supabase.table("tiendas").select("*").execute()
        
        if res.data:
            st.success(f"✅ ¡Conexión establecida! Hemos encontrado {len(res.data)} tiendas en tu base de datos.")
            for t in res.data:
                st.write(f"🏠 {t['nombre']} - {t.get('direccion', 'Sin dirección')}")
        else:
            st.warning("Conectado a Supabase, pero la tabla 'tiendas' está vacía.")
            
    except Exception as e:
        st.error(f"Error de conexión: {e}")

st.divider()
st.camera_input("Capturar Ticket")
