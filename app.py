import streamlit as st           # <--- ESTA ES LA LÍNEA QUE FALTA
from supabase import create_client

# El resto de tu código igual...
st.title("📍 Ahorro de Proximidad")

if st.button("Buscar"):
    # Buscamos en la tabla de precios de tu Supabase real
    res = supabase.table("precios").select("precio, tiendas(nombre, direccion), productos(nombre)").eq("productos.nombre", producto).execute()
    
    if res.data:
        for item in res.data:
            st.write(f"✅ {item['productos']['nombre']} a **{item['precio']}€**")
            st.caption(f"En {item['tiendas']['nombre']} ({item['tiendas']['direccion']})")
    else:
        st.warning("No tenemos precios para ese producto todavía. ¡Sé el primero en subir un ticket!")
