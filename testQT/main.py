from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
from ui import Ui_Form

# SYNC APP QT:
app = QtWidgets.QApplication(sys.argv)
# VARS:
Form = QtWidgets.QWidget()
ui = Ui_Form()
database_dir = os.curdir + '/database/'
# INIT FORM:
ui.setupUi(Form)
Form.show()


# NEW USER:
def write_user():
    name = ui.name.text()
    if name != ' ':
        with open(database_dir + 'base.txt', 'a+') as file:
            file.write(name + "\r")
        with open(database_dir + 'base.txt', 'r') as rFile:
            ui.list.setText(rFile.read())
        ui.name.clear()


# CLEAR DATABASE:
def delete_database():
    os.remove(database_dir + 'base.txt')


# IN START:
# CREATE DB FOLDER:
if not os.path.exists(database_dir):
    os.makedirs(database_dir)
# DON'T READ IF FOLDER EMPTY:
if len(os.listdir(database_dir)) != 0:
    with open(database_dir + 'base.txt', 'r') as file:
        ui.list.setText(file.read())
ui.name.setPlaceholderText("Enter username")
# EVENTS:
ui.clear.clicked.connect(delete_database)
ui.accept.clicked.connect(write_user)
# INIT APP:
sys.exit(app.exec_())
