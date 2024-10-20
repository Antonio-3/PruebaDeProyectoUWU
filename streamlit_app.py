import streamlit as st
from streamlit_option_menu import option_menu

## Logo de la empresa
st.sidebar.image(image='img/imagenProyecto.PNG',caption="")
st.sidebar.write("Bienvenido Admin!.")

st.sidebar.caption("Que desea hacer?")
st.sidebar.write("\n")
st.sidebar.selectbox("Seleccione una opcion:", ['Consultar tablas', 'Apartado de Asistencias'])

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
                "Autenticarse", 
                "Registrarse",
                "Personalizar",
                "Distribuir",                
                "Visualizar", #TODO visualiza stats y gráficos de correos enviados, hacer informes ? fechas etc, Visualizar el log aqui?
            ],
            )
