# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.8
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_menu(object):
    def setupUi(self, MainWindow_menu):
        MainWindow_menu.setObjectName("MainWindow_menu")
        MainWindow_menu.resize(331, 187)
        self.centralwidget = QtWidgets.QWidget(MainWindow_menu)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 30, 239, 83))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 0, 2, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 1, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.widget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 1, 1, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.widget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 1, 2, 1, 1)
        self.pushButton_publications = QtWidgets.QPushButton(self.widget)
        self.pushButton_publications.setObjectName("pushButton_publications")
        self.gridLayout.addWidget(self.pushButton_publications, 2, 0, 1, 1)
        MainWindow_menu.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow_menu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 331, 21))
        self.menubar.setObjectName("menubar")
        MainWindow_menu.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow_menu)
        self.statusbar.setObjectName("statusbar")
        MainWindow_menu.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow_menu)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_menu)

    def retranslateUi(self, MainWindow_menu):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_menu.setWindowTitle(_translate("MainWindow_menu", "Menu"))
        self.pushButton.setText(_translate("MainWindow_menu", "PushButton"))
        self.pushButton_2.setText(_translate("MainWindow_menu", "PushButton"))
        self.pushButton_3.setText(_translate("MainWindow_menu", "PushButton"))
        self.pushButton_4.setText(_translate("MainWindow_menu", "PushButton"))
        self.pushButton_5.setText(_translate("MainWindow_menu", "PushButton"))
        self.pushButton_6.setText(_translate("MainWindow_menu", "PushButton"))
        self.pushButton_publications.setText(_translate("MainWindow_menu", "Publicaciones"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow_menu = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_menu()
    ui.setupUi(MainWindow_menu)
    MainWindow_menu.show()
    sys.exit(app.exec_())
