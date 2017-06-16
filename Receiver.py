# -- Receiver.py as part of FERS XML File I/O as part of FERS Plugin
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

class Ui_Receiver(QtGui.QMainWindow):

    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        
        
    def setupUi(self, Receiver):
        Receiver.setObjectName(_fromUtf8("Receiver"))
        Receiver.resize(541, 377)
        self.centralwidget = QtGui.QWidget(Receiver)
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
        self.Rx_ad_btn = QtGui.QPushButton(self.centralwidget)
        self.Rx_ad_btn.setObjectName(_fromUtf8("Rx_ad_btn"))
        self._2.addWidget(self.Rx_ad_btn, 9, 1, 1, 1)
        self.propcheck = QtGui.QCheckBox(self.centralwidget)
        self.propcheck.setText(_fromUtf8(""))
        self.propcheck.setObjectName(_fromUtf8("propcheck"))
        self._2.addWidget(self.propcheck, 7, 1, 1, 1)
        self.T_Pulse_Carrier_label_5 = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_Carrier_label_5.setObjectName(_fromUtf8("T_Pulse_Carrier_label_5"))
        self._2.addWidget(self.T_Pulse_Carrier_label_5, 8, 0, 1, 1)
        self.T_Pulse_Carrier_label_4 = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_Carrier_label_4.setObjectName(_fromUtf8("T_Pulse_Carrier_label_4"))
        self._2.addWidget(self.T_Pulse_Carrier_label_4, 10, 0, 1, 1)
        self.T_Pulse_power_label = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_power_label.setObjectName(_fromUtf8("T_Pulse_power_label"))
        self._2.addWidget(self.T_Pulse_power_label, 4, 0, 1, 1)
        self.T_Pulse_name_label = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_name_label.setObjectName(_fromUtf8("T_Pulse_name_label"))
        self._2.addWidget(self.T_Pulse_name_label, 0, 0, 1, 1)
        self.T_Pulse_file_label = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_file_label.setObjectName(_fromUtf8("T_Pulse_file_label"))
        self._2.addWidget(self.T_Pulse_file_label, 3, 0, 1, 1)
        self.Rx_name_input = QtGui.QLineEdit(self.centralwidget)
        self.Rx_name_input.setObjectName(_fromUtf8("Rx_name_input"))
        self._2.addWidget(self.Rx_name_input, 0, 1, 1, 1)
        self.T_Pulse_filename_clear_3 = QtGui.QPushButton(self.centralwidget)
        self.T_Pulse_filename_clear_3.setObjectName(_fromUtf8("T_Pulse_filename_clear_3"))
        self._2.addWidget(self.T_Pulse_filename_clear_3, 1, 3, 1, 1)
        self.Rx_Antenna_name_input = QtGui.QLineEdit(self.centralwidget)
        self.Rx_Antenna_name_input.setObjectName(_fromUtf8("Rx_Antenna_name_input"))
        self._2.addWidget(self.Rx_Antenna_name_input, 1, 1, 1, 1)
        self.Rx_window_leng_input = QtGui.QLineEdit(self.centralwidget)
        self.Rx_window_leng_input.setObjectName(_fromUtf8("Rx_window_leng_input"))
        self._2.addWidget(self.Rx_window_leng_input, 4, 1, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self._2.addWidget(self.label, 6, 2, 1, 1)
        self.T_Pulse_name_label_4 = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_name_label_4.setObjectName(_fromUtf8("T_Pulse_name_label_4"))
        self._2.addWidget(self.T_Pulse_name_label_4, 2, 0, 1, 1)
        self.T_Pulse_Carrier_label_2 = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_Carrier_label_2.setObjectName(_fromUtf8("T_Pulse_Carrier_label_2"))
        self._2.addWidget(self.T_Pulse_Carrier_label_2, 6, 0, 1, 1)
        self.T_Pulse_Carrier_label = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_Carrier_label.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.T_Pulse_Carrier_label.setObjectName(_fromUtf8("T_Pulse_Carrier_label"))
        self._2.addWidget(self.T_Pulse_Carrier_label, 5, 0, 1, 1)
        self.T_Pulse_name_clear = QtGui.QPushButton(self.centralwidget)
        self.T_Pulse_name_clear.setObjectName(_fromUtf8("T_Pulse_name_clear"))
        self._2.addWidget(self.T_Pulse_name_clear, 3, 3, 1, 1)
        self.Rx_PRF_input = QtGui.QLineEdit(self.centralwidget)
        self.Rx_PRF_input.setObjectName(_fromUtf8("Rx_PRF_input"))
        self._2.addWidget(self.Rx_PRF_input, 5, 1, 1, 1)
        self.T_Pulse_carrier_clear_2 = QtGui.QPushButton(self.centralwidget)
        self.T_Pulse_carrier_clear_2.setObjectName(_fromUtf8("T_Pulse_carrier_clear_2"))
        self._2.addWidget(self.T_Pulse_carrier_clear_2, 6, 3, 1, 1)
        self.Rx_Window_skip_input = QtGui.QLineEdit(self.centralwidget)
        self.Rx_Window_skip_input.setEnabled(True)
        self.Rx_Window_skip_input.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.Rx_Window_skip_input.setObjectName(_fromUtf8("Rx_Window_skip_input"))
        self._2.addWidget(self.Rx_Window_skip_input, 3, 1, 1, 1)
        self.T_Pulse_filename_clear_4 = QtGui.QPushButton(self.centralwidget)
        self.T_Pulse_filename_clear_4.setObjectName(_fromUtf8("T_Pulse_filename_clear_4"))
        self._2.addWidget(self.T_Pulse_filename_clear_4, 2, 3, 1, 1)
        self.T_Pulse_name_label_3 = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_name_label_3.setObjectName(_fromUtf8("T_Pulse_name_label_3"))
        self._2.addWidget(self.T_Pulse_name_label_3, 1, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self._2.addWidget(self.label_2, 3, 2, 1, 1)
        self.T_Pulse_filename_clear = QtGui.QPushButton(self.centralwidget)
        self.T_Pulse_filename_clear.setObjectName(_fromUtf8("T_Pulse_filename_clear"))
        self._2.addWidget(self.T_Pulse_filename_clear, 0, 3, 1, 1)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self._2.addWidget(self.label_3, 4, 2, 1, 1)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self._2.addWidget(self.label_4, 5, 2, 1, 1)
        self.Rx_Timing_name_input = QtGui.QLineEdit(self.centralwidget)
        self.Rx_Timing_name_input.setObjectName(_fromUtf8("Rx_Timing_name_input"))
        self._2.addWidget(self.Rx_Timing_name_input, 2, 1, 1, 1)
        self.T_Pulse_carrier_clear = QtGui.QPushButton(self.centralwidget)
        self.T_Pulse_carrier_clear.setObjectName(_fromUtf8("T_Pulse_carrier_clear"))
        self._2.addWidget(self.T_Pulse_carrier_clear, 5, 3, 1, 1)
        self.T_Pulse_power_clear = QtGui.QPushButton(self.centralwidget)
        self.T_Pulse_power_clear.setObjectName(_fromUtf8("T_Pulse_power_clear"))
        self._2.addWidget(self.T_Pulse_power_clear, 4, 3, 1, 1)
        self.Rx_Noise_temp_input = QtGui.QLineEdit(self.centralwidget)
        self.Rx_Noise_temp_input.setObjectName(_fromUtf8("Rx_Noise_temp_input"))
        self._2.addWidget(self.Rx_Noise_temp_input, 6, 1, 1, 1)
        self.Rx_remove_input = QtGui.QLineEdit(self.centralwidget)
        self.Rx_remove_input.setObjectName(_fromUtf8("Rx_remove_input"))
        self._2.addWidget(self.Rx_remove_input, 10, 1, 1, 1)
        self.T_Pulse_carrier_clear_3 = QtGui.QPushButton(self.centralwidget)
        self.T_Pulse_carrier_clear_3.setObjectName(_fromUtf8("T_Pulse_carrier_clear_3"))
        self._2.addWidget(self.T_Pulse_carrier_clear_3, 10, 3, 1, 1)
        self.Rx_remove_btn = QtGui.QPushButton(self.centralwidget)
        self.Rx_remove_btn.setObjectName(_fromUtf8("Rx_remove_btn"))
        self._2.addWidget(self.Rx_remove_btn, 11, 1, 1, 1)
        self.ignorecheck = QtGui.QCheckBox(self.centralwidget)
        self.ignorecheck.setText(_fromUtf8(""))
        self.ignorecheck.setObjectName(_fromUtf8("ignorecheck"))
        self._2.addWidget(self.ignorecheck, 8, 1, 1, 1)
        self.T_Pulse_Carrier_label_3 = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_Carrier_label_3.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.T_Pulse_Carrier_label_3.setObjectName(_fromUtf8("T_Pulse_Carrier_label_3"))
        self._2.addWidget(self.T_Pulse_Carrier_label_3, 7, 0, 1, 1)
        self._2.setColumnStretch(0, 8)
        self.horizontalLayout3.addLayout(self._2)
        self.verticalLayout.addLayout(self.horizontalLayout3)
        self.Rx_view_btn = QtGui.QPushButton(self.centralwidget)
        self.Rx_view_btn.setObjectName(_fromUtf8("Rx_view_btn"))
        self.verticalLayout.addWidget(self.Rx_view_btn)
        Receiver.setCentralWidget(self.centralwidget)

        self.retranslateUi(Receiver)
        QtCore.QObject.connect(self.T_Pulse_filename_clear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Rx_name_input.clear)
        QtCore.QObject.connect(self.T_Pulse_name_clear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Rx_Window_skip_input.clear)
        QtCore.QObject.connect(self.T_Pulse_power_clear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Rx_window_leng_input.clear)
        QtCore.QObject.connect(self.T_Pulse_carrier_clear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Rx_PRF_input.clear)
        QtCore.QObject.connect(self.T_Pulse_carrier_clear_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Rx_Noise_temp_input.clear)
        QtCore.QObject.connect(self.T_Pulse_filename_clear_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Rx_Antenna_name_input.clear)
        QtCore.QObject.connect(self.T_Pulse_filename_clear_4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Rx_Timing_name_input.clear)
        QtCore.QObject.connect(self.T_Pulse_carrier_clear_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Rx_remove_input.clear)
        QtCore.QMetaObject.connectSlotsByName(Receiver)
        Receiver.setTabOrder(self.Rx_name_input, self.Rx_Antenna_name_input)
        Receiver.setTabOrder(self.Rx_Antenna_name_input, self.Rx_Timing_name_input)
        Receiver.setTabOrder(self.Rx_Timing_name_input, self.Rx_Window_skip_input)
        Receiver.setTabOrder(self.Rx_Window_skip_input, self.Rx_window_leng_input)
        Receiver.setTabOrder(self.Rx_window_leng_input, self.Rx_PRF_input)
        Receiver.setTabOrder(self.Rx_PRF_input, self.Rx_Noise_temp_input)
        Receiver.setTabOrder(self.Rx_Noise_temp_input, self.propcheck)
        Receiver.setTabOrder(self.propcheck, self.ignorecheck)
        Receiver.setTabOrder(self.ignorecheck, self.Rx_ad_btn)
        Receiver.setTabOrder(self.Rx_ad_btn, self.Rx_remove_input)
        Receiver.setTabOrder(self.Rx_remove_input, self.Rx_remove_btn)
        Receiver.setTabOrder(self.Rx_remove_btn, self.Rx_view_btn)
        Receiver.setTabOrder(self.Rx_view_btn, self.T_Pulse_filename_clear)
        Receiver.setTabOrder(self.T_Pulse_filename_clear, self.T_Pulse_filename_clear_3)
        Receiver.setTabOrder(self.T_Pulse_filename_clear_3, self.T_Pulse_filename_clear_4)
        Receiver.setTabOrder(self.T_Pulse_filename_clear_4, self.T_Pulse_name_clear)
        Receiver.setTabOrder(self.T_Pulse_name_clear, self.T_Pulse_power_clear)
        Receiver.setTabOrder(self.T_Pulse_power_clear, self.T_Pulse_carrier_clear)
        Receiver.setTabOrder(self.T_Pulse_carrier_clear, self.T_Pulse_carrier_clear_2)
        Receiver.setTabOrder(self.T_Pulse_carrier_clear_2, self.T_Pulse_carrier_clear_3)

    def retranslateUi(self, Receiver):
        Receiver.setWindowTitle(_translate("Receiver", "Receiver", None))
        self.T_Pulse_label.setText(_translate("Receiver", "Receiver", None))
        self.Rx_ad_btn.setText(_translate("Receiver", "Add to XML", None))
        self.T_Pulse_Carrier_label_5.setText(_translate("Receiver", "Ignore Direct Signals", None))
        self.T_Pulse_Carrier_label_4.setText(_translate("Receiver", "Remove existing receiver", None))
        self.T_Pulse_power_label.setText(_translate("Receiver", "Window Length", None))
        self.T_Pulse_name_label.setText(_translate("Receiver", "Name", None))
        self.T_Pulse_file_label.setText(_translate("Receiver", "Window Skip", None))
        self.Rx_name_input.setPlaceholderText(_translate("Receiver", "<Sample Name>", None))
        self.T_Pulse_filename_clear_3.setText(_translate("Receiver", "Clear", None))
        self.Rx_Antenna_name_input.setPlaceholderText(_translate("Receiver", "<Sample Name>", None))
        self.Rx_window_leng_input.setPlaceholderText(_translate("Receiver", "<Sample Value>", None))
        self.label.setText(_translate("Receiver", "Kelvin", None))
        self.T_Pulse_name_label_4.setText(_translate("Receiver", "Clock Name", None))
        self.T_Pulse_Carrier_label_2.setText(_translate("Receiver", "Noise Temperature", None))
        self.T_Pulse_Carrier_label.setToolTip(_translate("Receiver", "<html><head/><body><p>Values will be rounded down to the closest even number.</p></body></html>", None))
        self.T_Pulse_Carrier_label.setText(_translate("Receiver", "PRF", None))
        self.T_Pulse_name_clear.setText(_translate("Receiver", "Clear", None))
        self.Rx_PRF_input.setPlaceholderText(_translate("Receiver", "<Sample Value>", None))
        self.T_Pulse_carrier_clear_2.setText(_translate("Receiver", "Clear", None))
        self.Rx_Window_skip_input.setPlaceholderText(_translate("Receiver", "<Sample Value>", None))
        self.T_Pulse_filename_clear_4.setText(_translate("Receiver", "Clear", None))
        self.T_Pulse_name_label_3.setText(_translate("Receiver", "Antenna", None))
        self.label_2.setText(_translate("Receiver", "seconds", None))
        self.T_Pulse_filename_clear.setText(_translate("Receiver", "Clear", None))
        self.label_3.setText(_translate("Receiver", "seconds", None))
        self.label_4.setText(_translate("Receiver", "Hz", None))
        self.Rx_Timing_name_input.setPlaceholderText(_translate("Receiver", "<Sample Name>", None))
        self.T_Pulse_carrier_clear.setText(_translate("Receiver", "Clear", None))
        self.T_Pulse_power_clear.setText(_translate("Receiver", "Clear", None))
        self.Rx_Noise_temp_input.setPlaceholderText(_translate("Receiver", "<Sample Temp>", None))
        self.Rx_remove_input.setPlaceholderText(_translate("Receiver", "<Sample Name>", None))
        self.T_Pulse_carrier_clear_3.setText(_translate("Receiver", "Clear", None))
        self.Rx_remove_btn.setText(_translate("Receiver", "Remove from XML", None))
        self.T_Pulse_Carrier_label_3.setToolTip(_translate("Receiver", "<html><head/><body><p>true: propagation losses of received signal(s) will notbe taken into account</p></body></html>", None))
        self.T_Pulse_Carrier_label_3.setText(_translate("Receiver", "Ignore Propagation Loss", None))
        self.Rx_view_btn.setText(_translate("Receiver", "view XML", None))
 
        ## connects functions to buttons
        self.Rx_ad_btn.clicked.connect(self.callAppend)
        self.Rx_view_btn.clicked.connect(self.showEntry)
        self.Rx_remove_btn.clicked.connect(self.removeNode)  

    ## removes receiver from simulation
    def removeNode(self):
        doc = etree.parse(filename, parser)
        sim = doc.getroot()
        for rec in sim.findall('receiver'):
            name = rec.get('name')
            if name == str(self.Rx_remove_input.text()):            
                sim.remove(rec)
                doc.write(filename,pretty_print=False)
                print '--Receiver removed from Simulation--'
            else:
                print "--Receiver not found. Please Try Again--"

    ## prints formatted xml to console
    def showEntry(self):
        doc = etree.parse(filename, parser)
        print(etree.tostring(doc, pretty_print=True))                

    ## adds receiver to simulation
    def callAppend(self):
        name = str(self.Rx_name_input.text())
        antenna_name = str(self.Rx_Antenna_name_input.text())
        clock_name = str(self.Rx_Timing_name_input.text())       
        skip_time = str(self.Rx_Window_skip_input.text())
        receiver_window_length = str(self.Rx_window_leng_input.text())
        pulse_rf = str(self.Rx_PRF_input.text())
        receiver_temp = str(self.Rx_Noise_temp_input.text())

        nd_bool = 'false'
        noploss_bool  = 'false'        
        if (self.propcheck.isChecked()):
            noploss_bool = 'true'        
        if (self.ignorecheck.isChecked()):
            nd_bool = 'true'

        appendRx(filename, name, antenna_name, clock_name, nd_bool, noploss_bool, skip_time, receiver_window_length, pulse_rf, receiver_temp)
        print '--Receiver Added to Simulation--'             


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Receiver = QtGui.QMainWindow()
    ui = Ui_Receiver()
    ui.setupUi(Receiver)
    Receiver.show()
    sys.exit(app.exec_())

