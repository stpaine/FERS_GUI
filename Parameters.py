# -- Parameters.py as part of FERS XML File I/O as part of FERS Plugin
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

class Ui_MainWindow(QtGui.QMainWindow):

    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(540, 343)
        self.centralwidget = QtGui.QWidget(MainWindow)
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
        self._2.setObjectName(_fromUtf8("_2"))
        self.Para_Interprate_input = QtGui.QLineEdit(self.centralwidget)
        self.Para_Interprate_input.setObjectName(_fromUtf8("Para_Interprate_input"))
        self._2.addWidget(self.Para_Interprate_input, 7, 1, 1, 1)
        self.T_Pulse_Carrier_label_2 = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_Carrier_label_2.setObjectName(_fromUtf8("T_Pulse_Carrier_label_2"))
        self._2.addWidget(self.T_Pulse_Carrier_label_2, 4, 0, 1, 1)
        self.T_Pulse_Carrier_label_3 = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_Carrier_label_3.setObjectName(_fromUtf8("T_Pulse_Carrier_label_3"))
        self._2.addWidget(self.T_Pulse_Carrier_label_3, 5, 0, 1, 1)
        self.T_Pulse_carrier_clear = QtGui.QPushButton(self.centralwidget)
        self.T_Pulse_carrier_clear.setObjectName(_fromUtf8("T_Pulse_carrier_clear"))
        self._2.addWidget(self.T_Pulse_carrier_clear, 3, 3, 1, 1)
        self.Para_Rand_seed_input = QtGui.QLineEdit(self.centralwidget)
        self.Para_Rand_seed_input.setObjectName(_fromUtf8("Para_Rand_seed_input"))
        self._2.addWidget(self.Para_Rand_seed_input, 5, 1, 1, 1)
        self.Para_SOL_input = QtGui.QLineEdit(self.centralwidget)
        self.Para_SOL_input.setObjectName(_fromUtf8("Para_SOL_input"))
        self._2.addWidget(self.Para_SOL_input, 2, 1, 1, 1)
        self.T_Pulse_file_label = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_file_label.setObjectName(_fromUtf8("T_Pulse_file_label"))
        self._2.addWidget(self.T_Pulse_file_label, 1, 0, 1, 1)
        self.Para_Start_time_input = QtGui.QLineEdit(self.centralwidget)
        self.Para_Start_time_input.setObjectName(_fromUtf8("Para_Start_time_input"))
        self._2.addWidget(self.Para_Start_time_input, 0, 1, 1, 1)
        self.T_Pulse_power_label = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_power_label.setObjectName(_fromUtf8("T_Pulse_power_label"))
        self._2.addWidget(self.T_Pulse_power_label, 2, 0, 1, 1)
        self.T_Pulse_name_label = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_name_label.setObjectName(_fromUtf8("T_Pulse_name_label"))
        self._2.addWidget(self.T_Pulse_name_label, 0, 0, 1, 1)
        self.T_Pulse_Carrier_label = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_Carrier_label.setObjectName(_fromUtf8("T_Pulse_Carrier_label"))
        self._2.addWidget(self.T_Pulse_Carrier_label, 3, 0, 1, 1)
        self.T_Pulse_carrier_clear_3 = QtGui.QPushButton(self.centralwidget)
        self.T_Pulse_carrier_clear_3.setObjectName(_fromUtf8("T_Pulse_carrier_clear_3"))
        self._2.addWidget(self.T_Pulse_carrier_clear_3, 5, 3, 1, 1)
        self.T_Pulse_filename_clear = QtGui.QPushButton(self.centralwidget)
        self.T_Pulse_filename_clear.setObjectName(_fromUtf8("T_Pulse_filename_clear"))
        self._2.addWidget(self.T_Pulse_filename_clear, 0, 3, 1, 1)
        self.T_Pulse_power_clear = QtGui.QPushButton(self.centralwidget)
        self.T_Pulse_power_clear.setObjectName(_fromUtf8("T_Pulse_power_clear"))
        self._2.addWidget(self.T_Pulse_power_clear, 2, 3, 1, 1)
        self.Para_Rate_input = QtGui.QLineEdit(self.centralwidget)
        self.Para_Rate_input.setObjectName(_fromUtf8("Para_Rate_input"))
        self._2.addWidget(self.Para_Rate_input, 3, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self._2.addWidget(self.label_3, 1, 2, 1, 1)
        self.Para_Export_CSV_sel = QtGui.QCheckBox(self.centralwidget)
        self.Para_Export_CSV_sel.setObjectName(_fromUtf8("Para_Export_CSV_sel"))
        self._2.addWidget(self.Para_Export_CSV_sel, 4, 2, 1, 1)
        self.Para_Export_Binary_sel = QtGui.QCheckBox(self.centralwidget)
        self.Para_Export_Binary_sel.setObjectName(_fromUtf8("Para_Export_Binary_sel"))
        self._2.addWidget(self.Para_Export_Binary_sel, 4, 1, 1, 1)
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self._2.addWidget(self.label_8, 5, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self._2.addWidget(self.label_2, 0, 2, 1, 1)
        self.Para_End_time_input = QtGui.QLineEdit(self.centralwidget)
        self.Para_End_time_input.setObjectName(_fromUtf8("Para_End_time_input"))
        self._2.addWidget(self.Para_End_time_input, 1, 1, 1, 1)
        self.T_Pulse_Carrier_label_5 = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_Carrier_label_5.setObjectName(_fromUtf8("T_Pulse_Carrier_label_5"))
        self._2.addWidget(self.T_Pulse_Carrier_label_5, 6, 0, 1, 1)
        self.T_Pulse_filename_clear_2 = QtGui.QPushButton(self.centralwidget)
        self.T_Pulse_filename_clear_2.setObjectName(_fromUtf8("T_Pulse_filename_clear_2"))
        self._2.addWidget(self.T_Pulse_filename_clear_2, 1, 3, 1, 1)
        self.T_Pulse_Carrier_label_6 = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_Carrier_label_6.setObjectName(_fromUtf8("T_Pulse_Carrier_label_6"))
        self._2.addWidget(self.T_Pulse_Carrier_label_6, 7, 0, 1, 1)
        self.T_Pulse_carrier_clear_10 = QtGui.QPushButton(self.centralwidget)
        self.T_Pulse_carrier_clear_10.setObjectName(_fromUtf8("T_Pulse_carrier_clear_10"))
        self._2.addWidget(self.T_Pulse_carrier_clear_10, 8, 3, 1, 1)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self._2.addWidget(self.label_4, 2, 2, 1, 1)
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self._2.addWidget(self.label_9, 3, 2, 1, 1)
        self.T_Pulse_carrier_clear_9 = QtGui.QPushButton(self.centralwidget)
        self.T_Pulse_carrier_clear_9.setObjectName(_fromUtf8("T_Pulse_carrier_clear_9"))
        self._2.addWidget(self.T_Pulse_carrier_clear_9, 7, 3, 1, 1)
        self.Para_ADC_input = QtGui.QLineEdit(self.centralwidget)
        self.Para_ADC_input.setObjectName(_fromUtf8("Para_ADC_input"))
        self._2.addWidget(self.Para_ADC_input, 6, 1, 1, 1)
        self.T_Pulse_carrier_clear_8 = QtGui.QPushButton(self.centralwidget)
        self.T_Pulse_carrier_clear_8.setObjectName(_fromUtf8("T_Pulse_carrier_clear_8"))
        self._2.addWidget(self.T_Pulse_carrier_clear_8, 6, 3, 1, 1)
        self.T_Pulse_Carrier_label_7 = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_Carrier_label_7.setObjectName(_fromUtf8("T_Pulse_Carrier_label_7"))
        self._2.addWidget(self.T_Pulse_Carrier_label_7, 8, 0, 1, 1)
        self.Para_Export_XML_sel = QtGui.QCheckBox(self.centralwidget)
        self.Para_Export_XML_sel.setObjectName(_fromUtf8("Para_Export_XML_sel"))
        self._2.addWidget(self.Para_Export_XML_sel, 4, 3, 1, 1)
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self._2.addWidget(self.label_6, 6, 2, 1, 1)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self._2.addWidget(self.label_5, 8, 2, 1, 1)
        self.Para_Osample_input = QtGui.QLineEdit(self.centralwidget)
        self.Para_Osample_input.setObjectName(_fromUtf8("Para_Osample_input"))
        self._2.addWidget(self.Para_Osample_input, 8, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self._2.addWidget(self.label_7, 9, 2, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.Para_Add_btn = QtGui.QPushButton(self.centralwidget)
        self.Para_Add_btn.setObjectName(_fromUtf8("Para_Add_btn"))
        self.horizontalLayout.addWidget(self.Para_Add_btn)
        self.Para_Remove_btn = QtGui.QPushButton(self.centralwidget)
        self.Para_Remove_btn.setObjectName(_fromUtf8("Para_Remove_btn"))
        self.horizontalLayout.addWidget(self.Para_Remove_btn)
        self._2.addLayout(self.horizontalLayout, 9, 1, 1, 1)
        self.Para_viewXML_btn = QtGui.QPushButton(self.centralwidget)
        self.Para_viewXML_btn.setObjectName(_fromUtf8("Para_viewXML_btn"))
        self._2.addWidget(self.Para_viewXML_btn, 9, 3, 1, 1)
        self._2.setColumnStretch(0, 8)
        self.horizontalLayout3.addLayout(self._2)
        self.verticalLayout.addLayout(self.horizontalLayout3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.T_Pulse_carrier_clear_10, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Para_Osample_input.clear)
        QtCore.QObject.connect(self.T_Pulse_carrier_clear_9, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Para_Interprate_input.clear)
        QtCore.QObject.connect(self.T_Pulse_carrier_clear_8, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Para_ADC_input.clear)
        QtCore.QObject.connect(self.T_Pulse_carrier_clear_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Para_Rand_seed_input.clear)
        QtCore.QObject.connect(self.T_Pulse_carrier_clear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Para_Rate_input.clear)
        QtCore.QObject.connect(self.T_Pulse_power_clear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Para_SOL_input.clear)
        QtCore.QObject.connect(self.T_Pulse_filename_clear_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Para_End_time_input.clear)
        QtCore.QObject.connect(self.T_Pulse_filename_clear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Para_Start_time_input.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.Para_Start_time_input, self.Para_End_time_input)
        MainWindow.setTabOrder(self.Para_End_time_input, self.Para_SOL_input)
        MainWindow.setTabOrder(self.Para_SOL_input, self.Para_Rate_input)
        MainWindow.setTabOrder(self.Para_Rate_input, self.Para_Export_Binary_sel)
        MainWindow.setTabOrder(self.Para_Export_Binary_sel, self.Para_Export_CSV_sel)
        MainWindow.setTabOrder(self.Para_Export_CSV_sel, self.Para_Export_XML_sel)
        MainWindow.setTabOrder(self.Para_Export_XML_sel, self.Para_Rand_seed_input)
        MainWindow.setTabOrder(self.Para_Rand_seed_input, self.Para_ADC_input)
        MainWindow.setTabOrder(self.Para_ADC_input, self.Para_Interprate_input)
        MainWindow.setTabOrder(self.Para_Interprate_input, self.Para_Osample_input)
        MainWindow.setTabOrder(self.Para_Osample_input, self.Para_Add_btn)
        MainWindow.setTabOrder(self.Para_Add_btn, self.Para_Remove_btn)
        MainWindow.setTabOrder(self.Para_Remove_btn, self.Para_viewXML_btn)
        MainWindow.setTabOrder(self.Para_viewXML_btn, self.T_Pulse_filename_clear)
        MainWindow.setTabOrder(self.T_Pulse_filename_clear, self.T_Pulse_filename_clear_2)
        MainWindow.setTabOrder(self.T_Pulse_filename_clear_2, self.T_Pulse_power_clear)
        MainWindow.setTabOrder(self.T_Pulse_power_clear, self.T_Pulse_carrier_clear)
        MainWindow.setTabOrder(self.T_Pulse_carrier_clear, self.T_Pulse_carrier_clear_3)
        MainWindow.setTabOrder(self.T_Pulse_carrier_clear_3, self.T_Pulse_carrier_clear_8)
        MainWindow.setTabOrder(self.T_Pulse_carrier_clear_8, self.T_Pulse_carrier_clear_9)
        MainWindow.setTabOrder(self.T_Pulse_carrier_clear_9, self.T_Pulse_carrier_clear_10)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Parameters", None))
        self.Monostatics.setText(_translate("MainWindow", "Parameters", None))
        self.Para_Interprate_input.setPlaceholderText(_translate("MainWindow", "<Sample Value>", None))
        self.T_Pulse_Carrier_label_2.setText(_translate("MainWindow", "Export Type", None))
        self.T_Pulse_Carrier_label_3.setText(_translate("MainWindow", "Random Seed", None))
        self.T_Pulse_carrier_clear.setText(_translate("MainWindow", "Clear", None))
        self.Para_Rand_seed_input.setPlaceholderText(_translate("MainWindow", "<Sample Value>", None))
        self.Para_SOL_input.setPlaceholderText(_translate("MainWindow", "<c=299792458>", None))
        self.T_Pulse_file_label.setText(_translate("MainWindow", "End Time", None))
        self.Para_Start_time_input.setPlaceholderText(_translate("MainWindow", "<Sample Time>", None))
        self.T_Pulse_power_label.setText(_translate("MainWindow", "Speed of light", None))
        self.T_Pulse_name_label.setText(_translate("MainWindow", "Start Time", None))
        self.T_Pulse_Carrier_label.setText(_translate("MainWindow", "Export Sampling Rate", None))
        self.T_Pulse_carrier_clear_3.setText(_translate("MainWindow", "Clear", None))
        self.T_Pulse_filename_clear.setText(_translate("MainWindow", "Clear", None))
        self.T_Pulse_power_clear.setText(_translate("MainWindow", "Clear", None))
        self.Para_Rate_input.setPlaceholderText(_translate("MainWindow", "<Sample Value>", None))
        self.label_3.setText(_translate("MainWindow", "Seconds", None))
        self.Para_Export_CSV_sel.setText(_translate("MainWindow", "CSV", None))
        self.Para_Export_Binary_sel.setText(_translate("MainWindow", "Binary", None))
        self.label_8.setText(_translate("MainWindow", "unit", None))
        self.label_2.setText(_translate("MainWindow", "Seconds", None))
        self.Para_End_time_input.setPlaceholderText(_translate("MainWindow", "<Sample Time>", None))
        self.T_Pulse_Carrier_label_5.setText(_translate("MainWindow", "ADC Bits", None))
        self.T_Pulse_filename_clear_2.setText(_translate("MainWindow", "Clear", None))
        self.T_Pulse_Carrier_label_6.setText(_translate("MainWindow", "Interpolation rate", None))
        self.T_Pulse_carrier_clear_10.setText(_translate("MainWindow", "Clear", None))
        self.label_4.setText(_translate("MainWindow", "m/s", None))
        self.label_9.setText(_translate("MainWindow", "Hz", None))
        self.T_Pulse_carrier_clear_9.setText(_translate("MainWindow", "Clear", None))
        self.Para_ADC_input.setPlaceholderText(_translate("MainWindow", "<Sample Value>", None))
        self.T_Pulse_carrier_clear_8.setText(_translate("MainWindow", "Clear", None))
        self.T_Pulse_Carrier_label_7.setText(_translate("MainWindow", "Oversample", None))
        self.Para_Export_XML_sel.setText(_translate("MainWindow", "XML", None))
        self.label_6.setText(_translate("MainWindow", "bits", None))
        self.label_5.setText(_translate("MainWindow", "unit", None))
        self.Para_Osample_input.setPlaceholderText(_translate("MainWindow", "<Sample Value>", None))
        self.label_7.setText(_translate("MainWindow", "from XML", None))
        self.Para_Add_btn.setText(_translate("MainWindow", "Add", None))
        self.Para_Remove_btn.setText(_translate("MainWindow", "Remove", None))
        self.Para_viewXML_btn.setText(_translate("MainWindow", "View XML", None))
        
        ## connects functions to buttons
        self.Para_Add_btn.clicked.connect(self.callAppend)
        self.Para_viewXML_btn.clicked.connect(self.showEntry)
        self.Para_Remove_btn.clicked.connect(self.removeNode)
        
    ## removes parameters from simulation
    def removeNode(self):
        doc = etree.parse(filename, parser)
        sim = doc.getroot()
        for parameter in sim.findall('parameters'):
            sim.remove(parameter)
            doc.write(filename,pretty_print=True)
        print '--Parameter Removed--'
            
    ## prints formatted xml to console      
    def showEntry(self):
        doc = etree.parse(filename, parser)
        print(etree.tostring(doc, pretty_print=True))        
            
    ## adds parameters to simulation
    def callAppend(self):
        interp = str(self.Para_Interprate_input.text())
        randseed = str(self.Para_Rand_seed_input.text())
        SOL = str(self.Para_SOL_input.text())
        if SOL == '':
            SOL = '299792458'
        else:
            SOL = str(self.Para_SOL_input.text())
        start = str(self.Para_Start_time_input.text())
        end = str(self.Para_End_time_input.text())
        rate = str(self.Para_Rate_input.text())
        Orate = str(self.Para_Osample_input.text())
        ADC = str(self.Para_ADC_input.text())
        csv = 'false'
        binary = 'false'
        xml = 'false'        
        if (self.Para_Export_CSV_sel.isChecked()):
            csv = 'true'
        elif (self.Para_Export_Binary_sel.isChecked()):
            binary = 'true'
        elif (self.Para_Export_XML_sel.isChecked()):
            xml = 'true' 
        else:
            print'--Please select relevant export format--'
            
        
        appendParameters(filename, start, end, SOL, rate, csv,binary, xml, interp,randseed, ADC,Orate)
        print'--Parameters Added--'


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

