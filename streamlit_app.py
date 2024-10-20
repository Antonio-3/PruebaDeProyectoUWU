import streamlit as st
from streamlit_option_menu import option_menu
import ConsultarTablas, Asistencias


st.sidebar.image(image='img/imagenProyecto.PNG',caption="")
st.sidebar.caption("Bienvenido Admin!.")

class MultiApplicaciones:
        def _init_(self):
            self.apps= []
        def add_app(self, title, function):
            self.apps.append({
                "title": title
                "function": function
            })

        def correr():
            
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
st.sidebar.write("\n")
st.sidebar.button("Generar Reportes")
        
