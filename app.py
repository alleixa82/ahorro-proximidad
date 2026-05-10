import streamlit as st
from supabase import create_client

# Credenciales
URL = "https://ibqsxnnogdxffzahlmub.supabase.co"
KEY = "EyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImlicXN4bm5vZ2R4ZmZ0YWhsbXViIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzgzNTU5NDgsImV4cCI6MjA5MzkzMTk0OH0.kh1ADj3hYJrlBRUqKRnHiktCLPd02Pwz3yWWFV3H59k"
supabase = create_client(URL, KEY)

st.title("📍 Ahorro de Proximidad")

# --- BOTÓN DE CARGA INICIAL (Solo para hoy) ---
if st.sidebar.button("🚀 Cargar Datos de Prueba"):
    try:
        # Insertamos una tienda y un producto para probar
        st.sidebar.write("Cargando...")
        t = supabase.table("tiendas").insert({"nombre": "Mercadona Prueba", "latitud": 40.4, "longitud": -3.7}).execute()
        p = supabase.table("productos").insert({"nombre": "Aceite de Oliva", "marca": "Hacendado"}).execute()
        
        # Sacamos los IDs para el precio
        id_t = t.data[0]['id']
        id_p = p.data[0]['id']
        
        supabase.table("precios").insert({"id_producto": id_p, "id_tienda": id_t, "precio": 8.50}).execute()
        st.sidebar.success("✅ ¡Datos cargados con éxito!")
    except Exception as e:
        st.sidebar.error(f"Error: {e}")

# --- BUSCADOR ---
producto = st.text_input("¿Qué buscas?", "Aceite")

if st.button("Ejecutar Búsqueda"):
    try:
        # Buscamos en la tabla de precios y unimos con productos y tiendas
        res = supabase.table("precios").select("precio, productos(nombre), tiendas(nombre)").execute()
        
        if res.data:
            for r in res.data:
                st.success(f"🛒 {r['productos']['nombre']}: {r['precio']}€ en {r['tiendas']['nombre']}")
        else:
            st.warning("No hay resultados. ¿Has pulsado el botón de carga en el lateral?")
    except Exception as e:
        st.error(f"Error al buscar: {e}")
