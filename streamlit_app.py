import streamlit as st
from streamlit_option_menu import option_menu


st.sidebar.image(image='img/imagenProyecto.PNG',caption="")
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
            options=[
                "Consultar tablas", 
                "Asistencias",
            ],
            )

        button("Decargar Reporte")
        
