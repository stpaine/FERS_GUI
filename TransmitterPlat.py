# -- TransmitterPlat.py as part of FERS XML File I/O as past of FERS Plugin
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

class Ui_Transmitter(QtGui.QMainWindow):

    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        
    def setupUi(self, Transmitter):
        Transmitter.setObjectName(_fromUtf8("Transmitter"))
        Transmitter.resize(575, 348)
        self.centralwidget = QtGui.QWidget(Transmitter)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout3 = QtGui.QHBoxLayout()
        self.horizontalLayout3.setObjectName(_fromUtf8("horizontalLayout3"))
        self.Tx_label = QtGui.QLabel(self.centralwidget)
        self.Tx_label.setBaseSize(QtCore.QSize(7, 0))
        self.Tx_label.setObjectName(_fromUtf8("Tx_label"))
        self.horizontalLayout3.addWidget(self.Tx_label)
        self._2 = QtGui.QGridLayout()
        self._2.setObjectName(_fromUtf8("_2"))
        self.Tx_PRF_input = QtGui.QLineEdit(self.centralwidget)
        self.Tx_PRF_input.setObjectName(_fromUtf8("Tx_PRF_input"))
        self._2.addWidget(self.Tx_PRF_input, 6, 1, 1, 1)
        self.T_Pulse_name_label_2 = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_name_label_2.setObjectName(_fromUtf8("T_Pulse_name_label_2"))
        self._2.addWidget(self.T_Pulse_name_label_2, 8, 0, 1, 1)
        self.T_Pulse_carrier_clear = QtGui.QPushButton(self.centralwidget)
        self.T_Pulse_carrier_clear.setObjectName(_fromUtf8("T_Pulse_carrier_clear"))
        self._2.addWidget(self.T_Pulse_carrier_clear, 4, 3, 1, 1)
        self.Tx_name_input = QtGui.QLineEdit(self.centralwidget)
        self.Tx_name_input.setObjectName(_fromUtf8("Tx_name_input"))
        self._2.addWidget(self.Tx_name_input, 1, 1, 1, 1)
        self.T_Pulse_carrier_clear_4 = QtGui.QPushButton(self.centralwidget)
        self.T_Pulse_carrier_clear_4.setObjectName(_fromUtf8("T_Pulse_carrier_clear_4"))
        self._2.addWidget(self.T_Pulse_carrier_clear_4, 6, 3, 1, 1)
        self.T_Pulse_Carrier_label_2 = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_Carrier_label_2.setObjectName(_fromUtf8("T_Pulse_Carrier_label_2"))
        self._2.addWidget(self.T_Pulse_Carrier_label_2, 5, 0, 1, 1)
        self.T_Pulse_filename_clear = QtGui.QPushButton(self.centralwidget)
        self.T_Pulse_filename_clear.setObjectName(_fromUtf8("T_Pulse_filename_clear"))
        self._2.addWidget(self.T_Pulse_filename_clear, 1, 3, 1, 1)
        self.Tx_Pulse_power_input = QtGui.QLineEdit(self.centralwidget)
        self.Tx_Pulse_power_input.setObjectName(_fromUtf8("Tx_Pulse_power_input"))
        self._2.addWidget(self.Tx_Pulse_power_input, 3, 1, 1, 1)
        self.checkBox_2 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self._2.addWidget(self.checkBox_2, 2, 1, 1, 1)
        self.T_Pulse_power_clear = QtGui.QPushButton(self.centralwidget)
        self.T_Pulse_power_clear.setObjectName(_fromUtf8("T_Pulse_power_clear"))
        self._2.addWidget(self.T_Pulse_power_clear, 3, 3, 1, 1)
        self.Tx_Antenna_Name_input = QtGui.QLineEdit(self.centralwidget)
        self.Tx_Antenna_Name_input.setObjectName(_fromUtf8("Tx_Antenna_Name_input"))
        self._2.addWidget(self.Tx_Antenna_Name_input, 4, 1, 1, 1)
        self.T_Pulse_Carrier_label_3 = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_Carrier_label_3.setObjectName(_fromUtf8("T_Pulse_Carrier_label_3"))
        self._2.addWidget(self.T_Pulse_Carrier_label_3, 6, 0, 1, 1)
        self.T_Pulse_name_label = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_name_label.setObjectName(_fromUtf8("T_Pulse_name_label"))
        self._2.addWidget(self.T_Pulse_name_label, 1, 0, 1, 1)
        self.Tx_Timer_name_input = QtGui.QLineEdit(self.centralwidget)
        self.Tx_Timer_name_input.setObjectName(_fromUtf8("Tx_Timer_name_input"))
        self._2.addWidget(self.Tx_Timer_name_input, 5, 1, 1, 1)
        self.T_Pulse_Carrier_label = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_Carrier_label.setObjectName(_fromUtf8("T_Pulse_Carrier_label"))
        self._2.addWidget(self.T_Pulse_Carrier_label, 4, 0, 1, 1)
        self.checkBox = QtGui.QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self._2.addWidget(self.checkBox, 2, 3, 1, 1)
        self.T_Pulse_name_label_3 = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_name_label_3.setObjectName(_fromUtf8("T_Pulse_name_label_3"))
        self._2.addWidget(self.T_Pulse_name_label_3, 9, 0, 1, 1)
        self.Tx_Record_btn = QtGui.QPushButton(self.centralwidget)
        self.Tx_Record_btn.setObjectName(_fromUtf8("Tx_Record_btn"))
        self._2.addWidget(self.Tx_Record_btn, 7, 1, 1, 1)
        self.T_Pulse_carrier_clear_3 = QtGui.QPushButton(self.centralwidget)
        self.T_Pulse_carrier_clear_3.setObjectName(_fromUtf8("T_Pulse_carrier_clear_3"))
        self._2.addWidget(self.T_Pulse_carrier_clear_3, 5, 3, 1, 1)
        self.T_Pulse_file_label = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_file_label.setObjectName(_fromUtf8("T_Pulse_file_label"))
        self._2.addWidget(self.T_Pulse_file_label, 2, 0, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self._2.addWidget(self.label, 6, 2, 1, 1)
        self.Tx_Record_btn_2 = QtGui.QPushButton(self.centralwidget)
        self.Tx_Record_btn_2.setObjectName(_fromUtf8("Tx_Record_btn_2"))
        self._2.addWidget(self.Tx_Record_btn_2, 10, 1, 1, 1)
        self.T_Pulse_carrier_clear_5 = QtGui.QPushButton(self.centralwidget)
        self.T_Pulse_carrier_clear_5.setObjectName(_fromUtf8("T_Pulse_carrier_clear_5"))
        self._2.addWidget(self.T_Pulse_carrier_clear_5, 9, 3, 1, 1)
        self.T_Pulse_power_label = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_power_label.setObjectName(_fromUtf8("T_Pulse_power_label"))
        self._2.addWidget(self.T_Pulse_power_label, 3, 0, 1, 1)
        self.Tx_name_input_3 = QtGui.QLineEdit(self.centralwidget)
        self.Tx_name_input_3.setObjectName(_fromUtf8("Tx_name_input_3"))
        self._2.addWidget(self.Tx_name_input_3, 9, 1, 1, 1)
        self.T_Pulse_name_label_4 = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_name_label_4.setObjectName(_fromUtf8("T_Pulse_name_label_4"))
        self._2.addWidget(self.T_Pulse_name_label_4, 0, 0, 1, 1)
        self.platform_sel = QtGui.QComboBox(self.centralwidget)
        self.platform_sel.setObjectName(_fromUtf8("platform_sel"))
        self._2.addWidget(self.platform_sel, 0, 1, 1, 3)
        self._2.setColumnStretch(0, 8)
        self.horizontalLayout3.addLayout(self._2)
        self.verticalLayout.addLayout(self.horizontalLayout3)
        self.Tx_back_btn = QtGui.QPushButton(self.centralwidget)
        self.Tx_back_btn.setObjectName(_fromUtf8("Tx_back_btn"))
        self.verticalLayout.addWidget(self.Tx_back_btn)
        Transmitter.setCentralWidget(self.centralwidget)

        self.retranslateUi(Transmitter)
        QtCore.QObject.connect(self.T_Pulse_filename_clear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Tx_name_input.clear)
        QtCore.QObject.connect(self.T_Pulse_power_clear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Tx_Pulse_power_input.clear)
        QtCore.QObject.connect(self.T_Pulse_carrier_clear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Tx_Antenna_Name_input.clear)
        QtCore.QObject.connect(self.T_Pulse_carrier_clear_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Tx_Timer_name_input.clear)
        QtCore.QObject.connect(self.T_Pulse_carrier_clear_4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Tx_PRF_input.clear)
        QtCore.QObject.connect(self.T_Pulse_carrier_clear_5, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Tx_name_input_3.clear)
        QtCore.QMetaObject.connectSlotsByName(Transmitter)
        Transmitter.setTabOrder(self.Tx_name_input, self.checkBox_2)
        Transmitter.setTabOrder(self.checkBox_2, self.checkBox)
        Transmitter.setTabOrder(self.checkBox, self.Tx_Pulse_power_input)
        Transmitter.setTabOrder(self.Tx_Pulse_power_input, self.Tx_Antenna_Name_input)
        Transmitter.setTabOrder(self.Tx_Antenna_Name_input, self.Tx_Timer_name_input)
        Transmitter.setTabOrder(self.Tx_Timer_name_input, self.Tx_PRF_input)
        Transmitter.setTabOrder(self.Tx_PRF_input, self.Tx_Record_btn)
        Transmitter.setTabOrder(self.Tx_Record_btn, self.Tx_name_input_3)
        Transmitter.setTabOrder(self.Tx_name_input_3, self.Tx_Record_btn_2)
        Transmitter.setTabOrder(self.Tx_Record_btn_2, self.Tx_back_btn)
        Transmitter.setTabOrder(self.Tx_back_btn, self.T_Pulse_filename_clear)
        Transmitter.setTabOrder(self.T_Pulse_filename_clear, self.T_Pulse_power_clear)
        Transmitter.setTabOrder(self.T_Pulse_power_clear, self.T_Pulse_carrier_clear)
        Transmitter.setTabOrder(self.T_Pulse_carrier_clear, self.T_Pulse_carrier_clear_3)
        Transmitter.setTabOrder(self.T_Pulse_carrier_clear_3, self.T_Pulse_carrier_clear_4)
        Transmitter.setTabOrder(self.T_Pulse_carrier_clear_4, self.T_Pulse_carrier_clear_5)

    def retranslateUi(self, Transmitter):
        Transmitter.setWindowTitle(_translate("Transmitter", "Transmitter", None))
        self.Tx_label.setText(_translate("Transmitter", "Transmitter", None))
        self.Tx_PRF_input.setPlaceholderText(_translate("Transmitter", "<Sample Value>", None))
        self.T_Pulse_name_label_2.setText(_translate("Transmitter", "Remove Existing Transmitter", None))
        self.T_Pulse_carrier_clear.setText(_translate("Transmitter", "Clear", None))
        self.Tx_name_input.setPlaceholderText(_translate("Transmitter", "<Sample Name>", None))
        self.T_Pulse_carrier_clear_4.setText(_translate("Transmitter", "Clear", None))
        self.T_Pulse_Carrier_label_2.setText(_translate("Transmitter", "Timer Name", None))
        self.T_Pulse_filename_clear.setText(_translate("Transmitter", "Clear", None))
        self.Tx_Pulse_power_input.setPlaceholderText(_translate("Transmitter", "<Sample Name>", None))
        self.checkBox_2.setText(_translate("Transmitter", "Pulsed", None))
        self.T_Pulse_power_clear.setText(_translate("Transmitter", "Clear", None))
        self.Tx_Antenna_Name_input.setPlaceholderText(_translate("Transmitter", "<Sample Name>", None))
        self.T_Pulse_Carrier_label_3.setText(_translate("Transmitter", "PRF", None))
        self.T_Pulse_name_label.setText(_translate("Transmitter", "Transmitter Name", None))
        self.Tx_Timer_name_input.setPlaceholderText(_translate("Transmitter", "<Sample Name>", None))
        self.T_Pulse_Carrier_label.setText(_translate("Transmitter", "Antenna Name", None))
        self.checkBox.setText(_translate("Transmitter", "Continous", None))
        self.T_Pulse_name_label_3.setText(_translate("Transmitter", "Name", None))
        self.Tx_Record_btn.setText(_translate("Transmitter", "Add to XML", None))
        self.T_Pulse_carrier_clear_3.setText(_translate("Transmitter", "Clear", None))
        self.T_Pulse_file_label.setText(_translate("Transmitter", "Type ", None))
        self.label.setText(_translate("Transmitter", "Hz", None))
        self.Tx_Record_btn_2.setText(_translate("Transmitter", "Remove from XML", None))
        self.T_Pulse_carrier_clear_5.setText(_translate("Transmitter", "Clear", None))
        self.T_Pulse_power_label.setText(_translate("Transmitter", "Pulse Name", None))
        self.Tx_name_input_3.setPlaceholderText(_translate("Transmitter", "<Sample Name>", None))
        self.T_Pulse_name_label_4.setText(_translate("Transmitter", "Platform Name", None))
        self.Tx_back_btn.setText(_translate("Transmitter", "View XML", None))
        
        ## connects functions to buttons
        self.Tx_Record_btn.clicked.connect(self.callAppend)
        self.Tx_back_btn.clicked.connect(self.showEntry)
        self.Tx_Record_btn_2.clicked.connect(self.removeNode)
    
        ## adds platform names to selection boxs
        self.platform_sel.clear()
    
        names = []
        doc = etree.parse(filename, parser)
        sim = doc.getroot()
        for plat in sim.findall('platform'):
            name = plat.get('name')
            names.append(name)
        for name in names:
            self.platform_sel.addItem(name)         

    ## removes transmitter from platform
    def removeNode(self):
        doc = etree.parse(filename, parser)
        sim = doc.getroot()
        for plat in sim.findall('platform'):
            name = plat.get('name')
            if name == str(self.platform_sel.currentText()):
                for trans in plat.findall('transmitter'):
                    name = trans.get('name')
                    if name == str(self.Tx_name_input_3.text()):            
                        plat.remove(trans)
                        doc.write(filename,pretty_print=True)
                        print '--Transmitter removed from Platform--'
                    else:
                        print "--Transmitter not found--"
            else:
                print '--Invalid Platform. Please Try Again--'
        
    ## prints formatted xml to console
    def showEntry(self):
        doc = etree.parse(filename, parser)
        print(etree.tostring(doc, pretty_print=True)) 

    ## adds transmitter to platform
    def callAppend(self):
        name = str(self.Tx_name_input.text())
        pulse_name = str(self.Tx_Pulse_power_input.text())
        antenna_name = str(self.Tx_Antenna_Name_input.text())
        clock_name = str(self.Tx_Timer_name_input.text())
        prf = str(self.Tx_PRF_input.text())
        plat_name = str(self.platform_sel.currentText())
        
        if (self.checkBox_2.isChecked()):
            trans_type = 'pulsed'
            appendTxToPlatform(filename,plat_name, name, trans_type, pulse_name, antenna_name, clock_name, prf)
        elif (self.checkBox.isChecked()):
            trans_type = 'continuous'
            appendTxToPlatform(filename,plat_name, name, trans_type, pulse_name, antenna_name, clock_name, prf)
        else:
            print '--Please select the appropriate transmission type--'

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Transmitter = QtGui.QMainWindow()
    ui = Ui_Transmitter()
    ui.setupUi(Transmitter)
    Transmitter.show()
    sys.exit(app.exec_())

