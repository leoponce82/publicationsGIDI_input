from ui_files.recover_password_code import Ui_Dialog_recover_password
from gidi_data_input import ADMIN_USER, ADMIN_PASSWORD

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
# ADMIN_USER = "admin"
# ADMIN_PASSWORD = "admin"

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
        self.close()

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
        self.close()