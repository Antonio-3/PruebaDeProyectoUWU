import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import sqlite3
from fpdf import FPDF

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
        seleccion_profeexd = st.selectbox('Selecciona un profesor:', df['Profesor'])
        cursor = conexion.cursor()
        conexion.close()

        pr = st.button("Generar reporte del profesor")
        if pr==True:

                st.write(pr)
                # Conectar a la base de datos
                conexion = sqlite3.connect('BasePrueba/ProfesoresPrueba.db')
                cursor = conexion.cursor()
                # Seleccionar todas las materias
                cursor.execute('''
                SELECT * FROM materiaprofe
                ''')
                # Recuperar todos los registros
                ala = cursor.fetchall()
                # Cerrar la conexión
                conexion.close()

                # Crear una instancia de FPDF
                pdf = FPDF()
                pdf.set_auto_page_break(auto=True, margin=15)
                # Agregar una página
                pdf.add_page()
                # Establecer el tipo de fuente (Arial, negrita, tamaño 16)
                pdf.set_font('Arial', 'B', 16)
                # Título del reporte
                pdf.cell(200, 10, 'Reporte de Materias', ln=True, align='C')
                # Espacio adicional
                pdf.ln(10)
                # Establecer el tipo de fuente para el contenido (Arial, tamaño 12)
                pdf.set_font('Arial', '', 12)
                # Encabezados de la tabla
                pdf.cell(20, 10, 'ID', 1)
                pdf.cell(80, 10, 'Profesor', 1)
                pdf.cell(60, 10, 'Materia', 1)
                pdf.cell(30, 10, 'Carrera', 1)
                pdf.cell(80, 10, 'Fecha', 1)
                pdf.cell(60, 10, 'Horario', 1)
                pdf.cell(30, 10, 'Asistencia', 1)
                pdf.ln()
                
                # Agregar los registros de materias al PDF
                for jaja in ala:
                        pdf.cell(20, 10, str(jaja[0]), 1)
                        pdf.cell(80, 10, jaja[1], 1)
                        pdf.cell(60, 10, jaja[2], 1)
                        pdf.cell(30, 10, jaja[3], 1)
                        pdf.cell(80, 10, str(jaja[4]), 1)
                        pdf.cell(60, 10, str(jaja[5]), 1)
                        pdf.cell(30, 10, str(jaja[6]), 1)
                        pdf.ln()
                        # Guardar el archivo PDF
                        pdf.output('XDxd.pdf')


                
        
