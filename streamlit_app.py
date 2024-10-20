import streamlit as st
from streamlit_option_menu import option_menu

st.sidebar.image(image='img/LogoPerla.png',caption="")
st.sidebar.caption("Bienvenido Admin!.")

with st.sidebar:
        beta_sign = """
        <span style="
        font-size: 10px;
        font-weight: bold;
        color: #ffffff;
        background-color: #ff5733;
        padding: 5px 10px;
        border-radius: 4px;
        ">
            BETA
        </span>
        """
        seleccion_menu = option_menu(
            menu_title="Menú",
            options=["Inicio","Consultar tablas", "Asistencias"]
        )

if seleccion_menu == "Inicio":
        st.image(image='img/LogoUnixd.png', caption="", use_column_width=True)
        st.write("\n")
        st.title("Bienvenidos a PAJD")
        St.write("Somos Antonio, Perla , Josue y Danahy, estudiantes de la Universidad De Colima. ")
        st.write("\n")
        St.write("Este proyecto tiene como objetivo crear un programa para que un admistrador pueda consultar o asignar las faltas de asistencia de profesores, materias, o dependiendo del programa educativo")
        st.write("\n")
        St.write("A lo largo de esta página, encontrarás información sobre nuestro trabajo, ideas y logros a lo largo del proceso. Esperamos que disfrutes navegando por nuestra página y descubras más sobre este emocionante proyecto.")

                
if seleccion_menu == "Consultar tablas":
        st.write("Prueba")
st.sidebar.write("\n")
st.sidebar.button("Generar Reportes")
        
