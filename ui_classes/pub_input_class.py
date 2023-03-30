from ui_files.activities_input_code import Ui_MainWindow
from publicaciones_data_input import tipos_publicaciones, revistas, categorias, paises, areas_salud, direcciones, authors_gender


from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from PyQt5.QtWidgets import QApplication as qta
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt, QAbstractTableModel

import sqlite3
import urllib.request
from werkzeug.security import generate_password_hash, check_password_hash

import sys
import os.path
from datetime import date, datetime
import pandas
from openpyxl import load_workbook

# authors = []
# authors_gender = []

# tipos_publicaciones = {
#     "Publicación científica periódica",
#     "Capítulos de libros científicos",
#     "Memorias de Eventos Científicos/Proceedings",
# }

# revistas = {
#     "Nature Biomedical Engineering",
#     "IEEE",
#     "Insects",
#     "Springer Nature",
#     "INSPILIP",
#     "PLOS ONE",
#     "Virus evolution",
#     "virological.org",
#     "Parasites & Vectors",
#     "Journal of Virological Methods",
#     "PLOS Neglected Tropical Disease",
#     "Mex Cienc Perú",
#     "Infection and Drug Resistance",
#     "BMC Public Health",
#     "Royal Society Open Science",
#     "Journal of Arthropod Borne Disease",
#     "BMC Public Health",
#     "Vector-Borne and Zoonotic Diseases",
#     "Journal of the American Mosquito Control Association",
#     "Agrociencia",
#     "The Journal of the Royal Society Interface",
#     "Journal of Helminthology",
#     "Journal of Environmental and Public Health",
#     "BMJ OPEN",
#     "Journal of Medical Entomology",
#     "The International Journal of Applied Research in Veterinary Medicine",
#     "Acta Tropica",
#     "Photochemical & Photobiological Sciences",
#     "Frontiers in microbiology",
#     "Water Resources Management",
#     "Journal of Vector Ecology",
#     "Entomotropica",
#     "Boletín de Malariología y Salud Ambiental",
# }

# categorias = {
#     "Bioquímica, Genética y Biología Molecular",
#     "Ciencias de la computación",
#     "Ciencia de los insectos",
#     "Parasitología y Biología",
#     "Sistemática de insectosm Filogenia y Evolucion",
#     "Virología",
#     "Genómica",
#     "Ecología",
#     "Inmunologia y Microbiología",
#     "Enfermedades infecciosas",
#     "Salud Pública",
#     "Agricultura",
#     "Zoología",
#     "Veterinaria",
#     "Medicina",
#     "Vectores artropodos de arbovirus",
#     "Parasitologiía",
#     "Genética",
#     "Zoonosis",
#     "Física",
#     "Tecnologías de la Información" "Ciencias del agua",
#     "Multidisciplinaria",
# }

