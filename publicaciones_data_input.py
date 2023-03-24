from activities_input_code import Ui_MainWindow
from add_author_code import Ui_Dialog_add_author

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from PyQt5.QtWidgets import QApplication as qta
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt

import sys
from datetime import date, datetime

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
    "Congreso Internacional de Ordenamiento Territorial y Tecnologías de la Información Geográfica",
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


class WindowUi(qtw.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(WindowUi, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.setWindowIcon(qtg.QIcon("logo256png.png"))
        addAuthor.send_authors.connect(self.get_author)

        self.dateEdit_aceptacion.setDateTime(qtc.QDateTime.currentDateTime())
        self.dateEdit_envio.setDateTime(qtc.QDateTime.currentDateTime())
        self.dateEdit_publicacion.setDateTime(qtc.QDateTime.currentDateTime())

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
        for each in sorted(databases):
            self.comboBox_databases.addItem(each)
        for each in sorted(direcciones):
            self.comboBox_direccion.addItem(each)

        self.pushButton_agregar_autor.clicked.connect(self.show_add_author)

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
        
    def get_author(self, author_name):
        if str(self.textEdit_autores.toPlainText()) != "":
            authors_str = str(self.textEdit_autores.toPlainText()) + "\n" +str(author_name)
            self.textEdit_autores.setPlainText(authors_str)
        else:
            authors_str = str(author_name)
            self.textEdit_autores.setPlainText(authors_str)


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
        self.full_name = (
            str(self.lineEdit_nombres.text())
            + " "
            + str(self.lineEdit_apellidos.text())
        )
        if self.checkBox_otro.isChecked():
            self.genero = self.lineEdit_genero.text()
        
        self.send_authors.emit(str(self.full_name))
        print(self.full_name, self.genero)
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


if __name__ == "__main__":
    import sys

    app = qtw.QApplication(sys.argv)
    addAuthor = AddAuthor()
    windowUi = WindowUi()
    # addAuthor.show()
    windowUi.show()

    sys.exit(app.exec_())
