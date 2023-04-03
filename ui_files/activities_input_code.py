# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'activities_input.ui'
#
# Created by: PyQt5 UI code generator 5.15.8
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1465, 822)
        MainWindow.setStyleSheet("QWidget {\n"
"  background-color: #fff;\n"
"}\n"
"QLabel {\n"
"  color: #464d55;\n"
"  font-weight: 600;\n"
"}\n"
"QLabel#heading {\n"
"  color: #0f1925;\n"
"  font-size: 18px;\n"
"  margin-bottom: 10px;\n"
"}\n"
"\n"
"QLabel#subheading {\n"
"  color: #0f1925;\n"
"  font-size: 12px;\n"
"  font-weight: normal;\n"
"  margin-bottom: 10px;\n"
"}\n"
"QLineEdit {\n"
"  border-radius: 8px;\n"
"  border: 1px solid #e0e4e7;\n"
"  padding: 5px 15px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"  border: 1px solid #d0e3ff;\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"  color: #767e89;\n"
"}\n"
"QPushButton {\n"
"  background-color: #0d6efd;\n"
"  color: #fff;\n"
"  font-weight: 600;\n"
"  border-radius: 8px;\n"
"  border: 1px solid #0d6efd;\n"
"  padding: 10px 10px;\n"
"  margin-top: 1px;\n"
"  outline: 0px;\n"
"}\n"
"QPushButton:hover,\n"
"QPushButton:focus {\n"
"  background-color: #0b5ed7;\n"
"  border: 1px solid #9ac3fe;\n"
"}\n"
"QMenu {\n"
"background-color: #fff;\n"
"border: 1px solid black;\n"
"margin: 2px;\n"
"}\n"
"QMenu::item {\n"
"background-color: transparent;\n"
"}\n"
"QMenu::item:selected {\n"
"background-color: #0b5ed7;\n"
"color: rgb(255,255,255);\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.dateEdit_aceptacion = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_aceptacion.setCalendarPopup(True)
        self.dateEdit_aceptacion.setTimeSpec(QtCore.Qt.LocalTime)
        self.dateEdit_aceptacion.setObjectName("dateEdit_aceptacion")
        self.gridLayout_2.addWidget(self.dateEdit_aceptacion, 4, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 0, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_19.setFont(font)
        self.label_19.setWordWrap(True)
        self.label_19.setObjectName("label_19")
        self.gridLayout_2.addWidget(self.label_19, 4, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.gridLayout_2.addWidget(self.label_16, 1, 0, 1, 1)
        self.lineEdit_issn = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_issn.setObjectName("lineEdit_issn")
        self.gridLayout_2.addWidget(self.lineEdit_issn, 1, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.gridLayout_2.addWidget(self.label_17, 2, 0, 1, 1)
        self.lineEdit_doi = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_doi.setObjectName("lineEdit_doi")
        self.gridLayout_2.addWidget(self.lineEdit_doi, 0, 1, 1, 1)
        self.checkBox_publicado = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_publicado.setObjectName("checkBox_publicado")
        self.gridLayout_2.addWidget(self.checkBox_publicado, 7, 1, 1, 1)
        self.checkBox_submitido = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_submitido.setObjectName("checkBox_submitido")
        self.gridLayout_2.addWidget(self.checkBox_submitido, 5, 1, 1, 1)
        self.textEdit_resumen = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_resumen.setObjectName("textEdit_resumen")
        self.gridLayout_2.addWidget(self.textEdit_resumen, 2, 1, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.gridLayout_2.addWidget(self.label_18, 3, 0, 1, 1)
        self.dateEdit_envio = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_envio.setCalendarPopup(True)
        self.dateEdit_envio.setObjectName("dateEdit_envio")
        self.gridLayout_2.addWidget(self.dateEdit_envio, 3, 1, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.gridLayout_2.addWidget(self.label_20, 5, 0, 1, 1)
        self.checkBox_aceptado = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_aceptado.setObjectName("checkBox_aceptado")
        self.gridLayout_2.addWidget(self.checkBox_aceptado, 6, 1, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_2, 1, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.comboBox_tipo = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_tipo.setMaximumSize(QtCore.QSize(240, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_tipo.setFont(font)
        self.comboBox_tipo.setObjectName("comboBox_tipo")
        self.gridLayout.addWidget(self.comboBox_tipo, 1, 1, 1, 2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.spinBox_indiceH = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_indiceH.setMaximumSize(QtCore.QSize(238, 16777215))
        self.spinBox_indiceH.setMaximum(1000)
        self.spinBox_indiceH.setObjectName("spinBox_indiceH")
        self.gridLayout.addWidget(self.spinBox_indiceH, 9, 1, 1, 2)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 10, 0, 1, 1)
        self.comboBox_pais = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_pais.setMaximumSize(QtCore.QSize(240, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_pais.setFont(font)
        self.comboBox_pais.setObjectName("comboBox_pais")
        self.gridLayout.addWidget(self.comboBox_pais, 4, 1, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 11, 0, 1, 1)
        self.textEdit_titulo = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_titulo.setMaximumSize(QtCore.QSize(240, 16777215))
        self.textEdit_titulo.setObjectName("textEdit_titulo")
        self.gridLayout.addWidget(self.textEdit_titulo, 0, 1, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.textEdit_databases = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_databases.setMaximumSize(QtCore.QSize(240, 16777215))
        self.textEdit_databases.setReadOnly(True)
        self.textEdit_databases.setObjectName("textEdit_databases")
        self.gridLayout.addWidget(self.textEdit_databases, 6, 1, 1, 2)
        self.textEdit_gender = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_gender.setMaximumSize(QtCore.QSize(105, 16777215))
        self.textEdit_gender.setReadOnly(True)
        self.textEdit_gender.setObjectName("textEdit_gender")
        self.gridLayout.addWidget(self.textEdit_gender, 10, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_7.setFont(font)
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_5.setFont(font)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_9.setFont(font)
        self.label_9.setWordWrap(False)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 9, 0, 1, 1)
        self.dateEdit_publicacion = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_publicacion.setMaximumSize(QtCore.QSize(240, 16777215))
        self.dateEdit_publicacion.setCalendarPopup(True)
        self.dateEdit_publicacion.setObjectName("dateEdit_publicacion")
        self.gridLayout.addWidget(self.dateEdit_publicacion, 5, 1, 1, 2)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 8, 0, 1, 1)
        self.textEdit_autores = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_autores.setMaximumSize(QtCore.QSize(125, 16777215))
        self.textEdit_autores.setReadOnly(True)
        self.textEdit_autores.setObjectName("textEdit_autores")
        self.gridLayout.addWidget(self.textEdit_autores, 10, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.pushButton_agregar_autor = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_agregar_autor.setObjectName("pushButton_agregar_autor")
        self.gridLayout.addWidget(self.pushButton_agregar_autor, 11, 2, 1, 1)
        self.comboBox_revista = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_revista.setMaximumSize(QtCore.QSize(240, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_revista.setFont(font)
        self.comboBox_revista.setObjectName("comboBox_revista")
        self.gridLayout.addWidget(self.comboBox_revista, 2, 1, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.comboBox_area_salud = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_area_salud.setMaximumSize(QtCore.QSize(240, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_area_salud.setFont(font)
        self.comboBox_area_salud.setObjectName("comboBox_area_salud")
        self.gridLayout.addWidget(self.comboBox_area_salud, 8, 1, 1, 2)
        self.comboBox_categoria = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_categoria.setMaximumSize(QtCore.QSize(240, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_categoria.setFont(font)
        self.comboBox_categoria.setObjectName("comboBox_categoria")
        self.gridLayout.addWidget(self.comboBox_categoria, 3, 1, 1, 2)
        self.toolButton_edit_authors = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_edit_authors.setMaximumSize(QtCore.QSize(16777215, 30))
        self.toolButton_edit_authors.setObjectName("toolButton_edit_authors")
        self.gridLayout.addWidget(self.toolButton_edit_authors, 11, 1, 1, 1)
        self.pushButton_add_database = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_add_database.setObjectName("pushButton_add_database")
        self.gridLayout.addWidget(self.pushButton_add_database, 7, 1, 1, 2)
        self.gridLayout_5.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.gridLayout_3.addWidget(self.label_21, 0, 0, 1, 1)
        self.textEdit_pagweb = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_pagweb.setObjectName("textEdit_pagweb")
        self.gridLayout_3.addWidget(self.textEdit_pagweb, 0, 1, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_22.setFont(font)
        self.label_22.setWordWrap(True)
        self.label_22.setObjectName("label_22")
        self.gridLayout_3.addWidget(self.label_22, 1, 0, 1, 1)
        self.comboBox_direccion = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_direccion.setObjectName("comboBox_direccion")
        self.gridLayout_3.addWidget(self.comboBox_direccion, 1, 1, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.gridLayout_3.addWidget(self.label_23, 2, 0, 1, 1)
        self.textEdit_proyecto = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_proyecto.setObjectName("textEdit_proyecto")
        self.gridLayout_3.addWidget(self.textEdit_proyecto, 2, 1, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.gridLayout_3.addWidget(self.label_24, 3, 0, 1, 1)
        self.checkBox_finalizado = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_finalizado.setObjectName("checkBox_finalizado")
        self.gridLayout_3.addWidget(self.checkBox_finalizado, 3, 1, 1, 1)
        self.checkBox_ejecucion = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_ejecucion.setObjectName("checkBox_ejecucion")
        self.gridLayout_3.addWidget(self.checkBox_ejecucion, 4, 1, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.gridLayout_3.addWidget(self.label_25, 5, 0, 1, 1)
        self.textEdit_observaciones = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_observaciones.setObjectName("textEdit_observaciones")
        self.gridLayout_3.addWidget(self.textEdit_observaciones, 5, 1, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_3, 1, 2, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_5.addWidget(self.label_11, 0, 0, 1, 3)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setObjectName("label_12")
        self.gridLayout_4.addWidget(self.label_12, 0, 0, 1, 1)
        self.label_current_user = QtWidgets.QLabel(self.centralwidget)
        self.label_current_user.setObjectName("label_current_user")
        self.gridLayout_4.addWidget(self.label_current_user, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(1168, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 0, 2, 1, 1)
        self.pushButton_input = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_input.setObjectName("pushButton_input")
        self.gridLayout_4.addWidget(self.pushButton_input, 0, 3, 1, 1)
        self.toolButton_logout = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_logout.setObjectName("toolButton_logout")
        self.gridLayout_4.addWidget(self.toolButton_logout, 1, 0, 1, 1)
        self.toolButton_search_data = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_search_data.setObjectName("toolButton_search_data")
        self.gridLayout_4.addWidget(self.toolButton_search_data, 1, 3, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 2, 0, 1, 3)
        self.horizontalLayout.addLayout(self.gridLayout_5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1465, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PublicacionesGIDI"))
        self.label_15.setText(_translate("MainWindow", "DOI:"))
        self.label_19.setText(_translate("MainWindow", "Fecha de aceptación:"))
        self.label_16.setText(_translate("MainWindow", "ISSN:"))
        self.label_17.setText(_translate("MainWindow", "* Resumen:"))
        self.checkBox_publicado.setText(_translate("MainWindow", "Publicado"))
        self.checkBox_submitido.setText(_translate("MainWindow", "Submitido"))
        self.label_18.setText(_translate("MainWindow", "Fecha de envío:"))
        self.label_20.setText(_translate("MainWindow", "Estado:"))
        self.checkBox_aceptado.setText(_translate("MainWindow", "Aceptado"))
        self.label.setText(_translate("MainWindow", "* Título:"))
        self.label_10.setText(_translate("MainWindow", "* Autores:"))
        self.label_3.setText(_translate("MainWindow", "Revista:"))
        self.label_7.setText(_translate("MainWindow", "* Base de datos indexadas:"))
        self.label_5.setText(_translate("MainWindow", "País de origen de la revista:"))
        self.label_2.setText(_translate("MainWindow", "Tipo de Publicación:"))
        self.label_9.setText(_translate("MainWindow", "Índice de citación - Índice H"))
        self.label_8.setText(_translate("MainWindow", "Área de salud:"))
        self.label_6.setText(_translate("MainWindow", "Fecha de publicación:"))
        self.pushButton_agregar_autor.setText(_translate("MainWindow", "Agregar Autor"))
        self.label_4.setText(_translate("MainWindow", "Categoría:"))
        self.toolButton_edit_authors.setText(_translate("MainWindow", "            Eliminar            "))
        self.pushButton_add_database.setText(_translate("MainWindow", "Agregar / Eliminar"))
        self.label_21.setText(_translate("MainWindow", "Pagina web - evidencia:"))
        self.label_22.setText(_translate("MainWindow", "Dirección a la que pertenece el autor:"))
        self.label_23.setText(_translate("MainWindow", "Nombre del Proyecto:"))
        self.label_24.setText(_translate("MainWindow", "Estado del Proyecto:"))
        self.checkBox_finalizado.setText(_translate("MainWindow", "Finalizado"))
        self.checkBox_ejecucion.setText(_translate("MainWindow", "Ejecución"))
        self.label_25.setText(_translate("MainWindow", "Observaciones:"))
        self.label_11.setText(_translate("MainWindow", "Ingreso de datos - Publicaciones del personal de la GIDI CZ9"))
        self.label_12.setText(_translate("MainWindow", "Usuario:"))
        self.label_current_user.setText(_translate("MainWindow", "usuario"))
        self.pushButton_input.setText(_translate("MainWindow", "            Guardar            "))
        self.toolButton_logout.setText(_translate("MainWindow", "Salir"))
        self.toolButton_search_data.setText(_translate("MainWindow", "            Búsqueda            "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
