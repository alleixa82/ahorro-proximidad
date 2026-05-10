import streamlit as st
from supabase import create_client

# Limpiamos las variables por si acaso hay espacios invisibles
URL = "https://ibqsxnnogdxffzahlmub.supabase.co".strip()
KEY = "EyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImlicXN4bm5vZ2R4ZmZ0YWhsbXViIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzgzNTU5NDgsImV4cCI6MjA5MzkzMTk0OH0.kh1ADj3hYJrlBRUqKRnHiktCLPd02Pwz3yWWFV3H59k".strip()

# Intentamos conectar
try:
    supabase = create_client(URL, KEY)
except Exception as e:
    st.error(f"Error al inicializar cliente: {e}")

st.title("📍 Ahorro de Proximidad")

if st.button("Buscar"):
    try:
        # Prueba de fuego: pedimos solo el nombre de las tiendas
        res = supabase.table("tiendas").select("nombre").execute()
        
        if res.data:
            st.success(f"✅ ¡CONECTADO! Tienes {len(res.data)} tiendas.")
            for t in res.data:
                st.write(f"🏠 {t['nombre']}")
        else:
            st.warning("Conexión OK, pero no hay tiendas en la base de datos.")
            
    except Exception as e:
        st.error(f"Fallo total de red: {e}")
        st.info("💡 Nota: El servidor dice que no encuentra 'ibqsxnnogdxffzahlmub.supabase.co'. Revisa que no falte ninguna letra en la URL de tu GitHub.")

st.divider()
st.camera_input("Capturar Ticket")