# paises = {
#     "Afganistán",
#     "Albania",
#     "Alemania",
#     "Andorra",
#     "Angola",
#     "Antigua y Barbuda",
#     "Arabia Saudita",
#     "Argelia",
#     "Argentina",
#     "Armenia",
#     "Australia",
#     "Austria",
#     "Azerbaiyán",
#     "Bahamas",
#     "Bahréin",
#     "Bangladés",
#     "Barbados",
#     "Bielorrusia",
#     "Bélgica",
#     "Belice",
#     "Benín",
#     "Bután",
#     "Bolivia",
#     "Bosnia-Herzegovina",
#     "Botsuana",
#     "Brasil",
#     "Brunéi",
#     "Bulgaria",
#     "Burkina Faso",
#     "Burundi",
#     "Cabo Verde",
#     "Camboya",
#     "Camerún",
#     "Canadá",
#     "Chad",
#     "República Checa",
#     "Chequia",
#     "Chile",
#     "China",
#     "Chipre",
#     "Colombia",
#     "Comoras",
#     "Congo",
#     "Corea del Norte",
#     "Corea del Sur",
#     "Costa Rica",
#     "Costa de Marfil",
#     "Croacia",
#     "Cuba",
#     "Dinamarca",
#     "Yibuti",
#     "Dominica",
#     "Ecuador",
#     "Egipto",
#     "El Salvador",
#     "Emiratos Árabes Unidos",
#     "Eritrea",
#     "Eslovaquia",
#     "Eslovenia",
#     "España",
#     "Estados Unidos",
#     "Estonia",
#     "Etiopía",
#     "Fiyi",
#     "Filipinas",
#     "Finlandia",
#     "Francia",
#     "Gabón",
#     "Gambia",
#     "Georgia",
#     "Ghana",
#     "Granada",
#     "Grecia",
#     "Guatemala",
#     "Guinea",
#     "Guinea-Bissau",
#     "Guinea Ecuatorial",
#     "Guyana",
#     "Haití",
#     "Honduras",
#     "Hungría",
#     "India",
#     "Indonesia",
#     "Irán",
#     "Iraq",
#     "Irlanda",
#     "Islandia",
#     "Israel",
#     "Italia",
#     "Jamaica",
#     "Japón",
#     "Jordania",
#     "Kazajistán",
#     "Kenia",
#     "Kirguistán",
#     "Kiribati",
#     "Kuwait",
#     "Laos",
#     "Lesoto",
#     "Letonia",
#     "Líbano",
#     "Liberia",
#     "Libia",
#     "Liechtenstein",
#     "Lituania",
#     "Luxemburgo",
#     "Macedonia",
#     "Madagascar",
#     "Malasia",
#     "Malaui",
#     "Maldivas",
#     "Mali / Malí",
#     "Malta",
#     "Marruecos",
#     "Islas Marshall",
#     "Mauricio",
#     "Mauritania",
#     "México",
#     "Micronesia",
#     "Moldavia",
#     "Mónaco",
#     "Mongolia",
#     "Montenegro",
#     "Mozambique",
#     "Birmania",
#     "Namibia",
#     "Nauru",
#     "Nepal",
#     "Nicaragua",
#     "Níger",
#     "Nigeria",
#     "Noruega",
#     "Nueva Zelanda",
#     "Omán",
#     "Países Bajos",
#     "Pakistán",
#     "Palaos",
#     "Panamá",
#     "Papúa Nueva Guinea",
#     "Paraguay",
#     "Perú",
#     "Polonia",
#     "Portugal",
#     "Qatar",
#     "Reino Unido",
#     "República Centroafricana",
#     "República Dominicana",
#     "Rumanía / Rumania",
#     "Rusia",
#     "Ruanda",
#     "San Cristóbal y Nieves",
#     "Islas Salomón",
#     "Samoa",
#     "San Marino",
#     "Santa Lucía",
#     "Ciudad del Vaticano",
#     "Santo Tomé y Príncipe",
#     "San Vicente y las Granadinas",
#     "Senegal",
#     "Serbia",
#     "Seychelles",
#     "Sierra Leona",
#     "Singapur",
#     "Siria",
#     "Somalia",
#     "Sri Lanka",
#     "Sudáfrica",
#     "Sudán",
#     "Sudán del Sur",
#     "Suecia",
#     "Suiza",
#     "Surinam",
#     "Suazilandia",
#     "Tailandia",
#     "Tanzania",
#     "Tayikistán",
#     "Timor Oriental",
#     "Togo",
#     "Tonga",
#     "Trinidad y Tobago",
#     "Túnez",
#     "Turkmenistán",
#     "Turquía",
#     "Tuvalu",
#     "Ucrania",
#     "Uganda",
#     "Uruguay",
#     "Uzbekistán",
#     "Vanuatu",
#     "Venezuela",
#     "Vietnam",
#     "Yemen",
#     "Zambia",
#     "Zimbabue",
# }

# databases = {
#     "Academic Search Complete",
#     "AccessScience",
#     "ACS Publications",
#     "AGORA",
#     "BioMed Central",
#     "BIOSIS Citation Index",
#     "BIOSIS Previews",
#     "CAB Abstracts",
#     "Cambridge Core",
#     "Chemical Abstracts Service (CAS)",
#     "CINAHL Plus with Full Text",
#     "Cochrane Library",
#     "Current Contents Connect",
#     "Directory of Open Access Journals (DOAJ)",
#     "EBSCOhost",
#     "Embase",
#     "Entrez (NCBI)",
#     "FSTA - Food Science and Technology Abstracts",
#     "Google Scholar",
#     "IEEE Xplore Digital Library",
#     "InCites (Clarivate Analytics)",
#     "JSTOR",
#     "LWW Total Access Collection",
#     "MathSciNet",
#     "MEDLINE",
#     "Nature Research Journals",
#     "Ovid MEDLINE",
#     "PLOS One",
#     "ProQuest",
#     "PubMed",
#     "ResearchGate",
#     "ScienceDirect",
#     "SciFinder (CAS)",
#     "Scimago Journal Rank",
#     "Scopus",
#     "SpringerLink",
#     "Taylor & Francis Online",
#     "Web of Science",
#     "Wiley Online Library",
#     "Zoological Record",
# }

