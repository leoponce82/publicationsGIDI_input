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

EXPORT_FILE_NAME = "data.xlsx"
ADMIN_USER = "admin"
ADMIN_PASSWORD = "admin"
path = "./users.db"
check_file = os.path.exists(path)

if check_file is False:
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute(
        """CREATE TABLE IF NOT EXISTS users (
            user_name text PRIMARY KEY,
            email text,
            user_password text
            )"""
    )
    admin_password_complete = generate_password_hash(ADMIN_PASSWORD, method="sha256")
    c.execute(
        "INSERT INTO users VALUES (:user, :email, :user_password)",
        {
            "user": ADMIN_USER,
            "email": None,
            "user_password": str(admin_password_complete),
        },
    )
    conn.commit()
    conn.close()

authors = []
authors_gender = []

tipos_publicaciones = {
    "Publicación científica periódica",
    "Capítulos de libros científicos",
    "Memorias de Eventos Científicos/Proceedings",
}

revistas = {
    "Nature Biomedical Engineering",
    "IEEE",
    "Insects",
    "Springer Nature",
    "INSPILIP",
    "PLOS ONE",
    "Virus evolution",
    "virological.org",
    "Parasites & Vectors",
    "Journal of Virological Methods",
    "PLOS Neglected Tropical Disease",
    "Mex Cienc Perú",
    "Infection and Drug Resistance",
    "BMC Public Health",
    "Royal Society Open Science",
    "Journal of Arthropod Borne Disease",
    "BMC Public Health",
    "Vector-Borne and Zoonotic Diseases",
    "Journal of the American Mosquito Control Association",
    "Agrociencia",
    "The Journal of the Royal Society Interface",
    "Journal of Helminthology",
    "Journal of Environmental and Public Health",
    "BMJ OPEN",
    "Journal of Medical Entomology",
    "The International Journal of Applied Research in Veterinary Medicine",
    "Acta Tropica",
    "Photochemical & Photobiological Sciences",
    "Frontiers in microbiology",
    "Water Resources Management",
    "Journal of Vector Ecology",
    "Entomotropica",
    "Boletín de Malariología y Salud Ambiental",
}

categorias = {
    "Bioquímica, Genética y Biología Molecular",
    "Ciencias de la computación",
    "Ciencia de los insectos",
    "Parasitología y Biología",
    "Sistemática de insectosm Filogenia y Evolucion",
    "Virología",
    "Genómica",
    "Ecología",
    "Inmunologia y Microbiología",
    "Enfermedades infecciosas",
    "Salud Pública",
    "Agricultura",
    "Zoología",
    "Veterinaria",
    "Medicina",
    "Vectores artropodos de arbovirus",
    "Parasitologiía",
    "Genética",
    "Zoonosis",
    "Física",
    "Tecnologías de la Información" "Ciencias del agua",
    "Multidisciplinaria",
}

paises = {
    "Afganistán",
    "Albania",
    "Alemania",
    "Andorra",
    "Angola",
    "Antigua y Barbuda",
    "Arabia Saudita",
    "Argelia",
    "Argentina",
    "Armenia",
    "Australia",
    "Austria",
    "Azerbaiyán",
    "Bahamas",
    "Bahréin",
    "Bangladés",
    "Barbados",
    "Bielorrusia",
    "Bélgica",
    "Belice",
    "Benín",
    "Bután",
    "Bolivia",
    "Bosnia-Herzegovina",
    "Botsuana",
    "Brasil",
    "Brunéi",
    "Bulgaria",
    "Burkina Faso",
    "Burundi",
    "Cabo Verde",
    "Camboya",
    "Camerún",
    "Canadá",
    "Chad",
    "República Checa",
    "Chequia",
    "Chile",
    "China",
    "Chipre",
    "Colombia",
    "Comoras",
    "Congo",
    "Corea del Norte",
    "Corea del Sur",
    "Costa Rica",
    "Costa de Marfil",
    "Croacia",
    "Cuba",
    "Dinamarca",
    "Yibuti",
    "Dominica",
    "Ecuador",
    "Egipto",
    "El Salvador",
    "Emiratos Árabes Unidos",
    "Eritrea",
    "Eslovaquia",
    "Eslovenia",
    "España",
    "Estados Unidos",
    "Estonia",
    "Etiopía",
    "Fiyi",
    "Filipinas",
    "Finlandia",
    "Francia",
    "Gabón",
    "Gambia",
    "Georgia",
    "Ghana",
    "Granada",
    "Grecia",
    "Guatemala",
    "Guinea",
    "Guinea-Bissau",
    "Guinea Ecuatorial",
    "Guyana",
    "Haití",
    "Honduras",
    "Hungría",
    "India",
    "Indonesia",
    "Irán",
    "Iraq",
    "Irlanda",
    "Islandia",
    "Israel",
    "Italia",
    "Jamaica",
    "Japón",
    "Jordania",
    "Kazajistán",
    "Kenia",
    "Kirguistán",
    "Kiribati",
    "Kuwait",
    "Laos",
    "Lesoto",
    "Letonia",
    "Líbano",
    "Liberia",
    "Libia",
    "Liechtenstein",
    "Lituania",
    "Luxemburgo",
    "Macedonia",
    "Madagascar",
    "Malasia",
    "Malaui",
    "Maldivas",
    "Mali / Malí",
    "Malta",
    "Marruecos",
    "Islas Marshall",
    "Mauricio",
    "Mauritania",
    "México",
    "Micronesia",
    "Moldavia",
    "Mónaco",
    "Mongolia",
    "Montenegro",
    "Mozambique",
    "Birmania",
    "Namibia",
    "Nauru",
    "Nepal",
    "Nicaragua",
    "Níger",
    "Nigeria",
    "Noruega",
    "Nueva Zelanda",
    "Omán",
    "Países Bajos",
    "Pakistán",
    "Palaos",
    "Panamá",
    "Papúa Nueva Guinea",
    "Paraguay",
    "Perú",
    "Polonia",
    "Portugal",
    "Qatar",
    "Reino Unido",
    "República Centroafricana",
    "República Dominicana",
    "Rumanía / Rumania",
    "Rusia",
    "Ruanda",
    "San Cristóbal y Nieves",
    "Islas Salomón",
    "Samoa",
    "San Marino",
    "Santa Lucía",
    "Ciudad del Vaticano",
    "Santo Tomé y Príncipe",
    "San Vicente y las Granadinas",
    "Senegal",
    "Serbia",
    "Seychelles",
    "Sierra Leona",
    "Singapur",
    "Siria",
    "Somalia",
    "Sri Lanka",
    "Sudáfrica",
    "Sudán",
    "Sudán del Sur",
    "Suecia",
    "Suiza",
    "Surinam",
    "Suazilandia",
    "Tailandia",
    "Tanzania",
    "Tayikistán",
    "Timor Oriental",
    "Togo",
    "Tonga",
    "Trinidad y Tobago",
    "Túnez",
    "Turkmenistán",
    "Turquía",
    "Tuvalu",
    "Ucrania",
    "Uganda",
    "Uruguay",
    "Uzbekistán",
    "Vanuatu",
    "Venezuela",
    "Vietnam",
    "Yemen",
    "Zambia",
    "Zimbabue",
}

