# -- FERS_Input.py as part of FERS XML File I/O as part of FERS Plugin
# -- Created by James Gripper 
# -- November 2016
# -*- coding: utf-8 -*-#

from PyQt4 import QtCore, QtGui
from addNodes import *
from lxml import etree
import sys
import os

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

class Ui_FERS_Input(object):
        
    def setupUi(self, FERS_Input):
        FERS_Input.setObjectName(_fromUtf8("FERS_Input"))
        FERS_Input.resize(450, 430)
        self.horizontalLayout_3 = QtGui.QHBoxLayout(FERS_Input)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.FERS_Input_2 = QtGui.QLabel(FERS_Input)
        self.FERS_Input_2.setBaseSize(QtCore.QSize(7, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.FERS_Input_2.setFont(font)
        self.FERS_Input_2.setObjectName(_fromUtf8("FERS_Input_2"))
        self.verticalLayout_2.addWidget(self.FERS_Input_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label = QtGui.QLabel(FERS_Input)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 3, 0, 1, 1)
        self.T_Pulse_filename_clear_4 = QtGui.QPushButton(FERS_Input)
        self.T_Pulse_filename_clear_4.setObjectName(_fromUtf8("T_Pulse_filename_clear_4"))
        self.gridLayout_2.addWidget(self.T_Pulse_filename_clear_4, 2, 2, 1, 1)
        self.T_Pulse_filename_clear_3 = QtGui.QPushButton(FERS_Input)
        self.T_Pulse_filename_clear_3.setObjectName(_fromUtf8("T_Pulse_filename_clear_3"))
        self.gridLayout_2.addWidget(self.T_Pulse_filename_clear_3, 3, 2, 1, 1)
        self.FERS_Next_1 = QtGui.QPushButton(FERS_Input)
        self.FERS_Next_1.setObjectName(_fromUtf8("FERS_Next_1"))
        self.gridLayout_2.addWidget(self.FERS_Next_1, 3, 3, 1, 1)
        self.Filename_input = QtGui.QLineEdit(FERS_Input)
        self.Filename_input.setObjectName(_fromUtf8("Filename_input"))
        self.gridLayout_2.addWidget(self.Filename_input, 2, 1, 1, 1)
        self.Filename_set_btn = QtGui.QPushButton(FERS_Input)
        self.Filename_set_btn.setObjectName(_fromUtf8("Filename_set_btn"))
        self.gridLayout_2.addWidget(self.Filename_set_btn, 2, 3, 1, 1)
        self.label_2 = QtGui.QLabel(FERS_Input)
        self.label_2.setToolTip(_fromUtf8(""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)
        self.Simulation_name_input = QtGui.QLineEdit(FERS_Input)
        self.Simulation_name_input.setObjectName(_fromUtf8("Simulation_name_input"))
        self.gridLayout_2.addWidget(self.Simulation_name_input, 3, 1, 1, 1)
        self.New_Filename_input = QtGui.QLineEdit(FERS_Input)
        self.New_Filename_input.setObjectName(_fromUtf8("New_Filename_input"))
        self.gridLayout_2.addWidget(self.New_Filename_input, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(FERS_Input)
        self.label_3.setToolTip(_fromUtf8(""))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.T_Pulse_filename_clear_5 = QtGui.QPushButton(FERS_Input)
        self.T_Pulse_filename_clear_5.setObjectName(_fromUtf8("T_Pulse_filename_clear_5"))
        self.gridLayout_2.addWidget(self.T_Pulse_filename_clear_5, 1, 2, 1, 1)
        self.Create_file_btn = QtGui.QPushButton(FERS_Input)
        self.Create_file_btn.setObjectName(_fromUtf8("Create_file_btn"))
        self.gridLayout_2.addWidget(self.Create_file_btn, 1, 3, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self._2 = QtGui.QGridLayout()
        self._2.setObjectName(_fromUtf8("_2"))
        self.T_Pulse_name_label = QtGui.QLabel(FERS_Input)
        self.T_Pulse_name_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.T_Pulse_name_label.setObjectName(_fromUtf8("T_Pulse_name_label"))
        self._2.addWidget(self.T_Pulse_name_label, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.View_xml_btn = QtGui.QPushButton(FERS_Input)
        self.View_xml_btn.setObjectName(_fromUtf8("View_xml_btn"))
        self.horizontalLayout_2.addWidget(self.View_xml_btn)
        self._2.addLayout(self.horizontalLayout_2, 11, 0, 1, 1)
        self.T_Pulse_Carrier_label = QtGui.QLabel(FERS_Input)
        self.T_Pulse_Carrier_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.T_Pulse_Carrier_label.setObjectName(_fromUtf8("T_Pulse_Carrier_label"))
        self._2.addWidget(self.T_Pulse_Carrier_label, 7, 0, 1, 1)
        self.T_Pulse_Carrier_label_2 = QtGui.QLabel(FERS_Input)
        self.T_Pulse_Carrier_label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.T_Pulse_Carrier_label_2.setObjectName(_fromUtf8("T_Pulse_Carrier_label_2"))
        self._2.addWidget(self.T_Pulse_Carrier_label_2, 8, 0, 1, 1)
        self.Main_Timing_add_btn = QtGui.QPushButton(FERS_Input)
        self.Main_Timing_add_btn.setObjectName(_fromUtf8("Main_Timing_add_btn"))
        self._2.addWidget(self.Main_Timing_add_btn, 3, 2, 1, 1)
        self.Main_Tx_add_btn_2 = QtGui.QPushButton(FERS_Input)
        self.Main_Tx_add_btn_2.setObjectName(_fromUtf8("Main_Tx_add_btn_2"))
        self._2.addWidget(self.Main_Tx_add_btn_2, 9, 2, 1, 1)
        self.Main_Tx_add_btn_3 = QtGui.QPushButton(FERS_Input)
        self.Main_Tx_add_btn_3.setObjectName(_fromUtf8("Main_Tx_add_btn_3"))
        self._2.addWidget(self.Main_Tx_add_btn_3, 10, 2, 1, 1)
        self.T_Pulse_Carrier_label_3 = QtGui.QLabel(FERS_Input)
        self.T_Pulse_Carrier_label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.T_Pulse_Carrier_label_3.setObjectName(_fromUtf8("T_Pulse_Carrier_label_3"))
        self._2.addWidget(self.T_Pulse_Carrier_label_3, 3, 0, 1, 1)
        self.T_Pulse_Carrier_label_5 = QtGui.QLabel(FERS_Input)
        self.T_Pulse_Carrier_label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.T_Pulse_Carrier_label_5.setObjectName(_fromUtf8("T_Pulse_Carrier_label_5"))
        self._2.addWidget(self.T_Pulse_Carrier_label_5, 9, 0, 1, 1)
        self.T_Pulse_Carrier_label_6 = QtGui.QLabel(FERS_Input)
        self.T_Pulse_Carrier_label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.T_Pulse_Carrier_label_6.setObjectName(_fromUtf8("T_Pulse_Carrier_label_6"))
        self._2.addWidget(self.T_Pulse_Carrier_label_6, 10, 0, 1, 1)
        self.Main_Para_add_btn = QtGui.QPushButton(FERS_Input)
        self.Main_Para_add_btn.setObjectName(_fromUtf8("Main_Para_add_btn"))
        self._2.addWidget(self.Main_Para_add_btn, 0, 2, 1, 1)
        self.Main_TPulse_add_btn = QtGui.QPushButton(FERS_Input)
        self.Main_TPulse_add_btn.setObjectName(_fromUtf8("Main_TPulse_add_btn"))
        self._2.addWidget(self.Main_TPulse_add_btn, 1, 2, 1, 1)
        self.Main_Tx_add_btn = QtGui.QPushButton(FERS_Input)
        self.Main_Tx_add_btn.setObjectName(_fromUtf8("Main_Tx_add_btn"))
        self._2.addWidget(self.Main_Tx_add_btn, 8, 2, 1, 1)
        self.T_Pulse_file_label = QtGui.QLabel(FERS_Input)
        self.T_Pulse_file_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.T_Pulse_file_label.setObjectName(_fromUtf8("T_Pulse_file_label"))
        self._2.addWidget(self.T_Pulse_file_label, 1, 0, 1, 1)
        self.T_Pulse_power_label = QtGui.QLabel(FERS_Input)
        self.T_Pulse_power_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.T_Pulse_power_label.setObjectName(_fromUtf8("T_Pulse_power_label"))
        self._2.addWidget(self.T_Pulse_power_label, 5, 0, 1, 1)
        self.Main_Rx_add_btn = QtGui.QPushButton(FERS_Input)
        self.Main_Rx_add_btn.setObjectName(_fromUtf8("Main_Rx_add_btn"))
        self._2.addWidget(self.Main_Rx_add_btn, 7, 2, 1, 1)
        self.Main_Plat_add_btn = QtGui.QPushButton(FERS_Input)
        self.Main_Plat_add_btn.setObjectName(_fromUtf8("Main_Plat_add_btn"))
        self._2.addWidget(self.Main_Plat_add_btn, 5, 2, 1, 1)
        self.T_Pulse_Carrier_label_4 = QtGui.QLabel(FERS_Input)
        self.T_Pulse_Carrier_label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.T_Pulse_Carrier_label_4.setObjectName(_fromUtf8("T_Pulse_Carrier_label_4"))
        self._2.addWidget(self.T_Pulse_Carrier_label_4, 4, 0, 1, 1)
        self.Main_Ant_add_btn_2 = QtGui.QPushButton(FERS_Input)
        self.Main_Ant_add_btn_2.setObjectName(_fromUtf8("Main_Ant_add_btn_2"))
        self._2.addWidget(self.Main_Ant_add_btn_2, 4, 2, 1, 1)
        self._2.setColumnStretch(0, 8)
        self.gridLayout.addLayout(self._2, 0, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.retranslateUi(FERS_Input)
        QtCore.QObject.connect(self.T_Pulse_filename_clear_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Simulation_name_input.clear)
        QtCore.QObject.connect(self.T_Pulse_filename_clear_4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Filename_input.clear)
        QtCore.QObject.connect(self.T_Pulse_filename_clear_5, QtCore.SIGNAL(_fromUtf8("clicked()")), self.New_Filename_input.clear)
        QtCore.QMetaObject.connectSlotsByName(FERS_Input)
        FERS_Input.setTabOrder(self.New_Filename_input, self.T_Pulse_filename_clear_5)
        FERS_Input.setTabOrder(self.T_Pulse_filename_clear_5, self.Create_file_btn)
        FERS_Input.setTabOrder(self.Create_file_btn, self.Filename_input)
        FERS_Input.setTabOrder(self.Filename_input, self.T_Pulse_filename_clear_4)
        FERS_Input.setTabOrder(self.T_Pulse_filename_clear_4, self.Filename_set_btn)
        FERS_Input.setTabOrder(self.Filename_set_btn, self.Simulation_name_input)
        FERS_Input.setTabOrder(self.Simulation_name_input, self.T_Pulse_filename_clear_3)
        FERS_Input.setTabOrder(self.T_Pulse_filename_clear_3, self.FERS_Next_1)
        FERS_Input.setTabOrder(self.FERS_Next_1, self.Main_Para_add_btn)
        FERS_Input.setTabOrder(self.Main_Para_add_btn, self.Main_TPulse_add_btn)
        FERS_Input.setTabOrder(self.Main_TPulse_add_btn, self.Main_Timing_add_btn)
        FERS_Input.setTabOrder(self.Main_Timing_add_btn, self.Main_Ant_add_btn_2)
        FERS_Input.setTabOrder(self.Main_Ant_add_btn_2, self.Main_Plat_add_btn)
        FERS_Input.setTabOrder(self.Main_Plat_add_btn, self.Main_Rx_add_btn)
        FERS_Input.setTabOrder(self.Main_Rx_add_btn, self.Main_Tx_add_btn)
        FERS_Input.setTabOrder(self.Main_Tx_add_btn, self.Main_Tx_add_btn_2)
        FERS_Input.setTabOrder(self.Main_Tx_add_btn_2, self.Main_Tx_add_btn_3)
        FERS_Input.setTabOrder(self.Main_Tx_add_btn_3, self.View_xml_btn)

    def retranslateUi(self, FERS_Input):
        FERS_Input.setWindowTitle(_translate("FERS_Input", "FERS_Input", None))
        self.FERS_Input_2.setText(_translate("FERS_Input", "FERS XML File Management", None))
        self.label.setText(_translate("FERS_Input", "Simulation Name", None))
        self.T_Pulse_filename_clear_4.setText(_translate("FERS_Input", "Clear", None))
        self.T_Pulse_filename_clear_3.setText(_translate("FERS_Input", "Clear", None))
        self.FERS_Next_1.setText(_translate("FERS_Input", "Set", None))
        self.Filename_input.setPlaceholderText(_translate("FERS_Input", "<Sample name>", None))
        self.Filename_set_btn.setText(_translate("FERS_Input", "Verify", None))
        self.label_2.setText(_translate("FERS_Input", "Existing File Name", None))
        self.Simulation_name_input.setPlaceholderText(_translate("FERS_Input", "<Sample name>", None))
        self.New_Filename_input.setPlaceholderText(_translate("FERS_Input", "<Sample name>", None))
        self.label_3.setText(_translate("FERS_Input", "New File", None))
        self.T_Pulse_filename_clear_5.setText(_translate("FERS_Input", "Clear", None))
        self.Create_file_btn.setText(_translate("FERS_Input", "Create", None))
        self.T_Pulse_name_label.setText(_translate("FERS_Input", "Parameters", None))
        self.View_xml_btn.setText(_translate("FERS_Input", "View XML", None))
        self.T_Pulse_Carrier_label.setText(_translate("FERS_Input", "Receiver", None))
        self.T_Pulse_Carrier_label_2.setText(_translate("FERS_Input", "Transmitter", None))
        self.Main_Timing_add_btn.setText(_translate("FERS_Input", "Manage", None))
        self.Main_Tx_add_btn_2.setText(_translate("FERS_Input", "Manage", None))
        self.Main_Tx_add_btn_3.setText(_translate("FERS_Input", "Manage", None))
        self.T_Pulse_Carrier_label_3.setText(_translate("FERS_Input", "Timing", None))
        self.T_Pulse_Carrier_label_5.setText(_translate("FERS_Input", "Monostatics", None))
        self.T_Pulse_Carrier_label_6.setText(_translate("FERS_Input", "Multipath Surfaces", None))
        self.Main_Para_add_btn.setText(_translate("FERS_Input", "Manage", None))
        self.Main_TPulse_add_btn.setText(_translate("FERS_Input", "Manage", None))
        self.Main_Tx_add_btn.setText(_translate("FERS_Input", "Manage", None))
        self.T_Pulse_file_label.setText(_translate("FERS_Input", "Transmission Pulse", None))
        self.T_Pulse_power_label.setText(_translate("FERS_Input", "Platform", None))
        self.Main_Rx_add_btn.setText(_translate("FERS_Input", "Manage", None))
        self.Main_Plat_add_btn.setText(_translate("FERS_Input", "Manage", None))
        self.T_Pulse_Carrier_label_4.setText(_translate("FERS_Input", "Antenna", None))
        self.Main_Ant_add_btn_2.setText(_translate("FERS_Input", "Manage", None))

        self.View_xml_btn.clicked.connect(self.showEntry)
        self.Main_Para_add_btn.clicked.connect(self.addP)
        self.Main_TPulse_add_btn.clicked.connect(self.addTP)
        self.Main_Timing_add_btn.clicked.connect(self.addTiming)
        self.Main_Plat_add_btn.clicked.connect(self.addPlatform)
        self.Main_Ant_add_btn_2.clicked.connect(self.addAnt)
        self.Main_Tx_add_btn.clicked.connect(self.addTx)
        self.Main_Rx_add_btn.clicked.connect(self.addRx)
        self.Filename_set_btn.clicked.connect(self.Verify)
        self.Filename_set_btn.clicked.connect(self.getFilename)
        self.FERS_Next_1.clicked.connect(self.renameSim)
        self.Main_Tx_add_btn_2.clicked.connect(self.addMono)
        self.Main_Tx_add_btn_3.clicked.connect(self.addMulti)
        self.Create_file_btn.clicked.connect(self.CreateFile)
                
        
    def getFilename(self):
        filename = str(self.Filename_input.text())
        placeholder = open("filename.txt", "w")
        placeholder.write(filename)      
        placeholder.close()     
        
    def CreateFile(self):
        name = str(self.New_Filename_input.text())
        sim = etree.Element('simulation',{'name':''})
        tree = etree.ElementTree(sim) ## tree object
        outFile = open(name, 'w')
        tree.write(outFile, xml_declaration=True, pretty_print=True)         
        print '--File Created--'
                
    def addP(self):
        os.system('Parameters.py')
    
    def addTP(self):
        os.system('T_Pulse.py')
    
    def addTiming(self):
        os.system('Clocks.py') 
    
    def addPlatform(self):
        os.system('Platform.py')
    
    def addAnt(self):
        os.system('Antennas.py')  
    
    def addTx(self):
        os.system('Transmitter.py')
    
    def addRx(self):
        os.system('Receiver.py') 

    def addMono(self):
        os.system('Monostatics.py') 
        
    def addMulti(self):
        os.system('Multipath_Surfaces.py')        
    
    ## checks that filename entered is a properly formatted xml that the program can handle
    def Verify(self):
        filename = str(self.Filename_input.text())
        print '--Filename entered: '+filename
        try: 
            doc = etree.parse(filename, parser)
        except:
            print '--Error in characters in xml--'  
        try:
            doc = etree.parse(filename, parser)
            print '--Filename Correct--'
        except:
            print '--Filename incorrect. Please try again--'
    
    ## displays formatted xml on console
    def showEntry(self):
        try:
            filename = str(self.Filename_input.text())
            doc = etree.parse(filename, parser)
            print etree.tostring(doc, pretty_print=True)       
        except:
            print '--Please enter filename--'

    ## renames simulation 
    def renameSim(self):
        filename = str(self.Filename_input.text())
        name =  str(self.Simulation_name_input.text())
        if name == '':
            print'--Please fill in simulation name--'
        else:
            renameSimulation(name, filename)



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    FERS_Input = QtGui.QWidget()
    ui = Ui_FERS_Input()
    ui.setupUi(FERS_Input)
    FERS_Input.show()
    sys.exit(app.exec_())

