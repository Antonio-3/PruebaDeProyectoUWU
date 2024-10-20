import streamlit as st
from streamlit_option_menu import option_menu

## Logo de la empresa
st.sidebar.image(image='img/imagenProyecto.PNG',caption="")
st.sidebar.write("Bienvenido Admin!.")

st.sidebar.caption("Que desea hacer?")
st.sidebar.write("\n")
st.sidebar.selectbox("Seleccione una opcion:", ['Consultar tablas', 'Apartado de Asistencias'])

st.sidebar.title("Menu")
opciones=["Consultar tablas", "Apartado de Asistencias"]

st.sidebar.seleccion_menu = option_menu(
            menu_title="Menú",
            options=[
                "Autenticarse", 
                "Registrarse",
                "Personalizar",
                "Distribuir",                
            ]
            )
