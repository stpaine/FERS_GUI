# -- Monostatics.py as part of FERS XML File I/O as part of FERS Plugin
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

class Ui_Monostatics_2(QtGui.QMainWindow):

    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        
    def setupUi(self, Monostatics_2):
        Monostatics_2.setObjectName(_fromUtf8("Monostatics_2"))
        Monostatics_2.resize(532, 335)
        self.centralwidget = QtGui.QWidget(Monostatics_2)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout3 = QtGui.QHBoxLayout()
        self.horizontalLayout3.setObjectName(_fromUtf8("horizontalLayout3"))
        self.Monostatics = QtGui.QLabel(self.centralwidget)
        self.Monostatics.setBaseSize(QtCore.QSize(7, 0))
        self.Monostatics.setObjectName(_fromUtf8("Monostatics"))
        self.horizontalLayout3.addWidget(self.Monostatics)
        self._2 = QtGui.QGridLayout()
        self._2.setContentsMargins(-1, -1, -1, 7)
        self._2.setObjectName(_fromUtf8("_2"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self._2.addWidget(self.label_2, 6, 2, 1, 1)
        self.T_Pulse_carrier_clear_3 = QtGui.QPushButton(self.centralwidget)
        self.T_Pulse_carrier_clear_3.setObjectName(_fromUtf8("T_Pulse_carrier_clear_3"))
        self._2.addWidget(self.T_Pulse_carrier_clear_3, 6, 3, 1, 1)
        self.T_Pulse_Carrier_label_3 = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_Carrier_label_3.setObjectName(_fromUtf8("T_Pulse_Carrier_label_3"))
        self._2.addWidget(self.T_Pulse_Carrier_label_3, 6, 0, 1, 1)
        self.T_Pulse_carrier_clear = QtGui.QPushButton(self.centralwidget)
        self.T_Pulse_carrier_clear.setObjectName(_fromUtf8("T_Pulse_carrier_clear"))
        self._2.addWidget(self.T_Pulse_carrier_clear, 3, 3, 1, 1)
        self.T_Pulse_carrier_clear_4 = QtGui.QPushButton(self.centralwidget)
        self.T_Pulse_carrier_clear_4.setObjectName(_fromUtf8("T_Pulse_carrier_clear_4"))
        self._2.addWidget(self.T_Pulse_carrier_clear_4, 7, 3, 1, 1)
        self.Mono_wind_skip_input = QtGui.QLineEdit(self.centralwidget)
        self.Mono_wind_skip_input.setObjectName(_fromUtf8("Mono_wind_skip_input"))
        self._2.addWidget(self.Mono_wind_skip_input, 5, 1, 1, 1)
        self.checkBox_2 = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self._2.addWidget(self.checkBox_2, 1, 3, 1, 1)
        self.Mono_clk_name_input = QtGui.QLineEdit(self.centralwidget)
        self.Mono_clk_name_input.setObjectName(_fromUtf8("Mono_clk_name_input"))
        self._2.addWidget(self.Mono_clk_name_input, 3, 1, 1, 1)
        self.T_Pulse_Carrier_label_2 = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_Carrier_label_2.setObjectName(_fromUtf8("T_Pulse_Carrier_label_2"))
        self._2.addWidget(self.T_Pulse_Carrier_label_2, 5, 0, 1, 1)
        self.T_Pulse_Carrier_label_4 = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_Carrier_label_4.setObjectName(_fromUtf8("T_Pulse_Carrier_label_4"))
        self._2.addWidget(self.T_Pulse_Carrier_label_4, 7, 0, 1, 1)
        self.T_Pulse_carrier_clear_2 = QtGui.QPushButton(self.centralwidget)
        self.T_Pulse_carrier_clear_2.setObjectName(_fromUtf8("T_Pulse_carrier_clear_2"))
        self._2.addWidget(self.T_Pulse_carrier_clear_2, 5, 3, 1, 1)
        self.Mono_PRF_input = QtGui.QLineEdit(self.centralwidget)
        self.Mono_PRF_input.setObjectName(_fromUtf8("Mono_PRF_input"))
        self._2.addWidget(self.Mono_PRF_input, 7, 1, 1, 1)
        self.Mono_name_input = QtGui.QLineEdit(self.centralwidget)
        self.Mono_name_input.setObjectName(_fromUtf8("Mono_name_input"))
        self._2.addWidget(self.Mono_name_input, 0, 1, 1, 1)
        self.checkBox = QtGui.QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self._2.addWidget(self.checkBox, 1, 1, 1, 1)
        self.T_Pulse_file_label = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_file_label.setObjectName(_fromUtf8("T_Pulse_file_label"))
        self._2.addWidget(self.T_Pulse_file_label, 1, 0, 1, 1)
        self.Mono_ant_name_input = QtGui.QLineEdit(self.centralwidget)
        self.Mono_ant_name_input.setObjectName(_fromUtf8("Mono_ant_name_input"))
        self._2.addWidget(self.Mono_ant_name_input, 2, 1, 1, 1)
        self.T_Pulse_power_label = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_power_label.setObjectName(_fromUtf8("T_Pulse_power_label"))
        self._2.addWidget(self.T_Pulse_power_label, 2, 0, 1, 1)
        self.T_Pulse_power_clear = QtGui.QPushButton(self.centralwidget)
        self.T_Pulse_power_clear.setObjectName(_fromUtf8("T_Pulse_power_clear"))
        self._2.addWidget(self.T_Pulse_power_clear, 2, 3, 1, 1)
        self.T_Pulse_name_label = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_name_label.setObjectName(_fromUtf8("T_Pulse_name_label"))
        self._2.addWidget(self.T_Pulse_name_label, 0, 0, 1, 1)
        self.T_Pulse_filename_clear = QtGui.QPushButton(self.centralwidget)
        self.T_Pulse_filename_clear.setObjectName(_fromUtf8("T_Pulse_filename_clear"))
        self._2.addWidget(self.T_Pulse_filename_clear, 0, 3, 1, 1)
        self.T_Pulse_Carrier_label = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_Carrier_label.setObjectName(_fromUtf8("T_Pulse_Carrier_label"))
        self._2.addWidget(self.T_Pulse_Carrier_label, 3, 0, 1, 1)
        self.T_Pulse_carrier_clear_15 = QtGui.QPushButton(self.centralwidget)
        self.T_Pulse_carrier_clear_15.setObjectName(_fromUtf8("T_Pulse_carrier_clear_15"))
        self._2.addWidget(self.T_Pulse_carrier_clear_15, 4, 3, 1, 1)
        self.T_Pulse_Carrier_label_5 = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_Carrier_label_5.setObjectName(_fromUtf8("T_Pulse_Carrier_label_5"))
        self._2.addWidget(self.T_Pulse_Carrier_label_5, 4, 0, 1, 1)
        self.Mono_Pulse_name_input = QtGui.QLineEdit(self.centralwidget)
        self.Mono_Pulse_name_input.setObjectName(_fromUtf8("Mono_Pulse_name_input"))
        self._2.addWidget(self.Mono_Pulse_name_input, 4, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self._2.addWidget(self.label_3, 7, 2, 1, 1)
        self.Mono_wind_leng_input = QtGui.QLineEdit(self.centralwidget)
        self.Mono_wind_leng_input.setObjectName(_fromUtf8("Mono_wind_leng_input"))
        self._2.addWidget(self.Mono_wind_leng_input, 6, 1, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self._2.addWidget(self.label, 5, 2, 1, 1)
        self.T_Pulse_Carrier_label_6 = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_Carrier_label_6.setObjectName(_fromUtf8("T_Pulse_Carrier_label_6"))
        self._2.addWidget(self.T_Pulse_Carrier_label_6, 9, 0, 1, 1)
        self.Mono_add_btn = QtGui.QPushButton(self.centralwidget)
        self.Mono_add_btn.setObjectName(_fromUtf8("Mono_add_btn"))
        self._2.addWidget(self.Mono_add_btn, 8, 1, 1, 1)
        self.Mono_remove_btn = QtGui.QPushButton(self.centralwidget)
        self.Mono_remove_btn.setObjectName(_fromUtf8("Mono_remove_btn"))
        self._2.addWidget(self.Mono_remove_btn, 9, 3, 1, 1)
        self._2.setColumnStretch(0, 8)
        self.horizontalLayout3.addLayout(self._2)
        self.verticalLayout.addLayout(self.horizontalLayout3)
        self.Mono_Record_btn = QtGui.QPushButton(self.centralwidget)
        self.Mono_Record_btn.setObjectName(_fromUtf8("Mono_Record_btn"))
        self.verticalLayout.addWidget(self.Mono_Record_btn)
        Monostatics_2.setCentralWidget(self.centralwidget)

        self.retranslateUi(Monostatics_2)
        QtCore.QObject.connect(self.T_Pulse_filename_clear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Mono_name_input.clear)
        QtCore.QObject.connect(self.T_Pulse_power_clear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Mono_ant_name_input.clear)
        QtCore.QObject.connect(self.T_Pulse_carrier_clear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Mono_clk_name_input.clear)
        QtCore.QObject.connect(self.T_Pulse_carrier_clear_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Mono_wind_skip_input.clear)
        QtCore.QObject.connect(self.T_Pulse_carrier_clear_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Mono_wind_leng_input.clear)
        QtCore.QObject.connect(self.T_Pulse_carrier_clear_4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Mono_PRF_input.clear)
        QtCore.QObject.connect(self.T_Pulse_carrier_clear_15, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Mono_Pulse_name_input.clear)
        QtCore.QMetaObject.connectSlotsByName(Monostatics_2)
        Monostatics_2.setTabOrder(self.Mono_name_input, self.checkBox)
        Monostatics_2.setTabOrder(self.checkBox, self.checkBox_2)
        Monostatics_2.setTabOrder(self.checkBox_2, self.Mono_ant_name_input)
        Monostatics_2.setTabOrder(self.Mono_ant_name_input, self.Mono_clk_name_input)
        Monostatics_2.setTabOrder(self.Mono_clk_name_input, self.Mono_Pulse_name_input)
        Monostatics_2.setTabOrder(self.Mono_Pulse_name_input, self.Mono_wind_skip_input)
        Monostatics_2.setTabOrder(self.Mono_wind_skip_input, self.Mono_wind_leng_input)
        Monostatics_2.setTabOrder(self.Mono_wind_leng_input, self.Mono_PRF_input)
        Monostatics_2.setTabOrder(self.Mono_PRF_input, self.Mono_add_btn)
        Monostatics_2.setTabOrder(self.Mono_add_btn, self.Mono_remove_btn)
        Monostatics_2.setTabOrder(self.Mono_remove_btn, self.Mono_Record_btn)
        Monostatics_2.setTabOrder(self.Mono_Record_btn, self.T_Pulse_filename_clear)
        Monostatics_2.setTabOrder(self.T_Pulse_filename_clear, self.T_Pulse_power_clear)
        Monostatics_2.setTabOrder(self.T_Pulse_power_clear, self.T_Pulse_carrier_clear)
        Monostatics_2.setTabOrder(self.T_Pulse_carrier_clear, self.T_Pulse_carrier_clear_15)
        Monostatics_2.setTabOrder(self.T_Pulse_carrier_clear_15, self.T_Pulse_carrier_clear_2)
        Monostatics_2.setTabOrder(self.T_Pulse_carrier_clear_2, self.T_Pulse_carrier_clear_3)
        Monostatics_2.setTabOrder(self.T_Pulse_carrier_clear_3, self.T_Pulse_carrier_clear_4)

    def retranslateUi(self, Monostatics_2):
        Monostatics_2.setWindowTitle(_translate("Monostatics_2", "Monostatics", None))
        self.Monostatics.setText(_translate("Monostatics_2", "Monostatics", None))
        self.label_2.setText(_translate("Monostatics_2", "seconds", None))
        self.T_Pulse_carrier_clear_3.setText(_translate("Monostatics_2", "Clear", None))
        self.T_Pulse_Carrier_label_3.setText(_translate("Monostatics_2", "Window Length", None))
        self.T_Pulse_carrier_clear.setText(_translate("Monostatics_2", "Clear", None))
        self.T_Pulse_carrier_clear_4.setText(_translate("Monostatics_2", "Clear", None))
        self.Mono_wind_skip_input.setPlaceholderText(_translate("Monostatics_2", "<Sample Value>", None))
        self.checkBox_2.setText(_translate("Monostatics_2", "Pulsed", None))
        self.Mono_clk_name_input.setPlaceholderText(_translate("Monostatics_2", "<Sample Name>", None))
        self.T_Pulse_Carrier_label_2.setText(_translate("Monostatics_2", "Window Skip", None))
        self.T_Pulse_Carrier_label_4.setText(_translate("Monostatics_2", "PRF", None))
        self.T_Pulse_carrier_clear_2.setText(_translate("Monostatics_2", "Clear", None))
        self.Mono_PRF_input.setPlaceholderText(_translate("Monostatics_2", "<Sample Value>", None))
        self.Mono_name_input.setPlaceholderText(_translate("Monostatics_2", "<Sample Name>", None))
        self.checkBox.setText(_translate("Monostatics_2", "Continuous", None))
        self.T_Pulse_file_label.setText(_translate("Monostatics_2", "Type", None))
        self.Mono_ant_name_input.setPlaceholderText(_translate("Monostatics_2", "<Sample Name>", None))
        self.T_Pulse_power_label.setText(_translate("Monostatics_2", "Antenna", None))
        self.T_Pulse_power_clear.setText(_translate("Monostatics_2", "Clear", None))
        self.T_Pulse_name_label.setText(_translate("Monostatics_2", "Name", None))
        self.T_Pulse_filename_clear.setText(_translate("Monostatics_2", "Clear", None))
        self.T_Pulse_Carrier_label.setText(_translate("Monostatics_2", "Clock Name", None))
        self.T_Pulse_carrier_clear_15.setText(_translate("Monostatics_2", "Clear", None))
        self.T_Pulse_Carrier_label_5.setText(_translate("Monostatics_2", "Pulse Name", None))
        self.Mono_Pulse_name_input.setPlaceholderText(_translate("Monostatics_2", "<Sample Name>", None))
        self.label_3.setText(_translate("Monostatics_2", "Hz", None))
        self.Mono_wind_leng_input.setPlaceholderText(_translate("Monostatics_2", "<Sample Value>", None))
        self.label.setText(_translate("Monostatics_2", "seconds", None))
        self.T_Pulse_Carrier_label_6.setText(_translate("Monostatics_2", "Remove existing Monostatics", None))
        self.Mono_add_btn.setText(_translate("Monostatics_2", "Add to XML", None))
        self.Mono_remove_btn.setText(_translate("Monostatics_2", "Remove from XML", None))
        self.Mono_Record_btn.setText(_translate("Monostatics_2", "View XML", None))

        ## connects functions to buttons
        self.Mono_add_btn.clicked.connect(self.callAppend)
        self.Mono_Record_btn.clicked.connect(self.showEntry)
        self.Mono_remove_btn.clicked.connect(self.removeNode)

        
    ## removes monostatic from simulation
    def removeNode(self):
        doc = etree.parse(filename, parser)
        sim = doc.getroot()
        tree=etree.ElementTree(sim)  
        for mono in sim.findall('monostatic'):
            sim.remove(mono)
            doc.write(filename,pretty_print=True)
            print '--Monostatic removed--'

    ## prints formatted xml to console
    def showEntry(self):
        doc = etree.parse(filename, parser)
        print(etree.tostring(doc, pretty_print=True))   

    ## adds monostatic to simulation
    def callAppend(self):
        mono_name = str(self.Mono_name_input.text())
        antenna_name = str(self.Mono_ant_name_input.text())
        pulse_name = str(self.Mono_Pulse_name_input.text())
        timing = str(self.Mono_clk_name_input.text())
        skip_time = str(self.Mono_wind_skip_input.text())
        rec_window_length = str(self.Mono_wind_leng_input.text())
        pulse_rf = str(self.Mono_PRF_input.text())
        if (self.checkBox_2.isChecked()):
            trans_type = 'pulsed'
        else:
            trans_type = 'continuous'        
        
        appendMonostatics(filename, mono_name, trans_type, antenna_name, pulse_name,timing, skip_time,rec_window_length,pulse_rf)
        print '--Monostatics added to simulation--'
        

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Monostatics_2 = QtGui.QMainWindow()
    ui = Ui_Monostatics_2()
    ui.setupUi(Monostatics_2)
    Monostatics_2.show()
    sys.exit(app.exec_())

