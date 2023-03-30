from ui_files.remove_authors_code import Ui_Dialog_remove_author
from gidi_data_input import authors, authors_gender

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from PyQt5.QtWidgets import QApplication as qta
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt, QAbstractTableModel


class RemoveAuthor(qtw.QDialog, Ui_Dialog_remove_author):
    send_authors = qtc.pyqtSignal()

    def __init__(self, *args, **kwargs):
        super(RemoveAuthor, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.setWindowIcon(qtg.QIcon("logo256png.png"))
        
        self.pushButton_remove_author.clicked.connect(self.delete_author)

    def delete_author(self):
        removed_author = self.comboBox_authors.currentText()
        try:
            index = authors.index(removed_author)
            authors.pop(index)
            authors_gender.pop(index)
            self.send_authors.emit()
            # print("add_author", self.full_name, self.genero)
            # print(self.send_authors)
            print(authors)
            self.close()
        except ValueError:
            return
