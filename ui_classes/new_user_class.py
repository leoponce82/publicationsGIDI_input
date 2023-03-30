from ui_files.new_user_code import Ui_Dialog_new_user
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

class DialogNewUser(qtw.QDialog, Ui_Dialog_new_user):
    def __init__(self,dialogLogin,dialogRecover, *args, **kwargs):
        super(DialogNewUser, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.dialogLogin = dialogLogin
        self.dialogRecover = dialogRecover
        self.setWindowIcon(qtg.QIcon("logo256png.png"))

        self.pushButton_Ok_newuser.clicked.connect(self.new_user)
        self.pushButton_cancel_newuser.clicked.connect(self.close_popup)

    def close_popup(self):
        self.close()

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
        self.dialogLogin.comboBox_login_users.clear()
        self.dialogRecover.comboBox_recover_users.clear()
        conn = sqlite3.connect("users.db")
        c = conn.cursor()
        all_users_list = {
            user_name[0] for user_name in c.execute("SELECT user_name FROM users")
        }
        conn.close()
        for each in all_users_list:
            self.dialogLogin.comboBox_login_users.addItem(each)
            self.dialogRecover.comboBox_recover_users.addItem(each)
        self.dialogLogin.show()
        self.close()
