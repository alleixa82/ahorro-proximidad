import streamlit as st
from supabase import create_client

# Credenciales (Verificadas)
URL = "https://ibqsxnnogdxffzahlmub.supabase.co"
KEY = "EyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImlicXN4bm5vZ2R4ZmZ0YWhsbXViIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzgzNTU5NDgsImV4cCI6MjA5MzkzMTk0OH0.kh1ADj3hYJrlBRUqKRnHiktCLPd02Pwz3yWWFV3H59k"

st.set_page_config(page_title="Ahorro Proximidad", layout="centered")

st.title("📍 Ahorro de Proximidad")

# Intentamos conectar nada más abrir la app
try:
    supabase = create_client(URL, KEY)
    st.success("🟢 El servidor de Supabase responde correctamente.")
except Exception as e:
    st.error(f"🔴 Error al conectar con el servidor: {e}")

# Botón de búsqueda de prueba
if st.button("Verificar Tablas"):
    try:
        # Probamos a leer la tabla de tiendas
        res = supabase.table("tiendas").select("*").execute()
        if res.data:
            st.info(f"Se han encontrado {len(res.data)} tiendas registradas.")
            for t in res.data:
                st.write(f"- {t['nombre']}")
        else:
            st.warning("⚠️ La base de datos está conectada pero la tabla 'tiendas' está vacía.")
            st.write("Siguiente paso: Insertar datos de prueba.")
    except Exception as e:
        st.error(f"No se pudo leer la tabla: {e}")

st.divider()
st.camera_input("📷 Escanea un ticket para empezar")