# areas_salud = {
#     "anatomía",
#     "bacteriología",
#     "biología celular",
#     "biología molecular",
#     "biotecnología",
#     "bioquímica",
#     "citoquímica",
#     "ecología",
#     "embriología",
#     "epidemiología",
#     "farmacología",
#     "fisiología",
#     "genética",
#     "histología",
#     "inmunología",
#     "microbiología",
#     "neurociencia",
#     "nutrición",
#     "oncología",
#     "patología",
#     "proteómica",
#     "psicología de la salud",
#     "psiquiatría",
#     "salud ambiental",
#     "salud pública",
#     "terapia celular",
#     "terapia génica",
#     "toxicología",
#     "virología",
# }

# direcciones = {"GIDI CZ9"}

# proy_status = {"Publicado", "Submitido", "Aceptado"}


class PublicationsWindow(qtw.QMainWindow, Ui_MainWindow):
    def __init__(self,menuWindow,addAuthor, addDatabase, dialogLogin, pubSearch, *args, **kwargs):
        super(PublicationsWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.menuWindow=menuWindow
        self.addAuthor=addAuthor
        self.addDatabase=addDatabase
        self.dialogLogin=dialogLogin
        self.pubSearch=pubSearch
        self.setWindowIcon(qtg.QIcon("logo256png.png"))
        addAuthor.send_authors.connect(self.get_author)
        addDatabase.send_databases.connect(self.get_databases)
        menuWindow.menu_send_username.connect(self.get_username)

        self.dateEdit_aceptacion.setDateTime(qtc.QDateTime.currentDateTime())
        self.dateEdit_envio.setDateTime(qtc.QDateTime.currentDateTime())
        self.dateEdit_publicacion.setDateTime(qtc.QDateTime.currentDateTime())

        self.checkBox_aceptado.stateChanged.connect(self.aceptadoStateChange)
        self.checkBox_submitido.stateChanged.connect(self.submitidoStateChange)
        self.checkBox_publicado.stateChanged.connect(self.publicadoStateChange)

        self.checkBox_ejecucion.stateChanged.connect(self.ejecucionStateChange)
        self.checkBox_finalizado.stateChanged.connect(self.finalizadoStateChange)

        for each in sorted(tipos_publicaciones):
            self.comboBox_tipo.addItem(each)
        for each in sorted(revistas):
            self.comboBox_revista.addItem(each)
        for each in sorted(categorias):
            self.comboBox_categoria.addItem(each)
        for each in sorted(paises):
            self.comboBox_pais.addItem(each)
        for each in sorted(areas_salud):
            self.comboBox_area_salud.addItem(each)
        for each in sorted(direcciones):
            self.comboBox_direccion.addItem(each)

        self.pub_date = None

        self.pushButton_agregar_autor.clicked.connect(self.show_add_author)
        self.pushButton_input.clicked.connect(self.input_data)
        self.pushButton_add_database.clicked.connect(self.show_add_database)
        self.toolButton_logout.clicked.connect(self.logout)
        self.toolButton_search_data.clicked.connect(self.search_data)

    def logout(self):
        self.close()
        self.dialogLogin.show()

    def search_data(self):
        self.pubSearch.show()

    def ejecucionStateChange(self):
        if self.checkBox_ejecucion.isChecked():
            self.checkBox_finalizado.setChecked(False)
            self.project_state = "Ejecucion"

    def finalizadoStateChange(self):
        if self.checkBox_finalizado.isChecked():
            self.checkBox_ejecucion.setChecked(False)
            self.project_state = "Finalizado"

    def aceptadoStateChange(self):
        if self.checkBox_aceptado.isChecked():
            self.checkBox_publicado.setChecked(False)
            self.checkBox_submitido.setChecked(False)
            self.pub_state = "Aceptado"
            self.pub_date = None

    def submitidoStateChange(self):
        if self.checkBox_submitido.isChecked():
            self.checkBox_aceptado.setChecked(False)
            self.checkBox_publicado.setChecked(False)
            self.pub_state = "Submitido"
            self.pub_date = None

    def publicadoStateChange(self):
        if self.checkBox_publicado.isChecked():
            self.checkBox_aceptado.setChecked(False)
            self.checkBox_submitido.setChecked(False)
            self.pub_state = "Publicado"
            self.pub_date = self.dateEdit_publicacion.date().toPyDate()

    def input_data(self):
        self.excel_data_df = pandas.read_excel(
            "INSPI_CZ9_GIDI_Pbl_Cnt_KL_2021_2022.xlsx", sheet_name="Pbl_2022", header=1
        )
        self.last_No = self.excel_data_df["No."].iloc[-1]
        # print(self.last_No)

        if (
            self.checkBox_finalizado.isChecked() is False
            and self.checkBox_ejecucion.isChecked() is False
        ):
            # print(self.checkBox_finalizado.isChecked())
            self.project_state = None
        if (
            self.checkBox_aceptado.isChecked() is False
            and self.checkBox_publicado.isChecked() is False
            and self.checkBox_submitido.isChecked() is False
        ):
            # print(self.checkBox_submitido.isChecked())
            self.pub_state = None

        gender_write = ""
        for each in authors_gender:
            gender_write = gender_write + each + "\n"

        to_append = [
            self.last_No + 1,
            self.textEdit_titulo.toPlainText(),
            self.comboBox_tipo.currentText(),
            self.comboBox_revista.currentText(),
            self.comboBox_categoria.currentText(),
            self.comboBox_pais.currentText(),
            self.pub_date,
            self.textEdit_databases.toPlainText(),
            self.comboBox_area_salud.currentText(),
            self.spinBox_indiceH.value(),
            self.textEdit_autores.toPlainText(),
            gender_write,
            self.lineEdit_doi.text(),
            self.lineEdit_issn.text(),
            self.textEdit_resumen.toPlainText(),
            self.dateEdit_envio.date().toPyDate(),
            self.dateEdit_aceptacion.date().toPyDate(),
            "Q"
            + str(((self.dateEdit_aceptacion.date().toPyDate().month) - 1) // 3 + 1),
            self.pub_state,
            self.textEdit_pagweb.toPlainText(),
            self.comboBox_direccion.currentText(),
            self.textEdit_proyecto.toPlainText(),
            self.project_state,
            self.textEdit_observaciones.toPlainText(),
        ]

        wb = load_workbook("INSPI_CZ9_GIDI_Pbl_Cnt_KL_2021_2022.xlsx")
        ws = wb["Pbl_2022"]
        ws.append(to_append)
        wb.save("INSPI_CZ9_GIDI_Pbl_Cnt_KL_2021_2022.xlsx")
        print("saved")
        qtw.QMessageBox.information(self, "Exito", "Datos ingresados correctamente")

    def show_add_author(self):
        # addAuthor.__init__()  # To clear all fields
        self.addAuthor.show()
        self.addAuthor.lineEdit_genero.clear()
        self.addAuthor.lineEdit_apellidos.clear()
        self.addAuthor.lineEdit_nombres.clear()
        self.addAuthor.checkBox_masc.setChecked(False)
        self.addAuthor.checkBox_fem.setChecked(False)
        self.addAuthor.checkBox_otro.setChecked(False)
        self.addAuthor.lineEdit_genero.setReadOnly(True)

    def show_add_database(self):
        self.addDatabase.show()

    def get_username(self, username):
        self.current_user = username
        self.label_current_user.setText(str(self.current_user))

    def get_author(self, author_name):
        if str(self.textEdit_autores.toPlainText()) != "":
            authors_str = (
                str(self.textEdit_autores.toPlainText()) + "\n" + str(author_name)
            )
            self.textEdit_autores.setPlainText(authors_str)
        else:
            authors_str = str(author_name)
            self.textEdit_autores.setPlainText(authors_str)

    def get_databases(self, database):
        if str(self.textEdit_databases.toPlainText()) != "":
            database_str = (
                str(self.textEdit_databases.toPlainText()) + "\n" + str(database)
            )
            self.textEdit_databases.setPlainText(database_str)
        else:
            database_str = str(database)
            self.textEdit_databases.setPlainText(database_str)