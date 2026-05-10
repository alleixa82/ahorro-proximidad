import streamlit as st
from supabase import create_client

# --- TUS CREDENCIALES VERIFICADAS ---
URL = "https://ibqsxnnogdxffzahlmub.supabase.co"
KEY = "EyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImlicXN4bm5vZ2R4ZmZ0YWhsbXViIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzgzNTU5NDgsImV4cCI6MjA5MzkzMTk0OH0.kh1ADj3hYJrlBRUqKRnHiktCLPd02Pwz3yWWFV3H59k"

# Inicialización del cliente
supabase = create_client(URL, KEY)

st.set_page_config(page_title="Ahorro Proximidad", page_icon="📍")

st.title("📍 Ahorro de Proximidad")

# Buscador de productos
producto = st.text_input("¿Qué buscas hoy?", "Aceite")

if st.button("Buscar Ofertas"):
    try:
        # Esto busca en tu tabla de Supabase
        res = supabase.table("tiendas").select("*").execute()
        
        if res.data:
            st.success(f"✅ Conectado. Hemos encontrado {len(res.data)} tiendas cerca.")
            for t in res.data:
                st.write(f"🏠 {t['nombre']} - {t.get('direccion', 'Sin dirección')}")
        else:
            st.warning("Conexión OK, pero no hay tiendas en la base de datos.")
            
    except Exception as e:
        st.error(f"Error de conexión: {e}")

st.divider()

# Sección de escáner
st.subheader("📸 Sube tu ticket")
foto = st.camera_input("Haz una foto al ticket para actualizar precios")

if foto:
    st.info("¡Ticket recibido! Procesando datos...")
