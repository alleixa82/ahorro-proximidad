import streamlit as st
from supabase import create_client

# 1. Credenciales limpias (He quitado cualquier espacio invisible)
URL = "https://ibqsxnnogdxffzahlmub.supabase.co"
KEY = "EyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImlicXN4bm5vZ2R4ZmZ0YWhsbXViIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzgzNTU5NDgsImV4cCI6MjA5MzkzMTk0OH0.kh1ADj3hYJrlBRUqKRnHiktCLPd02Pwz3yWWFV3H59k"

# Inicializamos conexión
try:
    supabase = create_client(URL, KEY)
except Exception as e:
    st.error("Error al configurar la conexión")

st.title("📍 Ahorro de Proximidad")

# 2. Formulario de búsqueda
with st.form("buscador"):
    producto = st.text_input("¿Qué buscas?", "Aceite")
    boton = st.form_submit_button("Ejecutar Búsqueda")

if boton:
    try:
        # Intentamos una consulta súper simple a la tabla tiendas
        res = supabase.table("tiendas").select("*").execute()
        
        if res.data:
            st.success(f"✅ ¡Conexión OK! Encontradas {len(res.data)} tiendas.")
            for t in res.data:
                st.write(f"🏠 {t['nombre']}")
        else:
            st.warning("📡 Conectado, pero no hay datos. ¡Usa el botón de abajo para cargar demo!")
            
    except Exception as e:
        st.error(f"❌ Error de red: {e}")

# 3. BOTÓN MÁGICO PARA CARGAR DATOS DESDE EL MÓVIL
st.divider()
if st.button("🚀 CARGAR DATOS DE PRUEBA"):
    try:
        # Insertamos una tienda de prueba directamente desde la App
        test_tienda = {"nombre": "Mercadona Prueba", "latitud": 40.0, "longitud": -3.0}
        supabase.table("tiendas").insert(test_tienda).execute()
        st.balloons()
        st.success("¡Datos cargados! Dale a 'Buscar' ahora.")
    except Exception as e:
        st.error(f"No se pudo cargar: {e}")
