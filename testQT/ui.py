# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Ray\Desktop\testQT\gui\test.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(273, 308)
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 20, 241, 271))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.accept = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.accept.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.accept.setStyleSheet("QPushButton {\n"
"    border-radius: 2px;\n"
"    background-color: #2a5bb0;\n"
"    width: 50px;\n"
"    height: 15px;\n"
"    color: rgba(255,255,255, 0.8);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #37b069;\n"
"}")
        self.accept.setObjectName("accept")
        self.gridLayout.addWidget(self.accept, 0, 2, 1, 1)
        self.name = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.name.setStyleSheet("border-radius: 2px")
        self.name.setObjectName("name")
        self.gridLayout.addWidget(self.name, 0, 0, 1, 1)
        self.list = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.list.setStyleSheet("border-radius: 2px")
        self.list.setObjectName("list")
        self.gridLayout.addWidget(self.list, 2, 0, 1, 1)
        self.clear = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.clear.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clear.setStyleSheet("QPushButton {\n"
"    border-radius: 2px;\n"
"    background-color: #2a5bb0;\n"
"    width: 50px;\n"
"    height: 15px;\n"
"    color: rgba(255,255,255, 0.8);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #c94e40;\n"
"}")
        self.clear.setObjectName("clear")
        self.gridLayout.addWidget(self.clear, 1, 2, 2, 1)

        self.retranslateUi(Form)
        self.clear.clicked.connect(self.list.clear)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Base", "Base"))
        self.accept.setText(_translate("Form", "Accept"))
        self.clear.setText(_translate("Form", "Clear"))