databases = {
    "Academic Search Complete",
    "AccessScience",
    "ACS Publications",
    "AGORA",
    "BioMed Central",
    "BIOSIS Citation Index",
    "BIOSIS Previews",
    "CAB Abstracts",
    "Cambridge Core",
    "Chemical Abstracts Service (CAS)",
    "CINAHL Plus with Full Text",
    "Cochrane Library",
    "Current Contents Connect",
    "Directory of Open Access Journals (DOAJ)",
    "EBSCOhost",
    "Embase",
    "Entrez (NCBI)",
    "FSTA - Food Science and Technology Abstracts",
    "Google Scholar",
    "IEEE Xplore Digital Library",
    "InCites (Clarivate Analytics)",
    "JSTOR",
    "LWW Total Access Collection",
    "MathSciNet",
    "MEDLINE",
    "Nature Research Journals",
    "Ovid MEDLINE",
    "PLOS One",
    "ProQuest",
    "PubMed",
    "ResearchGate",
    "ScienceDirect",
    "SciFinder (CAS)",
    "Scimago Journal Rank",
    "Scopus",
    "SpringerLink",
    "Taylor & Francis Online",
    "Web of Science",
    "Wiley Online Library",
    "Zoological Record",
}

areas_salud = {
    "anatomía",
    "bacteriología",
    "biología celular",
    "biología molecular",
    "biotecnología",
    "bioquímica",
    "citoquímica",
    "ecología",
    "embriología",
    "epidemiología",
    "farmacología",
    "fisiología",
    "genética",
    "histología",
    "inmunología",
    "microbiología",
    "neurociencia",
    "nutrición",
    "oncología",
    "patología",
    "proteómica",
    "psicología de la salud",
    "psiquiatría",
    "salud ambiental",
    "salud pública",
    "terapia celular",
    "terapia génica",
    "toxicología",
    "virología",
}

direcciones = {"GIDI CZ9"}

proy_status = {"Publicado", "Submitido", "Aceptado"}


if __name__ == "__main__":
    from ui_classes.pub_input_class import PublicationsWindow
    from ui_classes.add_author_class import AddAuthor
    from ui_classes.add_database_class import AddDatabase
    from ui_classes.login_class import DialogLogin
    from ui_classes.new_user_class import DialogNewUser
    from ui_classes.recover_password_class import DialogRecoverPassword
    from ui_classes.pub_search_class import PubSearch
    from ui_classes.menu_class import MenuWindow
    import sys

    app = qtw.QApplication(sys.argv)

    dialogRecover = DialogRecoverPassword()
    addAuthor = AddAuthor()
    addDatabase = AddDatabase()
    pubSearch = PubSearch()
    menuWindow = MenuWindow()
    dialogLogin = DialogLogin(menuWindow, dialogRecover)
    dialogNewUser = DialogNewUser(dialogLogin, dialogRecover)
    dialogLogin.set_dialog_new_user(dialogNewUser)
    dialogLogin.send_username.connect(menuWindow.get_username)
    publicationsWindow = PublicationsWindow(
        menuWindow, addAuthor, addDatabase, dialogLogin, pubSearch
    )
    menuWindow.set_publications_window(publicationsWindow)
    dialogLogin.show()

    sys.exit(app.exec_())
