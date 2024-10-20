import streamlit as st
from streamlit_option_menu import option_menu


st.sidebar.image(image='img/LogoPerla.png',caption="")
st.sidebar.caption("Bienvenido Admin!.")


st.set_page_config(
       page_title="Menu" 
)

class   MultiApp:
        def __init__(self):
                self.apps=[]
        def add_app(self, title, func):
                self.apps.append({
                        "title": title,
                        "function": function
                })
        def run():
            with st.sidebar:
                seleccion_menu = option_menu(
                     menu_title="Menú",
                    options=["Consultar tablas", "Asistencias"],
                    styles={
                          "container": {"padding": "5!important", "background-color": 'black'}                  
                    }
                )
