import streamlit as st
from streamlit_option_menu import option_menu
import sqlite3
import pandas as pd

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
            options=["Inicio","Consultar tablas", "Asistencias", "Generar Reportes"]
        )

if seleccion_menu == "Inicio":
        st.image(image='img/LogoUnixd.png', caption="", use_column_width=True)
        st.write("\n")
        st.title("Bienvenidos a nuestro proyecto :)")
        st.write("Somos Antonio, Perla , Josue y Danahy, estudiantes de la Universidad De Colima. ")
        st.write("\n")
        st.write("Este proyecto tiene como objetivo crear un programa para que un admistrador pueda consultar o asignar las faltas de asistencia de profesores, materias, o dependiendo del programa educativo")
        st.write("\n")
        st.write("A lo largo de esta página, encontrarás información sobre nuestro trabajo, ideas y logros a lo largo del proceso. Esperamos que disfrutes navegando por nuestra página y descubras más sobre este proyecto.")

                
if seleccion_menu == "Consultar tablas":
        st.title("Tablas")
        # Conectar a la base de datos
        conexion = sqlite3.connect('BasePrueba/ProfesoresPrueba.db')
        cursor = conexion.cursor()
        # Seleccionar todas las materias
        cursor.execute('''
        SELECT * FROM materiaprofe
         ''')
        # Recuperar todos los registros
        xd = cursor.fetchall()
        # Mostrar los registros de forma estructurada
        st.write("\nLista de Proferores:\n")
        st.write("{:<5} {:<25} {:<20} {:<10} {:20} {:<25} {:<20}".format('ID', 'Profesor', 'Materia', 'Carrera','Fecha','Horario','Asistencia'))
        st.write("-" * 60)
        for lol in xd:
                st.write("{:<5} {:<25} {:<20} {:<10} {:<25} {:<20} {:<10}".format(lol[0], lol[1], lol[2],
                 lol[3], lol[4], lol[5], lol[6]))
        conexion.close()

        
if seleccion_menu == "Asistencias":
        st.title("Asistencias")


if seleccion_menu == "Generar Reportes":
        st.title("Generar Reportes")
        # Conectar a la base de datos
        conexion = sqlite3.connect('BasePrueba/ProfesoresPrueba.db')
        df = pd.read_sql("SELECT DISTINCT Profesor FROM materiaprofe;", conexion)
        cursor = conexion.cursor()
        # Seleccionar todas las materias
        cursor.execute('''
        SELECT DISTINCT Profesor FROM materiaprofe
         ''')
        # Recuperar todos los registros
        xd = cursor.fetchall()

        seleccion_profe = st.selectbox('Selecciona un profesor:', xd['Profesor'])
    
pr = st.sidebar.button("Generar Reportes")
if pr==True:
        st.write("xd")
        
