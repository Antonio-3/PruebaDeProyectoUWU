import streamlit as st
from streamlit_option_menu import option_menu
import sqlite3

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
        conexion = sqlite3.connect('..\BasePruebaProfesoresPrueba.db')
        cursor = conexion.cursor()
        
        # Verificar si la tabla existe
        cursor.execute("SELECT * FROM materiaprofe WHERE type='table' AND name='materiaprofe';")
        if cursor.fetchone() is None:
            st.error("La tabla 'materiaprofe' no existe en la base de datos.")
        else:
            st.success("La tabla 'materiaprofe' fue detectada.")

            # Consultar los nombres de las columnas
            cursor.execute("PRAGMA table_info(materiaprofe);")
            columnas = cursor.fetchall()
            st.write("Columnas en la tabla 'materiaprofe':")
            for columna in columnas:
                st.write(columna[1])  # columna[1] tiene el nombre de la columna
                 conexion.close()


        
if seleccion_menu == "Asistencias":
        st.title("Asistencias")
if seleccion_menu == "Generar Reportes":
        st.title("Generar Reportes")
        
pr = st.sidebar.button("Generar Reportes")
if pr==True:
        st.write("xd")
        
