import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtGui import QPixmap
from receiver import ESP32

class IndoorMain(QDialog):
    '''Show image with a button constructor'''
    def __init__(self):
        super(IndoorMain, self).__init__()
        loadUi('indoor.ui', self)
        #self.btn_show_hidden_image.clicked.connect(self.add_image)
        self.chk_show_data.stateChanged.connect(self.mac_rssi)

    def mac_rssi(self):
        message = ESP32()
        if self.lbl_indoor_data.isChecked() == True:
            self.lbl_show_data.setText(message)


# Main
app = QApplication(sys.argv)
indoormain = IndoorMain()
widget = QtWidgets.QStackedWidget()
widget.addWidget(indoormain)
widget.setFixedHeight(700)
widget.setFixedWidth(700)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print('Existing')
