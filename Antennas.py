# -- Antennas.py as part of FERS XML File I/O as part of FERS Plugin
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

class Ui_Antennas(QtGui.QMainWindow):

    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        
    def setupUi(self, Antennas):
        Antennas.setObjectName(_fromUtf8("Antennas"))
        Antennas.resize(781, 360)
        self.centralwidget = QtGui.QWidget(Antennas)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.horizontalLayout1 = QtGui.QHBoxLayout()
        self.horizontalLayout1.setObjectName(_fromUtf8("horizontalLayout1"))
        self.Clocks_label = QtGui.QLabel(self.centralwidget)
        self.Clocks_label.setWordWrap(True)
        self.Clocks_label.setObjectName(_fromUtf8("Clocks_label"))
        self.horizontalLayout1.addWidget(self.Clocks_label)
        self.gridLayout1 = QtGui.QGridLayout()
        self.gridLayout1.setObjectName(_fromUtf8("gridLayout1"))
        self.Antennas_gauss_elscale_input = QtGui.QLineEdit(self.centralwidget)
        self.Antennas_gauss_elscale_input.setObjectName(_fromUtf8("Antennas_gauss_elscale_input"))
        self.gridLayout1.addWidget(self.Antennas_gauss_elscale_input, 6, 3, 1, 1)
        self.Antennas_efficiency_input = QtGui.QLineEdit(self.centralwidget)
        self.Antennas_efficiency_input.setObjectName(_fromUtf8("Antennas_efficiency_input"))
        self.gridLayout1.addWidget(self.Antennas_efficiency_input, 1, 2, 1, 1)
        self.Antennas_sinc_beta_input = QtGui.QLineEdit(self.centralwidget)
        self.Antennas_sinc_beta_input.setObjectName(_fromUtf8("Antennas_sinc_beta_input"))
        self.gridLayout1.addWidget(self.Antennas_sinc_beta_input, 4, 3, 1, 1)
        self.Antennas_gauss_clear_btn = QtGui.QPushButton(self.centralwidget)
        self.Antennas_gauss_clear_btn.setObjectName(_fromUtf8("Antennas_gauss_clear_btn"))
        self.gridLayout1.addWidget(self.Antennas_gauss_clear_btn, 6, 5, 1, 1)
        self.Antennas_sinc_gamma_input = QtGui.QLineEdit(self.centralwidget)
        self.Antennas_sinc_gamma_input.setObjectName(_fromUtf8("Antennas_sinc_gamma_input"))
        self.gridLayout1.addWidget(self.Antennas_sinc_gamma_input, 4, 4, 1, 1)
        self.Iso_chkbx = QtGui.QCheckBox(self.centralwidget)
        self.Iso_chkbx.setObjectName(_fromUtf8("Iso_chkbx"))
        self.gridLayout1.addWidget(self.Iso_chkbx, 3, 1, 1, 1)
        self.Sinc_chkbx = QtGui.QCheckBox(self.centralwidget)
        self.Sinc_chkbx.setObjectName(_fromUtf8("Sinc_chkbx"))
        self.gridLayout1.addWidget(self.Sinc_chkbx, 4, 1, 1, 1)
        self.Para_chkbx = QtGui.QCheckBox(self.centralwidget)
        self.Para_chkbx.setObjectName(_fromUtf8("Para_chkbx"))
        self.gridLayout1.addWidget(self.Para_chkbx, 5, 1, 1, 1)
        self.Antennas_sinc_alpha_input = QtGui.QLineEdit(self.centralwidget)
        self.Antennas_sinc_alpha_input.setObjectName(_fromUtf8("Antennas_sinc_alpha_input"))
        self.gridLayout1.addWidget(self.Antennas_sinc_alpha_input, 4, 2, 1, 1)
        self.Gauss_Chkbx = QtGui.QCheckBox(self.centralwidget)
        self.Gauss_Chkbx.setObjectName(_fromUtf8("Gauss_Chkbx"))
        self.gridLayout1.addWidget(self.Gauss_Chkbx, 6, 1, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout1.addWidget(self.label, 5, 2, 1, 1)
        self.Clocks_name_label = QtGui.QLabel(self.centralwidget)
        self.Clocks_name_label.setObjectName(_fromUtf8("Clocks_name_label"))
        self.gridLayout1.addWidget(self.Clocks_name_label, 0, 0, 1, 1)
        self.Antennas_name_input = QtGui.QLineEdit(self.centralwidget)
        self.Antennas_name_input.setObjectName(_fromUtf8("Antennas_name_input"))
        self.gridLayout1.addWidget(self.Antennas_name_input, 0, 2, 1, 1)
        self.Tx_Z_Clear_btn_11 = QtGui.QPushButton(self.centralwidget)
        self.Tx_Z_Clear_btn_11.setObjectName(_fromUtf8("Tx_Z_Clear_btn_11"))
        self.gridLayout1.addWidget(self.Tx_Z_Clear_btn_11, 4, 5, 1, 1)
        self.Antennas_para_diam_input = QtGui.QLineEdit(self.centralwidget)
        self.Antennas_para_diam_input.setObjectName(_fromUtf8("Antennas_para_diam_input"))
        self.gridLayout1.addWidget(self.Antennas_para_diam_input, 5, 3, 1, 1)
        self.Tx_Z_Clear_btn_8 = QtGui.QPushButton(self.centralwidget)
        self.Tx_Z_Clear_btn_8.setObjectName(_fromUtf8("Tx_Z_Clear_btn_8"))
        self.gridLayout1.addWidget(self.Tx_Z_Clear_btn_8, 3, 5, 1, 1)
        self.Antennas_gauss_azscale_input = QtGui.QLineEdit(self.centralwidget)
        self.Antennas_gauss_azscale_input.setObjectName(_fromUtf8("Antennas_gauss_azscale_input"))
        self.gridLayout1.addWidget(self.Antennas_gauss_azscale_input, 6, 2, 1, 1)
        self.Tx_Z_Val_label = QtGui.QLabel(self.centralwidget)
        self.Tx_Z_Val_label.setObjectName(_fromUtf8("Tx_Z_Val_label"))
        self.gridLayout1.addWidget(self.Tx_Z_Val_label, 3, 0, 1, 1)
        self.Tx_Y_Val_label = QtGui.QLabel(self.centralwidget)
        self.Tx_Y_Val_label.setObjectName(_fromUtf8("Tx_Y_Val_label"))
        self.gridLayout1.addWidget(self.Tx_Y_Val_label, 1, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout1.addWidget(self.label_2, 5, 4, 1, 1)
        self.Antennas_Add_btn = QtGui.QPushButton(self.centralwidget)
        self.Antennas_Add_btn.setObjectName(_fromUtf8("Antennas_Add_btn"))
        self.gridLayout1.addWidget(self.Antennas_Add_btn, 7, 2, 1, 1)
        self.Tx_X_Clear_btn = QtGui.QPushButton(self.centralwidget)
        self.Tx_X_Clear_btn.setObjectName(_fromUtf8("Tx_X_Clear_btn"))
        self.gridLayout1.addWidget(self.Tx_X_Clear_btn, 0, 5, 1, 1)
        self.Tx_Z_Clear_btn_12 = QtGui.QPushButton(self.centralwidget)
        self.Tx_Z_Clear_btn_12.setObjectName(_fromUtf8("Tx_Z_Clear_btn_12"))
        self.gridLayout1.addWidget(self.Tx_Z_Clear_btn_12, 5, 5, 1, 1)
        self.Tx_Z_Clear_btn = QtGui.QPushButton(self.centralwidget)
        self.Tx_Z_Clear_btn.setObjectName(_fromUtf8("Tx_Z_Clear_btn"))
        self.gridLayout1.addWidget(self.Tx_Z_Clear_btn, 1, 5, 1, 1)
        self.Antennas_viewXML_btn = QtGui.QPushButton(self.centralwidget)
        self.Antennas_viewXML_btn.setObjectName(_fromUtf8("Antennas_viewXML_btn"))
        self.gridLayout1.addWidget(self.Antennas_viewXML_btn, 9, 5, 1, 1)
        self.Antennas_Remove_btn = QtGui.QPushButton(self.centralwidget)
        self.Antennas_Remove_btn.setObjectName(_fromUtf8("Antennas_Remove_btn"))
        self.gridLayout1.addWidget(self.Antennas_Remove_btn, 9, 2, 1, 1)
        self.Tx_Z_Val_label_2 = QtGui.QLabel(self.centralwidget)
        self.Tx_Z_Val_label_2.setObjectName(_fromUtf8("Tx_Z_Val_label_2"))
        self.gridLayout1.addWidget(self.Tx_Z_Val_label_2, 8, 0, 1, 1)
        self.Antennas_removal_input = QtGui.QLineEdit(self.centralwidget)
        self.Antennas_removal_input.setObjectName(_fromUtf8("Antennas_removal_input"))
        self.gridLayout1.addWidget(self.Antennas_removal_input, 8, 2, 1, 1)
        self.Antennas_gauss_clear_btn_2 = QtGui.QPushButton(self.centralwidget)
        self.Antennas_gauss_clear_btn_2.setObjectName(_fromUtf8("Antennas_gauss_clear_btn_2"))
        self.gridLayout1.addWidget(self.Antennas_gauss_clear_btn_2, 8, 5, 1, 1)
        self.gridLayout1.setColumnStretch(0, 8)
        self.horizontalLayout1.addLayout(self.gridLayout1)
        self.horizontalLayout.addLayout(self.horizontalLayout1)
        Antennas.setCentralWidget(self.centralwidget)

        self.retranslateUi(Antennas)
        QtCore.QObject.connect(self.Tx_X_Clear_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Antennas_name_input.clear)
        QtCore.QObject.connect(self.Tx_Z_Clear_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Antennas_efficiency_input.clear)
        QtCore.QObject.connect(self.Tx_Z_Clear_btn_11, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Antennas_sinc_alpha_input.clear)
        QtCore.QObject.connect(self.Tx_Z_Clear_btn_11, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Antennas_sinc_beta_input.clear)
        QtCore.QObject.connect(self.Tx_Z_Clear_btn_11, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Antennas_sinc_gamma_input.clear)
        QtCore.QObject.connect(self.Tx_Z_Clear_btn_12, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Antennas_para_diam_input.clear)
        QtCore.QObject.connect(self.Antennas_gauss_clear_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Antennas_gauss_azscale_input.clear)
        QtCore.QObject.connect(self.Antennas_gauss_clear_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Antennas_gauss_elscale_input.clear)
        QtCore.QObject.connect(self.Tx_Z_Clear_btn_8, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Iso_chkbx.toggle)
        QtCore.QObject.connect(self.Tx_Z_Clear_btn_11, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Sinc_chkbx.toggle)
        QtCore.QObject.connect(self.Tx_Z_Clear_btn_12, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Para_chkbx.toggle)
        QtCore.QObject.connect(self.Antennas_gauss_clear_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Gauss_Chkbx.toggle)
        QtCore.QObject.connect(self.Antennas_gauss_clear_btn_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Antennas_removal_input.clear)
        QtCore.QMetaObject.connectSlotsByName(Antennas)
        Antennas.setTabOrder(self.Antennas_name_input, self.Antennas_efficiency_input)
        Antennas.setTabOrder(self.Antennas_efficiency_input, self.Iso_chkbx)
        Antennas.setTabOrder(self.Iso_chkbx, self.Sinc_chkbx)
        Antennas.setTabOrder(self.Sinc_chkbx, self.Antennas_sinc_alpha_input)
        Antennas.setTabOrder(self.Antennas_sinc_alpha_input, self.Antennas_sinc_beta_input)
        Antennas.setTabOrder(self.Antennas_sinc_beta_input, self.Antennas_sinc_gamma_input)
        Antennas.setTabOrder(self.Antennas_sinc_gamma_input, self.Para_chkbx)
        Antennas.setTabOrder(self.Para_chkbx, self.Antennas_para_diam_input)
        Antennas.setTabOrder(self.Antennas_para_diam_input, self.Gauss_Chkbx)
        Antennas.setTabOrder(self.Gauss_Chkbx, self.Antennas_gauss_azscale_input)
        Antennas.setTabOrder(self.Antennas_gauss_azscale_input, self.Antennas_gauss_elscale_input)
        Antennas.setTabOrder(self.Antennas_gauss_elscale_input, self.Antennas_Add_btn)
        Antennas.setTabOrder(self.Antennas_Add_btn, self.Tx_X_Clear_btn)
        Antennas.setTabOrder(self.Tx_X_Clear_btn, self.Tx_Z_Clear_btn)
        Antennas.setTabOrder(self.Tx_Z_Clear_btn, self.Tx_Z_Clear_btn_8)
        Antennas.setTabOrder(self.Tx_Z_Clear_btn_8, self.Tx_Z_Clear_btn_11)
        Antennas.setTabOrder(self.Tx_Z_Clear_btn_11, self.Tx_Z_Clear_btn_12)
        Antennas.setTabOrder(self.Tx_Z_Clear_btn_12, self.Antennas_gauss_clear_btn)
        Antennas.setTabOrder(self.Antennas_gauss_clear_btn, self.Antennas_removal_input)
        Antennas.setTabOrder(self.Antennas_removal_input, self.Antennas_Remove_btn)
        Antennas.setTabOrder(self.Antennas_Remove_btn, self.Antennas_gauss_clear_btn_2)
        Antennas.setTabOrder(self.Antennas_gauss_clear_btn_2, self.Antennas_viewXML_btn)

    def retranslateUi(self, Antennas):
        Antennas.setWindowTitle(_translate("Antennas", "Antennas", None))
        self.Clocks_label.setText(_translate("Antennas", "Antennas", None))
        self.Antennas_gauss_elscale_input.setPlaceholderText(_translate("Antennas", "<Sample elscale Value>", None))
        self.Antennas_efficiency_input.setPlaceholderText(_translate("Antennas", "< [ 0 : 1 ] >", None))
        self.Antennas_sinc_beta_input.setPlaceholderText(_translate("Antennas", "<Sample Beta Value>", None))
        self.Antennas_gauss_clear_btn.setText(_translate("Antennas", "Clear", None))
        self.Antennas_sinc_gamma_input.setPlaceholderText(_translate("Antennas", "<Sample Gamma Value>", None))
        self.Iso_chkbx.setText(_translate("Antennas", "Isotropic", None))
        self.Sinc_chkbx.setText(_translate("Antennas", "Sinc", None))
        self.Para_chkbx.setText(_translate("Antennas", "Parabolic", None))
        self.Antennas_sinc_alpha_input.setPlaceholderText(_translate("Antennas", "<Sample Alpha Value>", None))
        self.Gauss_Chkbx.setText(_translate("Antennas", "Gaussian", None))
        self.label.setText(_translate("Antennas", "Dish Diameter", None))
        self.Clocks_name_label.setText(_translate("Antennas", "Name", None))
        self.Antennas_name_input.setPlaceholderText(_translate("Antennas", "<Sample Name>", None))
        self.Tx_Z_Clear_btn_11.setText(_translate("Antennas", "Clear", None))
        self.Antennas_para_diam_input.setPlaceholderText(_translate("Antennas", "<Sample Diameter Value>", None))
        self.Tx_Z_Clear_btn_8.setText(_translate("Antennas", "Clear", None))
        self.Antennas_gauss_azscale_input.setPlaceholderText(_translate("Antennas", "<Sample azscale Value>", None))
        self.Tx_Z_Val_label.setText(_translate("Antennas", "Pattern", None))
        self.Tx_Y_Val_label.setText(_translate("Antennas", "Efficiency", None))
        self.label_2.setText(_translate("Antennas", "metres", None))
        self.Antennas_Add_btn.setText(_translate("Antennas", "Add to XML", None))
        self.Tx_X_Clear_btn.setText(_translate("Antennas", "Clear", None))
        self.Tx_Z_Clear_btn_12.setText(_translate("Antennas", "Clear", None))
        self.Tx_Z_Clear_btn.setText(_translate("Antennas", "Clear", None))
        self.Antennas_viewXML_btn.setText(_translate("Antennas", "View XML", None))
        self.Antennas_Remove_btn.setText(_translate("Antennas", "Remove from XML", None))
        self.Tx_Z_Val_label_2.setText(_translate("Antennas", "Remove existing antenna", None))
        self.Antennas_removal_input.setPlaceholderText(_translate("Antennas", "<Sample Name>", None))
        self.Antennas_gauss_clear_btn_2.setText(_translate("Antennas", "Clear", None))
    
        ## connects functions to buttons
        self.Antennas_Add_btn.clicked.connect(self.callAppend)
        self.Antennas_viewXML_btn.clicked.connect(self.showEntry)
        self.Antennas_Remove_btn.clicked.connect(self.removeNode)
    
    ## removes antenna from simulation
    def removeNode(self):
        doc = etree.parse(filename, parser)
        root = doc.getroot()
        for ant in root.findall('antenna'):
            name = ant.get('name')
            if name == str(self.Antennas_removal_input.text()):            
                root.remove(ant)
                doc.write(filename,pretty_print=False) 
                print '--Antenna removed--'
            else:
                print "--Antenna not found--"            

    ## prints formatted xml to console
    def showEntry(self):
        doc = etree.parse(filename, parser)
        print(etree.tostring(doc, pretty_print=True))
        
    
    ## adds antenna to simulation
    def callAppend(self):
        name = str(self.Antennas_name_input.text())
        ant_efficiency = str(self.Antennas_efficiency_input.text())
        a = str(self.Antennas_sinc_alpha_input.text())
        b = str(self.Antennas_sinc_beta_input.text())
        g = str(self.Antennas_sinc_gamma_input.text())
        d = str(self.Antennas_para_diam_input.text())
        az = str(self.Antennas_gauss_azscale_input.text())
        el = str(self.Antennas_gauss_elscale_input.text())       
        
        ## enables the program to only run when a relevant pattern type is selected
        if (self.Iso_chkbx.isChecked()):
            gain_pattern= 'isotropic'
            appendAntenna(filename, name, gain_pattern, '', ant_efficiency, a, b, g, d, az, el)
            print '--Antenna added--'
            
        elif(self.Sinc_chkbx.isChecked()):
            gain_pattern= 'sinc'
            appendAntenna(filename, name, gain_pattern, '', ant_efficiency, a, b, g, d, az, el)
            print '--Antenna added--'
            
        elif(self.Para_chkbx.isChecked()):
            gain_pattern = 'parabolic'
            appendAntenna(filename, name, gain_pattern, '', ant_efficiency, a, b, g, d, az, el)
            print '--Antenna added--'
            
        elif(self.Gauss_Chkbx.isChecked()):
            gain_pattern = 'gaussian' 
            appendAntenna(filename, name, gain_pattern, '', ant_efficiency, a, b, g, d, az, el)
            print '--Antenna added--'
            
        else:
            gain_pattern=''
            print '--Please select relevant pattern type--'
            
        


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Antennas = QtGui.QMainWindow()
    ui = Ui_Antennas()
    ui.setupUi(Antennas)
    Antennas.show()
    sys.exit(app.exec_())

