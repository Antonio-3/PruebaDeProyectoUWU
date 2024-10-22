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
    try:
        conexion = sqlite3.connect('ProfesoresPrueba.db')
        cursor = conexion.cursor()

        # Verificar las tablas existentes en la base de datos
        cursor.execute('''SELECT name FROM sqlite_master WHERE type='table';''')
        tablas = cursor.fetchall()

        st.write("Tablas en la base de datos:", tablas)

        # Verificar si la tabla 'materiaprofe' existe
        if not any(tabla[0] == 'materiaprofe' for tabla in tablas):
            st.write("La tabla 'materiaprofe' no existe.")
        else:
            # Ejecutar consulta para seleccionar todas las materias
            cursor.execute('''SELECT * FROM materiaprofe''')

            # Recuperar todos los registros
            materiaprofe = cursor.fetchall()

            # Mostrar los registros en formato tabla
            if materiaprofe:
                st.table(materiaprofe)
            else:
                st.write("No se encontraron registros en la tabla.")
    
    except sqlite3.Error as e:
        st.write(f"Error al conectar o consultar la base de datos: {e}")
    
    finally:
        if conexion:
            conexion.close()


        
if seleccion_menu == "Asistencias":
        st.title("Asistencias")
if seleccion_menu == "Generar Reportes":
        st.title("Generar Reportes")
        
pr = st.sidebar.button("Generar Reportes")
if pr==True:
        st.write("xd")
        
