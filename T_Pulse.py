# -- T_Pulse.py as part of FERS XML File I/O as part of FERS Plugin
# -- Created by James Gripper 
# -- November 2016
# -*- coding: utf-8 -*-#

from PyQt4 import QtCore, QtGui
from addNodes import *
from lxml import etree
import FERS_Input
import sys
import os

## reads in filename string
placeholder = open("filename.txt", "r")
filename = placeholder.read()
placeholder.close() 

## creates parser object
parser = etree.XMLParser(remove_blank_text=True,ns_clean=True)

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_T_Pulse(QtGui.QMainWindow):

    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

    def setupUi(self, T_Pulse):
        T_Pulse.setObjectName(_fromUtf8("T_Pulse"))
        T_Pulse.resize(531, 267)
        self.centralwidget = QtGui.QWidget(T_Pulse)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout3 = QtGui.QHBoxLayout()
        self.horizontalLayout3.setObjectName(_fromUtf8("horizontalLayout3"))
        self.T_Pulse_label = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_label.setBaseSize(QtCore.QSize(7, 0))
        self.T_Pulse_label.setObjectName(_fromUtf8("T_Pulse_label"))
        self.horizontalLayout3.addWidget(self.T_Pulse_label)
        self._2 = QtGui.QGridLayout()
        self._2.setObjectName(_fromUtf8("_2"))
        self.T_Pulse_power_label = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_power_label.setObjectName(_fromUtf8("T_Pulse_power_label"))
        self._2.addWidget(self.T_Pulse_power_label, 2, 0, 1, 1)
        self.T_Pulse_name_label = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_name_label.setObjectName(_fromUtf8("T_Pulse_name_label"))
        self._2.addWidget(self.T_Pulse_name_label, 0, 0, 1, 1)
        self.T_Pulse_filename_input = QtGui.QLineEdit(self.centralwidget)
        self.T_Pulse_filename_input.setEnabled(True)
        self.T_Pulse_filename_input.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.T_Pulse_filename_input.setObjectName(_fromUtf8("T_Pulse_filename_input"))
        self._2.addWidget(self.T_Pulse_filename_input, 1, 1, 1, 1)
        self.T_Pulse_power_input = QtGui.QLineEdit(self.centralwidget)
        self.T_Pulse_power_input.setObjectName(_fromUtf8("T_Pulse_power_input"))
        self._2.addWidget(self.T_Pulse_power_input, 2, 1, 1, 1)
        self.T_Pulse_carrier_input = QtGui.QLineEdit(self.centralwidget)
        self.T_Pulse_carrier_input.setObjectName(_fromUtf8("T_Pulse_carrier_input"))
        self._2.addWidget(self.T_Pulse_carrier_input, 3, 1, 1, 1)
        self.T_Pulse_power_clear = QtGui.QPushButton(self.centralwidget)
        self.T_Pulse_power_clear.setObjectName(_fromUtf8("T_Pulse_power_clear"))
        self._2.addWidget(self.T_Pulse_power_clear, 2, 3, 1, 1)
        self.T_Pulse_file_label = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_file_label.setObjectName(_fromUtf8("T_Pulse_file_label"))
        self._2.addWidget(self.T_Pulse_file_label, 1, 0, 1, 1)
        self.T_Pulse_name_clear = QtGui.QPushButton(self.centralwidget)
        self.T_Pulse_name_clear.setObjectName(_fromUtf8("T_Pulse_name_clear"))
        self._2.addWidget(self.T_Pulse_name_clear, 1, 3, 1, 1)
        self.T_Pulse_filename_clear = QtGui.QPushButton(self.centralwidget)
        self.T_Pulse_filename_clear.setObjectName(_fromUtf8("T_Pulse_filename_clear"))
        self._2.addWidget(self.T_Pulse_filename_clear, 0, 3, 1, 1)
        self.T_Pulse_name_input = QtGui.QLineEdit(self.centralwidget)
        self.T_Pulse_name_input.setObjectName(_fromUtf8("T_Pulse_name_input"))
        self._2.addWidget(self.T_Pulse_name_input, 0, 1, 1, 1)
        self.T_Pulse_Carrier_label = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_Carrier_label.setObjectName(_fromUtf8("T_Pulse_Carrier_label"))
        self._2.addWidget(self.T_Pulse_Carrier_label, 3, 0, 1, 1)
        self.T_Pulse_carrier_clear = QtGui.QPushButton(self.centralwidget)
        self.T_Pulse_carrier_clear.setObjectName(_fromUtf8("T_Pulse_carrier_clear"))
        self._2.addWidget(self.T_Pulse_carrier_clear, 3, 3, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self._2.addWidget(self.label_2, 1, 2, 1, 1)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self._2.addWidget(self.label_3, 2, 2, 1, 1)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self._2.addWidget(self.label_4, 3, 2, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self._2.addWidget(self.label, 5, 0, 1, 1)
        self.T_Pulse_removal_input = QtGui.QLineEdit(self.centralwidget)
        self.T_Pulse_removal_input.setObjectName(_fromUtf8("T_Pulse_removal_input"))
        self._2.addWidget(self.T_Pulse_removal_input, 6, 1, 1, 1)
        self.T_Pulse_Carrier_label_2 = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_Carrier_label_2.setObjectName(_fromUtf8("T_Pulse_Carrier_label_2"))
        self._2.addWidget(self.T_Pulse_Carrier_label_2, 6, 0, 1, 1)
        self.T_Pulse_Add_btn = QtGui.QPushButton(self.centralwidget)
        self.T_Pulse_Add_btn.setObjectName(_fromUtf8("T_Pulse_Add_btn"))
        self._2.addWidget(self.T_Pulse_Add_btn, 4, 1, 1, 1)
        self.T_Pulse_Remove_btn = QtGui.QPushButton(self.centralwidget)
        self.T_Pulse_Remove_btn.setObjectName(_fromUtf8("T_Pulse_Remove_btn"))
        self._2.addWidget(self.T_Pulse_Remove_btn, 7, 1, 1, 1)
        self.T_Pulse_carrier_clear_2 = QtGui.QPushButton(self.centralwidget)
        self.T_Pulse_carrier_clear_2.setObjectName(_fromUtf8("T_Pulse_carrier_clear_2"))
        self._2.addWidget(self.T_Pulse_carrier_clear_2, 6, 3, 1, 1)
        self._2.setColumnStretch(0, 8)
        self.horizontalLayout3.addLayout(self._2)
        self.verticalLayout.addLayout(self.horizontalLayout3)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)
        T_Pulse.setCentralWidget(self.centralwidget)

        self.retranslateUi(T_Pulse)
        QtCore.QObject.connect(self.T_Pulse_filename_clear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.T_Pulse_name_input.clear)
        QtCore.QObject.connect(self.T_Pulse_name_clear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.T_Pulse_filename_input.clear)
        QtCore.QObject.connect(self.T_Pulse_power_clear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.T_Pulse_power_input.clear)
        QtCore.QObject.connect(self.T_Pulse_carrier_clear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.T_Pulse_carrier_input.clear)
        QtCore.QObject.connect(self.T_Pulse_carrier_clear_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.T_Pulse_removal_input.clear)
        QtCore.QMetaObject.connectSlotsByName(T_Pulse)
        T_Pulse.setTabOrder(self.T_Pulse_name_input, self.T_Pulse_filename_input)
        T_Pulse.setTabOrder(self.T_Pulse_filename_input, self.T_Pulse_power_input)
        T_Pulse.setTabOrder(self.T_Pulse_power_input, self.T_Pulse_carrier_input)
        T_Pulse.setTabOrder(self.T_Pulse_carrier_input, self.T_Pulse_Add_btn)
        T_Pulse.setTabOrder(self.T_Pulse_Add_btn, self.T_Pulse_removal_input)
        T_Pulse.setTabOrder(self.T_Pulse_removal_input, self.T_Pulse_Remove_btn)
        T_Pulse.setTabOrder(self.T_Pulse_Remove_btn, self.pushButton)
        T_Pulse.setTabOrder(self.pushButton, self.T_Pulse_filename_clear)
        T_Pulse.setTabOrder(self.T_Pulse_filename_clear, self.T_Pulse_name_clear)
        T_Pulse.setTabOrder(self.T_Pulse_name_clear, self.T_Pulse_power_clear)
        T_Pulse.setTabOrder(self.T_Pulse_power_clear, self.T_Pulse_carrier_clear)
        T_Pulse.setTabOrder(self.T_Pulse_carrier_clear, self.T_Pulse_carrier_clear_2)

    def retranslateUi(self, T_Pulse):
        T_Pulse.setWindowTitle(_translate("T_Pulse", "T_Pulse", None))
        self.T_Pulse_label.setText(_translate("T_Pulse", "Transmission Pulse", None))
        self.T_Pulse_power_label.setText(_translate("T_Pulse", "Power", None))
        self.T_Pulse_name_label.setText(_translate("T_Pulse", "Name", None))
        self.T_Pulse_filename_input.setPlaceholderText(_translate("T_Pulse", "<Sample Filename>", None))
        self.T_Pulse_power_input.setPlaceholderText(_translate("T_Pulse", "<Value Watts>", None))
        self.T_Pulse_carrier_input.setPlaceholderText(_translate("T_Pulse", "<Value Hz>", None))
        self.T_Pulse_power_clear.setText(_translate("T_Pulse", "Clear", None))
        self.T_Pulse_file_label.setText(_translate("T_Pulse", "Type (file)", None))
        self.T_Pulse_name_clear.setText(_translate("T_Pulse", "Clear", None))
        self.T_Pulse_filename_clear.setText(_translate("T_Pulse", "Clear", None))
        self.T_Pulse_name_input.setPlaceholderText(_translate("T_Pulse", "<Sample Name>", None))
        self.T_Pulse_Carrier_label.setToolTip(_translate("T_Pulse", "eg. 89e6", None))
        self.T_Pulse_Carrier_label.setText(_translate("T_Pulse", "Carrier Frequency", None))
        self.T_Pulse_carrier_clear.setText(_translate("T_Pulse", "Clear", None))
        self.label_3.setText(_translate("T_Pulse", "Watts", None))
        self.label_4.setText(_translate("T_Pulse", "Hz", None))
        self.T_Pulse_removal_input.setPlaceholderText(_translate("T_Pulse", "<Sample Name>", None))
        self.T_Pulse_Carrier_label_2.setToolTip(_translate("T_Pulse", "eg. 89e6", None))
        self.T_Pulse_Carrier_label_2.setText(_translate("T_Pulse", "Remove existing TPulse", None))
        self.T_Pulse_Add_btn.setText(_translate("T_Pulse", "Add to XML", None))
        self.T_Pulse_Remove_btn.setText(_translate("T_Pulse", "Remove from XML", None))
        self.T_Pulse_carrier_clear_2.setText(_translate("T_Pulse", "Clear", None))
        self.pushButton.setText(_translate("T_Pulse", "Show XML", None))

        ## connects functions to buttons
        self.T_Pulse_Add_btn.clicked.connect(self.callAppend)
        self.pushButton.clicked.connect(self.showEntry)
        self.T_Pulse_Remove_btn.clicked.connect(self.removeNode)
    
    ## removes transmission pulse from simulation
    def removeNode(self):
        doc = etree.parse(filename, parser)
        root = doc.getroot()
        tree = etree.ElementTree(root)  
        for pulse in root.findall('pulse'):
            name = pulse.get('name')
            if name == str(self.T_Pulse_removal_input.text()):
                root.remove(pulse)
                doc.write(filename,pretty_print=False)
                print '--Pulse removed--'
            else:
                print "--Pulse not found--"
       
    ## prints formatted xml to console
    def showEntry(self):
        doc = etree.parse(filename, parser)
        print(etree.tostring(doc, pretty_print=True))     

    ## adds transmission pulse to simulation
    def callAppend(self):
        name =str(self.T_Pulse_name_input.text()) 
        pulse = str(self.T_Pulse_filename_input.text())
        power = str(self.T_Pulse_power_input.text())
        carrier = str(self.T_Pulse_carrier_input.text())
        appendTPulse(filename, name, 'file',pulse , power, carrier)  
        
        print '--Transmission Pulse added to Simulation--' 


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    T_Pulse = QtGui.QMainWindow()
    ui = Ui_T_Pulse()
    ui.setupUi(T_Pulse)
    T_Pulse.show()
    sys.exit(app.exec_())

