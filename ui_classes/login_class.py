from ui_files.login_code import Ui_Dialog_Login
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
from datetime import date, datetime


# ADMIN_USER = "admin"
# ADMIN_PASSWORD = "admin"

class DialogLogin(qtw.QDialog, Ui_Dialog_Login):
    send_username = qtc.pyqtSignal(str)

    def __init__(self,menuWindow,dialogRecover, *args, **kwargs):
        super(DialogLogin, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.menuWindow = menuWindow
        # self.dialogNewUser = dialogNewUser
        self.dialogRecover = dialogRecover
        self.setWindowIcon(qtg.QIcon("logo256png.png"))

        self.pushButton_Login.clicked.connect(self.login)
        self.pushButton_cancel_login.clicked.connect(self.close_popup)
        self.toolButton_new_user.clicked.connect(self.new_user)
        self.toolButton_recover_password.clicked.connect(self.recover)

        conn = sqlite3.connect("users.db")
        c = conn.cursor()
        all_users_list = {
            user_name[0] for user_name in c.execute("SELECT user_name FROM users")
        }
        conn.close()
        for each in all_users_list:
            self.comboBox_login_users.addItem(each)
            
    def set_dialog_new_user(self, dialog_new_user):
        self.dialogNewUser = dialog_new_user

    def login(self):
        conn = sqlite3.connect("users.db")
        c = conn.cursor()

        self.user = self.comboBox_login_users.currentText()
        self.password = self.lineEdit_password.text()

        if self.user == ADMIN_USER:
            if self.password == ADMIN_PASSWORD:
                self.send_username.emit(
                    self.user
                )  # ERROR when creating new user, dows not emits correctly
                # from publicaciones_data_input import menuWindow
                self.menuWindow.show()
                # publicationsWindow.show()
                self.close()
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
        conn.close()

        if check_password_hash(retrieved_password[0], self.password):
            self.send_username.emit(self.user)
            # from publicaciones_data_input import menuWindow
            self.menuWindow.show()
            self.close()
        else:
            qtw.QMessageBox.information(self, "Error", "Contraseña incorrecta")
            # self.comboBox_login_users.setCurrentText(str(self.user))
            return

    def new_user(self):
        self.dialogNewUser.show()

    def recover(self):
        self.dialogRecover.show()

    def close_popup(self):
        self.close()