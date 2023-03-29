from ui_files.activities_input_code import Ui_MainWindow
# from ui_classes.pub_input_class import PublicationsWindow

from ui_files.add_author_code import Ui_Dialog_add_author
# from ui_classes.add_author_class import AddAuthor

from ui_files.add_databases_code import Ui_Dialog_add_databases
# from ui_classes.add_database_class import AddDatabase

from ui_files.login_code import Ui_Dialog_Login
# from ui_classes.login_class import DialogLogin

from ui_files.new_user_code import Ui_Dialog_new_user
# from ui_classes.new_user_class import DialogNewUser

from ui_files.recover_password_code import Ui_Dialog_recover_password
# from ui_classes.recover_password_class import DialogRecoverPassword

from ui_files.pub_search_code import Ui_MainWindow_pub_search
# from ui_classes.pub_search_class import PubSearch

from ui_files.menu_code import Ui_MainWindow_menu
# from ui_classes.menu_class import MenuWindow

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


class PublicationsWindow(qtw.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(PublicationsWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.setWindowIcon(qtg.QIcon("logo256png.png"))
        addAuthor.send_authors.connect(self.get_author)
        addDatabase.send_databases.connect(self.get_databases)
        dialogLogin.send_username.connect(self.get_username)

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
        dialogLogin.show()
    
    def search_data(self):
        pubSearch.show()

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
        addAuthor.show()
        addAuthor.lineEdit_genero.clear()
        addAuthor.lineEdit_apellidos.clear()
        addAuthor.lineEdit_nombres.clear()
        addAuthor.checkBox_masc.setChecked(False)
        addAuthor.checkBox_fem.setChecked(False)
        addAuthor.checkBox_otro.setChecked(False)
        addAuthor.lineEdit_genero.setReadOnly(True)

    def show_add_database(self):
        addDatabase.show()

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


class AddAuthor(qtw.QDialog, Ui_Dialog_add_author):
    send_authors = qtc.pyqtSignal(str)

    def __init__(self, *args, **kwargs):
        super(AddAuthor, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.setWindowIcon(qtg.QIcon("logo256png.png"))
        self.lineEdit_genero.clear()
        self.lineEdit_genero.setReadOnly(True)
        self.lineEdit_apellidos.clear()
        self.lineEdit_nombres.clear()

        self.pushButton_guardar_autor.clicked.connect(self.add_author)
        self.checkBox_fem.stateChanged.connect(self.femStateChange)
        self.checkBox_masc.stateChanged.connect(self.mascStateChange)
        self.checkBox_otro.stateChanged.connect(self.otherStateChange)

    def add_author(self):
        if (
            str(self.lineEdit_nombres.text()) == ""
            or str(self.lineEdit_apellidos.text()) == ""
        ):
            qtw.QMessageBox.information(self, "Error", "Ingrese nombres y apellidos")
            return
        self.full_name = (
            str(self.lineEdit_nombres.text())
            + " "
            + str(self.lineEdit_apellidos.text())
        )
        if self.checkBox_otro.isChecked():
            self.genero = self.lineEdit_genero.text()

        self.send_authors.emit(str(self.full_name))
        print(self.full_name, self.genero)
        authors.append(self.full_name)
        authors_gender.append(self.genero)
        # print(self.send_authors)
        self.close()

    def femStateChange(self):
        if self.checkBox_fem.isChecked():
            self.checkBox_masc.setChecked(False)
            self.checkBox_otro.setChecked(False)
            self.lineEdit_genero.setReadOnly(True)
            self.lineEdit_genero.clear()
            self.genero = "Femenino"

    def mascStateChange(self):
        if self.checkBox_masc.isChecked():
            self.checkBox_fem.setChecked(False)
            self.checkBox_otro.setChecked(False)
            self.lineEdit_genero.setReadOnly(True)
            self.lineEdit_genero.clear()
            self.genero = "Masculino"

    def otherStateChange(self):
        if self.checkBox_otro.isChecked():
            self.checkBox_masc.setChecked(False)
            self.checkBox_fem.setChecked(False)
            self.lineEdit_genero.setReadOnly(False)


class AddDatabase(qtw.QDialog, Ui_Dialog_add_databases):
    send_databases = qtc.pyqtSignal(str)

    def __init__(self, *args, **kwargs):
        super(AddDatabase, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.setWindowIcon(qtg.QIcon("logo256png.png"))
        for each in sorted(databases):
            self.comboBox_databases.addItem(each)
        self.pushButton_guardar_base_indexadas.clicked.connect(self.add_database)

    def add_database(self):
        self.send_databases.emit(str(self.comboBox_databases.currentText()))
        self.close()


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
        folderpath = qtw.QFileDialog.getExistingDirectory(self, 'Select Folder')
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


class DialogLogin(qtw.QDialog, Ui_Dialog_Login):
    send_username = qtc.pyqtSignal(str)

    def __init__(self, *args, **kwargs):
        super(DialogLogin, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.setWindowIcon(qtg.QIcon("logo256png.png"))

        self.pushButton_Login.clicked.connect(self.login)
        self.pushButton_cancel_login.clicked.connect(self.close_popup)
        self.toolButton_new_user.clicked.connect(self.new_user)
        self.toolButton_recover_password.clicked.connect(self.recover)

        conn = sqlite3.connect("users.db")
        c = conn.cursor()
        all_users_list = [
            user_name[0] for user_name in c.execute("SELECT user_name FROM users")
        ]
        conn.close()
        for each in all_users_list:
            self.comboBox_login_users.addItem(each)

    def login(self):
        conn = sqlite3.connect("users.db")
        c = conn.cursor()

        self.user = self.comboBox_login_users.currentText()
        self.password = self.lineEdit_password.text()

        if self.user == ADMIN_USER:
            if self.password == ADMIN_PASSWORD:
                self.send_username.emit(str(self.user))
                menuWindow.show()
                dialogLogin.close()
                return
            else:
                qtw.QMessageBox.information(self, "Error", "Contraseña incorrecta")
                return

        if (
            c.execute(
                "SELECT EXISTS (SELECT 1 FROM users WHERE user_name=?)", (self.user,)
            ).fetchone()[0]
            == 0
        ):
            qtw.QMessageBox.information(
                self, "Error", f"El usuario {self.user} no existe"
            )
            return

        c.execute(
            "SELECT user_password FROM users WHERE user_name = :username",
            {"username": self.user},
        )
        retrieved_password = c.fetchone()
        # print(retrieved_password[0])

        if check_password_hash(retrieved_password[0], self.password):
            self.send_username.emit(str(self.user))
            menuWindow.show()
            conn.close()
            dialogLogin.close()
        else:
            qtw.QMessageBox.information(self, "Error", "Contraseña incorrecta")
            # self.comboBox_login_users.setCurrentText(str(self.user))
            return

    def new_user(self):
        dialogNewUser.show()

    def recover(self):
        dialogRecover.show()

    def close_popup(self):
        dialogLogin.close()


class DialogNewUser(qtw.QDialog, Ui_Dialog_new_user):
    def __init__(self, *args, **kwargs):
        super(DialogNewUser, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.setWindowIcon(qtg.QIcon("logo256png.png"))

        self.pushButton_Ok_newuser.clicked.connect(self.new_user)
        self.pushButton_cancel_newuser.clicked.connect(self.close_popup)

    def close_popup(self):
        dialogNewUser.close()

    def new_user(self):

        conn = sqlite3.connect("users.db")
        c = conn.cursor()

        new_username = self.lineEdit_new_username.text()
        new_password = self.lineEdit_new_password.text()
        new_password_2 = self.lineEdit_new_password_2.text()
        new_email = self.lineEdit_new_email.text()
        new_email_2 = self.lineEdit_new_email_2.text()

        if not ("@" in new_email) or not (".com" in new_email):
            qtw.QMessageBox.information(self, "Error", "Correo no válido")
            return

        if new_password != new_password_2:
            qtw.QMessageBox.information(self, "Error", "La contraseña no coincide")
            return
        if new_email != new_email_2:
            qtw.QMessageBox.information(self, "Error", "El correo no coincide")
            return
        if new_username == ADMIN_USER:
            qtw.QMessageBox.information(
                self, "Error", f"{ADMIN_USER} no se puede crear ni modificar"
            )
            return
        if c.execute(
            "SELECT 1 FROM users WHERE user_name = :new_username",
            {"new_username": new_username},
        ).fetchone():
            qtw.QMessageBox.information(
                self, "Error", f"El usuario {new_username} ya existe"
            )
            return

        password_complete = generate_password_hash(new_password_2, method="sha256")

        c.execute(
            "INSERT INTO users VALUES (:user, :email, :user_password)",
            {
                "user": str(new_username),
                "email": str(new_email),
                "user_password": str(password_complete),
            },
        )
        conn.commit()
        conn.close()

        qtw.QMessageBox.information(self, "Exito", "El usuario se ha guardado")
        # dialogRecover.comboBox_recover_users.addItem(new_username)
        # # print(new_username)
        dialogRecover.__init__()
        dialogLogin.close()
        dialogLogin.__init__()
        dialogLogin.show()
        dialogNewUser.close()


class DialogRecoverPassword(qtw.QDialog, Ui_Dialog_recover_password):
    def __init__(self, *args, **kwargs):
        super(DialogRecoverPassword, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.setWindowIcon(qtg.QIcon("logo256png.png"))

        self.pushButton_Ok_recover.clicked.connect(self.recover)
        self.pushButton_cancel_recover.clicked.connect(self.close_popup)

        conn = sqlite3.connect("users.db")
        c = conn.cursor()
        all_users_list = [
            user_name[0] for user_name in c.execute("SELECT user_name FROM users")
        ]
        conn.close()
        for each in all_users_list:
            self.comboBox_recover_users.addItem(each)

    def close_popup(self):
        dialogRecover.close()

    def recover(self):
        username = self.comboBox_recover_users.currentText()
        new_password = self.lineEdit_new_password.text()
        new_password_2 = self.lineEdit_new_password_2.text()
        if new_password != new_password_2:
            qtw.QMessageBox.information(self, "Error", "La contraseña no coincide")
            return
        if username == ADMIN_USER:
            qtw.QMessageBox.information(
                self, "Error", f"{ADMIN_USER} no se puede crear ni modificar"
            )
            return

        conn = sqlite3.connect("users.db")
        c = conn.cursor()
        password_complete = generate_password_hash(
            self.lineEdit_new_password_2.text(), method="sha256"
        )
        c.execute(
            """UPDATE users SET user_password = :new_password WHERE user_name = :user""",
            {"new_password": password_complete, "user": username},
        )
        conn.commit()
        conn.close()
        qtw.QMessageBox.information(self, "Exito", "Se ha actualizado la contraseña")
        dialogRecover.close()


class MenuWindow(qtw.QMainWindow, Ui_MainWindow_menu):
    def __init__(self, *args, **kwargs):
        super(MenuWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.setWindowIcon(qtg.QIcon("logo256png.png"))
        # self.show()
        self.pushButton_publications.clicked.connect(self.publications_window)
    
    def publications_window(self):
        publicationsWindow.show()
        self.close()

if __name__ == "__main__":
    import sys

    app = qtw.QApplication(sys.argv)
    dialogLogin = DialogLogin()
    dialogNewUser = DialogNewUser()
    dialogRecover = DialogRecoverPassword()
    addAuthor = AddAuthor()
    addDatabase = AddDatabase()
    pubSearch = PubSearch()
    menuWindow = MenuWindow()
    publicationsWindow = PublicationsWindow()
    # addAuthor.show()
    dialogLogin.show()

    sys.exit(app.exec_())
