# https://www.youtube.com/watch?v=2ZGpaRyO-jE

import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtGui import QPixmap

class MainWindow(QDialog):
    '''Show image with a button constructor'''
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('show_logo.ui', self)
        self.btn_show_hidden_image.clicked.connect(self.add_image)


    def add_image(self):
        '''Add the image'''
        qpixmap = QPixmap('sui_logo.png')
        self.lbl_hidden_image.setPixmap(qpixmap)

# Main
app = QApplication(sys.argv)
mainwindow = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedHeight(700)
widget.setFixedWidth(700)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print('Existing')