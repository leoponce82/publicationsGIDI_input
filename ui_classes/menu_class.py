from ui_files.menu_code import Ui_MainWindow_menu

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from PyQt5.QtWidgets import QApplication as qta
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt, QAbstractTableModel

class MenuWindow(qtw.QMainWindow, Ui_MainWindow_menu):
    menu_send_username = qtc.pyqtSignal(str)

    def __init__(self, *args, **kwargs):
        super(MenuWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.setWindowIcon(qtg.QIcon("logo256png.png"))
        # self.show()
        

        self.pushButton_publications.clicked.connect(self.publications_window)
        
    def set_publications_window(self, publicationsWindow):
        self.publicationsWindow = publicationsWindow

    def publications_window(self):
        self.menu_send_username.emit(self.current_user)
        self.publicationsWindow.show()
        self.close()

    def get_username(self, username):
        self.current_user = username
        self.label_current_user.setText(str(self.current_user))