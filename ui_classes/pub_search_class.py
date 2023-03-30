from ui_files.pub_search_code import Ui_MainWindow_pub_search
from publicaciones_data_input import tipos_publicaciones, revistas, categorias, areas_salud, proy_status
from publicaciones_data_input import EXPORT_FILE_NAME

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from PyQt5.QtWidgets import QApplication as qta
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt, QAbstractTableModel

import sqlite3
import urllib.request
from werkzeug.security import generate_password_hash, check_password_hash
import pandas
from datetime import date, datetime

# EXPORT_FILE_NAME = "data.xlsx"

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


class pandasModel(QAbstractTableModel):
    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parnet=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):  # type: ignore
        if index.isValid():
            if role == Qt.DisplayRole:  # type: ignore
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:  # type: ignore
            return self._data.columns[col]
        return None

class PubSearch(qtw.QMainWindow, Ui_MainWindow_pub_search):
    def __init__(self, *args, **kwargs):
        super(PubSearch, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.setWindowIcon(qtg.QIcon("logo256png.png"))

        self.dateEdit_year.setDateTime(qtc.QDateTime.currentDateTime())
        self.lineEdit_keywords.setPlaceholderText("Separadas por coma: virus, ecuador")
        self.lineEdit_author_search.setPlaceholderText(
            "Separados por coma: Andres, Ximena"
        )

        self.pushButton_search.clicked.connect(self.search)
        self.pushButton_export.clicked.connect(self.export_data)

        for each in sorted(tipos_publicaciones):
            self.comboBox_type_search.addItem(each)
        for each in sorted(revistas):
            self.comboBox_journal_search.addItem(each)
        for each in sorted(categorias):
            self.comboBox_category_search.addItem(each)
        for each in sorted(areas_salud):
            self.comboBox_area_search.addItem(each)
        for each in sorted(proy_status):
            self.comboBox_pub_state_search.addItem(each)

    def export_data(self):
        folderpath = qtw.QFileDialog.getExistingDirectory(self, "Select Folder")
        print(folderpath)
        try:
            self.export_df.to_excel(f"{folderpath}/{EXPORT_FILE_NAME}", index=False)
        except AttributeError:
            pass

    def search(self):
        publications_df = pandas.read_excel(
            "INSPI_CZ9_GIDI_Pbl_Cnt_KL_2021_2022.xlsx", sheet_name="Pbl_2022", header=1
        )

        if self.checkBox_keywords.isChecked():
            keywords_list = (
                (str(self.lineEdit_keywords.text())).lower().replace(" ", "").split(",")
            )
            # print(keywords_list)
        else:
            keywords_list = []

        if self.checkBox_year.isChecked():
            pub_year = self.dateEdit_year.date().toPyDate()
            pub_date = date(pub_year.year, 1, 1)
            publications_df = publications_df.query(
                "`Fecha de Publicación (mm/dd/aaaa)` >= @pub_date"
            )

        if self.checkBox_type.isChecked():
            type_list = [str(self.comboBox_type_search.currentText())]
        else:
            type_list = []

        if self.checkBox_journal.isChecked():
            journal_list = [str(self.comboBox_journal_search.currentText()).lower()]
        else:
            journal_list = []

        if self.checkBox_category.isChecked():
            category_list = [str(self.comboBox_category_search.currentText())]
        else:
            category_list = []

        if self.checkBox_area.isChecked():
            area_list = [str(self.comboBox_area_search.currentText())]
        else:
            area_list = []

        if self.checkBox_author.isChecked():
            author_list = (
                (str(self.lineEdit_author_search.text()))
                .lower()
                .replace(" ", "")
                .split(",")
            )
        else:
            author_list = []

        if self.checkBox_pub_state.isChecked():
            pub_state_list = [str(self.comboBox_pub_state_search.currentText())]
        else:
            pub_state_list = []
        ###################
        filtered_df = publications_df.copy()
        if keywords_list:
            filtered_df = filtered_df[
                filtered_df["Título"].str.lower().str.contains("|".join(keywords_list))
            ]
        if type_list:
            filtered_df = filtered_df[
                filtered_df["TIPO DE PUBLICACIÓN"].str.strip().isin(type_list)
            ]
        if journal_list:
            filtered_df = filtered_df[
                filtered_df["Revista"].str.lower().str.strip().isin(journal_list)
            ]
        if category_list:
            filtered_df = filtered_df[
                filtered_df.iloc[:, 4].str.strip().isin(category_list)
            ]  # error on categoria with tilde
        if area_list:
            filtered_df = filtered_df[
                filtered_df["Área de salud en la que esta enfocada la publicación"]
                .str.strip()
                .isin(area_list)
            ]
        if author_list:
            filtered_df = filtered_df[
                filtered_df["Nombres del autor (INSPI)"]
                .str.lower()
                .str.contains("|".join(author_list))
            ]
        if pub_state_list:
            filtered_df = filtered_df[
                filtered_df["Estado"].str.strip().isin(pub_state_list)
            ]
        self.export_df = filtered_df.copy()
        model = pandasModel(filtered_df)
        self.tableView.setModel(model)
