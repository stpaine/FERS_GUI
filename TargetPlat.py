# -- TargetPlat.py as part of FERS XML File I/O as part of FERS Plugin
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

class Ui_Target(QtGui.QMainWindow):

    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        
    def setupUi(self, Target):
        Target.setObjectName(_fromUtf8("Target"))
        Target.resize(595, 360)
        self.centralwidget = QtGui.QWidget(Target)
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
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self._2.addWidget(self.label_4, 4, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self._2.addWidget(self.label_2, 5, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self._2.addWidget(self.label_3, 6, 0, 1, 1)
        self.T_Pulse_power_clear_3 = QtGui.QPushButton(self.centralwidget)
        self.T_Pulse_power_clear_3.setObjectName(_fromUtf8("T_Pulse_power_clear_3"))
        self._2.addWidget(self.T_Pulse_power_clear_3, 6, 3, 1, 1)
        self.Target_Record_btn = QtGui.QPushButton(self.centralwidget)
        self.Target_Record_btn.setObjectName(_fromUtf8("Target_Record_btn"))
        self._2.addWidget(self.Target_Record_btn, 8, 1, 1, 1)
        self.Target_Name_input = QtGui.QLineEdit(self.centralwidget)
        self.Target_Name_input.setObjectName(_fromUtf8("Target_Name_input"))
        self._2.addWidget(self.Target_Name_input, 1, 1, 1, 1)
        self.T_Pulse_file_label = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_file_label.setObjectName(_fromUtf8("T_Pulse_file_label"))
        self._2.addWidget(self.T_Pulse_file_label, 2, 0, 1, 1)
        self.Target_RCS_input_2 = QtGui.QLineEdit(self.centralwidget)
        self.Target_RCS_input_2.setObjectName(_fromUtf8("Target_RCS_input_2"))
        self._2.addWidget(self.Target_RCS_input_2, 3, 1, 1, 1)
        self.T_Pulse_filename_clear = QtGui.QPushButton(self.centralwidget)
        self.T_Pulse_filename_clear.setObjectName(_fromUtf8("T_Pulse_filename_clear"))
        self._2.addWidget(self.T_Pulse_filename_clear, 1, 3, 1, 1)
        self.T_Pulse_power_clear = QtGui.QPushButton(self.centralwidget)
        self.T_Pulse_power_clear.setObjectName(_fromUtf8("T_Pulse_power_clear"))
        self._2.addWidget(self.T_Pulse_power_clear, 3, 3, 1, 1)
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self._2.addWidget(self.comboBox, 5, 1, 1, 3)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self._2.addWidget(self.label_5, 7, 0, 1, 1)
        self.Target_k_input = QtGui.QLineEdit(self.centralwidget)
        self.Target_k_input.setObjectName(_fromUtf8("Target_k_input"))
        self._2.addWidget(self.Target_k_input, 6, 1, 1, 1)
        self.Target_Constant_input = QtGui.QLineEdit(self.centralwidget)
        self.Target_Constant_input.setObjectName(_fromUtf8("Target_Constant_input"))
        self._2.addWidget(self.Target_Constant_input, 7, 1, 1, 1)
        self.T_Pulse_power_clear_4 = QtGui.QPushButton(self.centralwidget)
        self.T_Pulse_power_clear_4.setObjectName(_fromUtf8("T_Pulse_power_clear_4"))
        self._2.addWidget(self.T_Pulse_power_clear_4, 7, 3, 1, 1)
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self._2.addWidget(self.label_6, 10, 0, 1, 1)
        self.T_Pulse_name_label_2 = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_name_label_2.setObjectName(_fromUtf8("T_Pulse_name_label_2"))
        self._2.addWidget(self.T_Pulse_name_label_2, 0, 0, 1, 1)
        self.T_Pulse_power_label = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_power_label.setObjectName(_fromUtf8("T_Pulse_power_label"))
        self._2.addWidget(self.T_Pulse_power_label, 3, 0, 1, 1)
        self.T_Pulse_name_label = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_name_label.setObjectName(_fromUtf8("T_Pulse_name_label"))
        self._2.addWidget(self.T_Pulse_name_label, 1, 0, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self._2.addWidget(self.label, 3, 2, 1, 1)
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self._2.addWidget(self.label_7, 11, 0, 1, 1)
        self.Target_removal_input = QtGui.QLineEdit(self.centralwidget)
        self.Target_removal_input.setObjectName(_fromUtf8("Target_removal_input"))
        self._2.addWidget(self.Target_removal_input, 11, 1, 1, 1)
        self.T_Pulse_power_clear_5 = QtGui.QPushButton(self.centralwidget)
        self.T_Pulse_power_clear_5.setObjectName(_fromUtf8("T_Pulse_power_clear_5"))
        self._2.addWidget(self.T_Pulse_power_clear_5, 11, 3, 1, 1)
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self._2.addWidget(self.pushButton_4, 12, 1, 1, 1)
        self.platform_sel = QtGui.QComboBox(self.centralwidget)
        self.platform_sel.setObjectName(_fromUtf8("platform_sel"))
        self._2.addWidget(self.platform_sel, 0, 1, 1, 3)
        self._2.setColumnStretch(0, 8)
        self.horizontalLayout3.addLayout(self._2)
        self.verticalLayout.addLayout(self.horizontalLayout3)
        self.Target_back_btn_3 = QtGui.QPushButton(self.centralwidget)
        self.Target_back_btn_3.setObjectName(_fromUtf8("Target_back_btn_3"))
        self.verticalLayout.addWidget(self.Target_back_btn_3)
        Target.setCentralWidget(self.centralwidget)

        self.retranslateUi(Target)
        QtCore.QObject.connect(self.T_Pulse_filename_clear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Target_Name_input.clear)
        QtCore.QObject.connect(self.T_Pulse_power_clear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Target_RCS_input_2.clear)
        QtCore.QObject.connect(self.T_Pulse_power_clear_4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Target_Constant_input.clear)
        QtCore.QObject.connect(self.T_Pulse_power_clear_5, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Target_removal_input.clear)
        QtCore.QObject.connect(self.T_Pulse_power_clear_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Target_k_input.clear)
        QtCore.QMetaObject.connectSlotsByName(Target)
        Target.setTabOrder(self.Target_Name_input, self.Target_RCS_input_2)
        Target.setTabOrder(self.Target_RCS_input_2, self.comboBox)
        Target.setTabOrder(self.comboBox, self.Target_k_input)
        Target.setTabOrder(self.Target_k_input, self.Target_Constant_input)
        Target.setTabOrder(self.Target_Constant_input, self.Target_Record_btn)
        Target.setTabOrder(self.Target_Record_btn, self.Target_removal_input)
        Target.setTabOrder(self.Target_removal_input, self.pushButton_4)
        Target.setTabOrder(self.pushButton_4, self.T_Pulse_filename_clear)
        Target.setTabOrder(self.T_Pulse_filename_clear, self.T_Pulse_power_clear)
        Target.setTabOrder(self.T_Pulse_power_clear, self.T_Pulse_power_clear_3)
        Target.setTabOrder(self.T_Pulse_power_clear_3, self.T_Pulse_power_clear_4)
        Target.setTabOrder(self.T_Pulse_power_clear_4, self.T_Pulse_power_clear_5)
        Target.setTabOrder(self.T_Pulse_power_clear_5, self.Target_back_btn_3)

    def retranslateUi(self, Target):
        Target.setWindowTitle(_translate("Target", "Target", None))
        self.T_Pulse_label.setText(_translate("Target", "Target", None))
        self.label_4.setText(_translate("Target", "Model Parameters", None))
        self.label_2.setText(_translate("Target", "Model type", None))
        self.label_3.setText(_translate("Target", "k (chisquare or gamma)", None))
        self.T_Pulse_power_clear_3.setText(_translate("Target", "Clear", None))
        self.Target_Record_btn.setText(_translate("Target", "Add to XML", None))
        self.Target_Name_input.setPlaceholderText(_translate("Target", "<Sample Name>", None))
        self.T_Pulse_file_label.setText(_translate("Target", "RCS type (Default = \'isotropic\')", None))
        self.Target_RCS_input_2.setPlaceholderText(_translate("Target", "<Sample Value>", None))
        self.T_Pulse_filename_clear.setText(_translate("Target", "Clear", None))
        self.T_Pulse_power_clear.setText(_translate("Target", "Clear", None))
        self.comboBox.setItemText(0, _translate("Target", "constant", None))
        self.comboBox.setItemText(1, _translate("Target", "chnisquare", None))
        self.comboBox.setItemText(2, _translate("Target", "gamma", None))
        self.label_5.setText(_translate("Target", "constant", None))
        self.Target_k_input.setPlaceholderText(_translate("Target", "<Sample Value>", None))
        self.Target_Constant_input.setPlaceholderText(_translate("Target", "<Sample Value>", None))
        self.T_Pulse_power_clear_4.setText(_translate("Target", "Clear", None))
        self.label_6.setText(_translate("Target", "Remove from existing XML", None))
        self.T_Pulse_name_label_2.setText(_translate("Target", "Platform Name", None))
        self.T_Pulse_power_label.setText(_translate("Target", "RCS Value", None))
        self.T_Pulse_name_label.setText(_translate("Target", "Target Name", None))
        self.label.setText(_translate("Target", "m^2", None))
        self.label_7.setText(_translate("Target", "Existing target name", None))
        self.Target_removal_input.setPlaceholderText(_translate("Target", "<Sample Name>", None))
        self.T_Pulse_power_clear_5.setText(_translate("Target", "Clear", None))
        self.pushButton_4.setText(_translate("Target", "Remove from XML", None))
        self.Target_back_btn_3.setText(_translate("Target", "View XML", None))


        ## connects functions to buttons
        self.Target_Record_btn.clicked.connect(self.callAppend)
        self.Target_back_btn_3.clicked.connect(self.showEntry)
        self.pushButton_4.clicked.connect(self.removeNode)
        
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
    
    ## removes receiver from platform
    def removeNode(self):
        doc = etree.parse(filename, parser)
        sim = doc.getroot()
        tree=etree.ElementTree(sim)  
        for plat in sim.findall('platform'):
            lol = plat.get('name')
            if lol == str(self.platform_sel.currentText()):
                for targ in plat.findall('target'):
                    tar = targ.get('name')
                    if tar == str(self.Target_removal_input.text()):            
                        plat.remove(targ)
                        doc.write(filename,pretty_print=True)
                        print '--Target removed from Platform--'
                    else:
                        print "--Target not found--"
            else:
                print '--Invalid Platform. Please Try Again--'

    ## prints formatted xml to console
    def showEntry(self):
        doc = etree.parse(filename, parser)
        print(etree.tostring(doc, pretty_print=True))   

    ## adds receiver to platform
    def callAppend(self):
        name = str(self.Target_Name_input.text())
        rcs_type = 'isotropic'
        ##rcs_type = str(self.Target_RCS_filename_input.text())
        rcs_value = str(self.Target_RCS_input_2.text())
        model =str(self.comboBox.currentText())
        const = str(self.Target_Constant_input.text())
        standard_dev = str(self.Target_k_input.text())
        plat_name = str(self.platform_sel.currentText())

        appendTargetToPlatform(filename,plat_name, name, rcs_type, rcs_value, model, const, standard_dev)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Target = QtGui.QMainWindow()
    ui = Ui_Target()
    ui.setupUi(Target)
    Target.show()
    sys.exit(app.exec_())

