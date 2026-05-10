import streamlit as st
from supabase import create_client

# Configuración de página y estilo
st.set_page_config(page_title="Ahorro Proximidad", page_icon="📍", layout="centered")

# CSS inyectado para mejorar el look
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #27ae60; color: white; }
    .price-card { background: white; padding: 15px; border-radius: 15px; border-left: 5px solid #27ae60; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_stdio=True)

# Credenciales (Verificadas)
URL = "https://ibqsxnnogdxffzahlmub.supabase.co"
KEY = "EyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImlicXN4bm5vZ2R4ZmZ0YWhsbXViIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NzgzNTU5NDgsImV4cCI6MjA5MzkzMTk0OH0.kh1ADj3hYJrlBRUqKRnHiktCLPd02Pwz3yWWFV3H59k"
supabase = create_client(URL, KEY)

# --- INTERFAZ ---
st.title("📍 Mi Radar de Ahorro")
st.caption("Barcelona - Radio 5km")

tab1, tab2 = st.tabs(["🔍 Buscar Chollos", "📸 Subir Ticket"])

with tab1:
    producto = st.text_input("¿Qué producto buscas?", placeholder="Ej: Aceite de Oliva")
    
    if st.button("Buscar en mi zona"):
        # Simulamos la carga de datos con estilo
        with st.spinner('Escaneando supermercados cercanos...'):
            st.markdown("### 🛒 Mejores opciones encontradas:")
            
            # Tarjeta de producto 1
            st.markdown(f"""
            <div class="price-card">
                <span style="color: #27ae60; font-weight: bold;">MÁS BARATO</span>
                <h4>Aceite Oliva 1L (Hacendado)</h4>
                <p style="margin:0;">📍 <b>Mercadona Centro</b> (0.35 km)</p>
                <h2 style="margin:0; color: #27ae60;">8,50€</h2>
            </div>
            """, unsafe_allow_html=True)
            
            # Tarjeta de producto 2
            st.markdown(f"""
            <div class="price-card" style="border-left-color: #95a5a6;">
                <h4>Aceite Oliva 1L (Carbonell)</h4>
                <p style="margin:0;">📍 <b>Carrefour Express</b> (0.90 km)</p>
                <h2 style="margin:0; color: #333;">9,10€</h2>
            </div>
            """, unsafe_allow_html=True)

with tab2:
    st.subheader("¡Gana puntos compartiendo!")
    st.write("Haz una foto a tu ticket y nosotros actualizamos los precios para todos.")
    foto = st.camera_input("Capturar ticket de compra")
    if foto:
        st.balloons()
        st.success("¡Ticket recibido! Procesando datos con IA...")

