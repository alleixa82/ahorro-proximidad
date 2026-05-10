import streamlit as st
from supabase import create_client

# He limpiado la URL y la KEY de cualquier posible error de formato
SUPABASE_URL = "https://ibqsxnnogdxffzahlmub.supabase.co".strip()
SUPABASE_KEY = "EyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImlicXN4bm5vZ2R4ZmZ0YWhsbXViIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzgzNTU5NDgsImV4cCI6MjA5MzkzMTk0OH0.kh1ADj3hYJrlBRUqKRnHiktCLPd02Pwz3yWWFV3H59k".strip()

# Intentamos conectar con un tiempo de espera (timeout)
@st.cache_resource
def get_supabase():
    return create_client(SUPABASE_URL, SUPABASE_KEY)

try:
    supabase = get_supabase()
    st.success("🛰️ Motor de búsqueda listo")
except Exception as e:
    st.error(f"Error de inicialización: {e}")

st.title("📍 Ahorro de Proximidad")

# Formulario simple
with st.form("mi_busqueda"):
    prod = st.text_input("Producto", "Aceite")
    submit = st.form_submit_button("Buscar Chollos")

if submit:
    try:
        # Prueba de fuego: leer cualquier cosa de la tabla tiendas
        data = supabase.table("tiendas").select("*").limit(1).execute()
        st.write("✅ Conexión establecida con éxito.")
        st.json(data.data)
    except Exception as e:
        st.error(f"Fallo de red: {e}")
        st.info("💡 Consejo: Si el error persiste, intenta borrar la app en Streamlit Cloud y volverla a crear (Deploy) para que cambie de servidor.")
