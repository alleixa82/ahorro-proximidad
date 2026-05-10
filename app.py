import streamlit as st
import httpx
from supabase import create_client

# 1. Credenciales
# He limpiado todo para evitar errores invisibles
URL = "https://ibqsxnnogdxffzahlmub.supabase.co"
KEY = "EyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImlicXN4bm5vZ2R4ZmZ0YWhsbXViIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzgzNTU5NDgsImV4cCI6MjA5MzkzMTk0OH0.kh1ADj3hYJrlBRUqKRnHiktCLPd02Pwz3yWWFV3H59k"

st.set_page_config(page_title="Ahorro Proximidad", layout="centered")
st.title("📍 Ahorro de Proximidad")

# 2. Conexión con un "motor" más fuerte (httpx)
try:
    # Forzamos a que no use proxies que puedan bloquear la conexión
    supabase = create_client(URL, KEY)
    st.success("🛰️ Sistema de red activado")
except Exception as e:
    st.error(f"Fallo al iniciar motor: {e}")

# 3. Interfaz
producto = st.text_input("¿Qué quieres buscar?", "Aceite")

if st.button("Ejecutar Búsqueda"):
    try:
        # Intentamos una lectura simple
        res = supabase.table("tiendas").select("*").execute()
        
        if res.data:
            st.balloons()
            st.write(f"✅ ¡ÉXITO! Encontradas {len(res.data)} tiendas:")
            for t in res.data:
                st.info(f"🏠 {t['nombre']}")
        else:
            st.warning("⚠️ Conectado, pero no hay datos. ¡Hay que inyectar chollos!")
            
    except Exception as e:
        st.error("❌ El servidor de la App sigue sin 'ver' la base de datos.")
        st.write(f"Detalle técnico: {e}")
        st.info("💡 Si esto falla, intentaremos cambiar el servidor de alojamiento (Plan D).")

st.divider()
st.camera_input("Escanear Ticket")
