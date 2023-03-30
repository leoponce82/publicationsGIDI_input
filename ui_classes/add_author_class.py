from ui_files.add_author_code import Ui_Dialog_add_author
from gidi_data_input import authors, authors_gender

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from PyQt5.QtWidgets import QApplication as qta
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt, QAbstractTableModel

# authors = []
# authors_gender = []


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

        self.authors = []
        self.authors_gender = []

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
        self.authors.append(self.full_name)
        self.authors_gender.append(self.genero)
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
