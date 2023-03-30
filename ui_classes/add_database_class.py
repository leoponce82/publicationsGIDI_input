from ui_files.add_databases_code import Ui_Dialog_add_databases
from gidi_data_input import databases, added_databases


from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from PyQt5.QtWidgets import QApplication as qta
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt, QAbstractTableModel

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


class AddDatabase(qtw.QDialog, Ui_Dialog_add_databases):
    send_databases = qtc.pyqtSignal()

    def __init__(self, *args, **kwargs):
        super(AddDatabase, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.setWindowIcon(qtg.QIcon("logo256png.png"))
        for each in sorted(databases):
            self.comboBox_databases.addItem(each)
        self.pushButton_guardar_base_indexadas.clicked.connect(self.add_database)
        self.pushButton_eliminar_base_indexadas.clicked.connect(self.delete_database)

    def add_database(self):
        added_databases.add(self.comboBox_databases.currentText())
        self.send_databases.emit()
        self.close()

    def delete_database(self):
        try:
            added_databases.remove(self.comboBox_databases.currentText())
            self.send_databases.emit()
            self.close()
        except KeyError:
            return
