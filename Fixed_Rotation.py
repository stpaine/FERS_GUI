# -- Fixed_Rotation.py as part of FERS XML File I/O as part of FERS Plugin
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

class Ui_Fixed_Rotation(QtGui.QMainWindow):

    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        
    def setupUi(self, Fixed_Rotation):
        Fixed_Rotation.setObjectName(_fromUtf8("Fixed_Rotation"))
        Fixed_Rotation.resize(501, 257)
        self.centralwidget = QtGui.QWidget(Fixed_Rotation)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout3 = QtGui.QHBoxLayout()
        self.horizontalLayout3.setObjectName(_fromUtf8("horizontalLayout3"))
        self._2 = QtGui.QGridLayout()
        self._2.setObjectName(_fromUtf8("_2"))
        self.T_Pulse_carrier_clear_3 = QtGui.QPushButton(self.centralwidget)
        self.T_Pulse_carrier_clear_3.setObjectName(_fromUtf8("T_Pulse_carrier_clear_3"))
        self._2.addWidget(self.T_Pulse_carrier_clear_3, 3, 4, 1, 1)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self._2.addWidget(self.label_4, 2, 3, 1, 1)
        self.FixedR_Azi_AV_input = QtGui.QLineEdit(self.centralwidget)
        self.FixedR_Azi_AV_input.setObjectName(_fromUtf8("FixedR_Azi_AV_input"))
        self._2.addWidget(self.FixedR_Azi_AV_input, 2, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self._2.addWidget(self.label_2, 4, 3, 1, 1)
        self.T_Pulse_file_label_2 = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_file_label_2.setObjectName(_fromUtf8("T_Pulse_file_label_2"))
        self._2.addWidget(self.T_Pulse_file_label_2, 1, 1, 1, 1)
        self.FixedR_Init_Azi_input = QtGui.QLineEdit(self.centralwidget)
        self.FixedR_Init_Azi_input.setObjectName(_fromUtf8("FixedR_Init_Azi_input"))
        self._2.addWidget(self.FixedR_Init_Azi_input, 1, 2, 1, 1)
        self.T_Pulse_file_label_5 = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_file_label_5.setObjectName(_fromUtf8("T_Pulse_file_label_5"))
        self._2.addWidget(self.T_Pulse_file_label_5, 4, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self._2.addWidget(self.label_3, 1, 3, 1, 1)
        self.T_Pulse_carrier_clear_4 = QtGui.QPushButton(self.centralwidget)
        self.T_Pulse_carrier_clear_4.setObjectName(_fromUtf8("T_Pulse_carrier_clear_4"))
        self._2.addWidget(self.T_Pulse_carrier_clear_4, 4, 4, 1, 1)
        self.Motion_Path_time_input = QtGui.QLineEdit(self.centralwidget)
        self.Motion_Path_time_input.setObjectName(_fromUtf8("Motion_Path_time_input"))
        self._2.addWidget(self.Motion_Path_time_input, 4, 2, 1, 1)
        self.Motion_Path_alt_input = QtGui.QLineEdit(self.centralwidget)
        self.Motion_Path_alt_input.setObjectName(_fromUtf8("Motion_Path_alt_input"))
        self._2.addWidget(self.Motion_Path_alt_input, 3, 2, 1, 1)
        self.FixedR_ = QtGui.QPushButton(self.centralwidget)
        self.FixedR_.setObjectName(_fromUtf8("FixedR_"))
        self._2.addWidget(self.FixedR_, 5, 2, 1, 1)
        self.FixedR_Remove_btn = QtGui.QPushButton(self.centralwidget)
        self.FixedR_Remove_btn.setObjectName(_fromUtf8("FixedR_Remove_btn"))
        self._2.addWidget(self.FixedR_Remove_btn, 6, 4, 1, 1)
        self.T_Pulse_carrier_clear_2 = QtGui.QPushButton(self.centralwidget)
        self.T_Pulse_carrier_clear_2.setObjectName(_fromUtf8("T_Pulse_carrier_clear_2"))
        self._2.addWidget(self.T_Pulse_carrier_clear_2, 2, 4, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self._2.addWidget(self.label, 3, 3, 1, 1)
        self.T_Pulse_file_label_6 = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_file_label_6.setObjectName(_fromUtf8("T_Pulse_file_label_6"))
        self._2.addWidget(self.T_Pulse_file_label_6, 6, 1, 1, 1)
        self.T_Pulse_carrier_clear = QtGui.QPushButton(self.centralwidget)
        self.T_Pulse_carrier_clear.setObjectName(_fromUtf8("T_Pulse_carrier_clear"))
        self._2.addWidget(self.T_Pulse_carrier_clear, 1, 4, 1, 1)
        self.T_Pulse_file_label_4 = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_file_label_4.setObjectName(_fromUtf8("T_Pulse_file_label_4"))
        self._2.addWidget(self.T_Pulse_file_label_4, 3, 1, 1, 1)
        self.T_Pulse_file_label_3 = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_file_label_3.setObjectName(_fromUtf8("T_Pulse_file_label_3"))
        self._2.addWidget(self.T_Pulse_file_label_3, 2, 1, 1, 1)
        self.T_Pulse_label_2 = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_label_2.setBaseSize(QtCore.QSize(7, 0))
        self.T_Pulse_label_2.setObjectName(_fromUtf8("T_Pulse_label_2"))
        self._2.addWidget(self.T_Pulse_label_2, 3, 0, 1, 1)
        self.T_Pulse_file_label_7 = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_file_label_7.setObjectName(_fromUtf8("T_Pulse_file_label_7"))
        self._2.addWidget(self.T_Pulse_file_label_7, 0, 1, 1, 1)
        self.platform_sel = QtGui.QComboBox(self.centralwidget)
        self.platform_sel.setObjectName(_fromUtf8("platform_sel"))
        self._2.addWidget(self.platform_sel, 0, 2, 1, 3)
        self._2.setColumnStretch(0, 8)
        self.horizontalLayout3.addLayout(self._2)
        self.verticalLayout.addLayout(self.horizontalLayout3)
        self.Motion_Path_back_btn = QtGui.QPushButton(self.centralwidget)
        self.Motion_Path_back_btn.setObjectName(_fromUtf8("Motion_Path_back_btn"))
        self.verticalLayout.addWidget(self.Motion_Path_back_btn)
        Fixed_Rotation.setCentralWidget(self.centralwidget)

        self.retranslateUi(Fixed_Rotation)
        QtCore.QObject.connect(self.T_Pulse_carrier_clear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.FixedR_Init_Azi_input.clear)
        QtCore.QObject.connect(self.T_Pulse_carrier_clear_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.FixedR_Azi_AV_input.clear)
        QtCore.QObject.connect(self.T_Pulse_carrier_clear_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Motion_Path_alt_input.clear)
        QtCore.QObject.connect(self.T_Pulse_carrier_clear_4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Motion_Path_time_input.clear)
        QtCore.QMetaObject.connectSlotsByName(Fixed_Rotation)
        Fixed_Rotation.setTabOrder(self.FixedR_Init_Azi_input, self.FixedR_Azi_AV_input)
        Fixed_Rotation.setTabOrder(self.FixedR_Azi_AV_input, self.Motion_Path_alt_input)
        Fixed_Rotation.setTabOrder(self.Motion_Path_alt_input, self.Motion_Path_time_input)
        Fixed_Rotation.setTabOrder(self.Motion_Path_time_input, self.FixedR_)
        Fixed_Rotation.setTabOrder(self.FixedR_, self.T_Pulse_carrier_clear)
        Fixed_Rotation.setTabOrder(self.T_Pulse_carrier_clear, self.T_Pulse_carrier_clear_2)
        Fixed_Rotation.setTabOrder(self.T_Pulse_carrier_clear_2, self.T_Pulse_carrier_clear_3)
        Fixed_Rotation.setTabOrder(self.T_Pulse_carrier_clear_3, self.T_Pulse_carrier_clear_4)
        Fixed_Rotation.setTabOrder(self.T_Pulse_carrier_clear_4, self.FixedR_Remove_btn)
        Fixed_Rotation.setTabOrder(self.FixedR_Remove_btn, self.Motion_Path_back_btn)

    def retranslateUi(self, Fixed_Rotation):
        Fixed_Rotation.setWindowTitle(_translate("Fixed_Rotation", "Fixed_Rotation", None))
        self.T_Pulse_carrier_clear_3.setText(_translate("Fixed_Rotation", "Clear", None))
        self.label_4.setText(_translate("Fixed_Rotation", "m/s", None))
        self.FixedR_Azi_AV_input.setPlaceholderText(_translate("Fixed_Rotation", "<Sample Velocity>", None))
        self.label_2.setText(_translate("Fixed_Rotation", "m/s", None))
        self.T_Pulse_file_label_2.setText(_translate("Fixed_Rotation", "Initial Azimuth Angle", None))
        self.FixedR_Init_Azi_input.setPlaceholderText(_translate("Fixed_Rotation", "<Sample Value>", None))
        self.T_Pulse_file_label_5.setText(_translate("Fixed_Rotation", "Elevation Angular Velocity", None))
        self.label_3.setText(_translate("Fixed_Rotation", "degrees", None))
        self.T_Pulse_carrier_clear_4.setText(_translate("Fixed_Rotation", "Clear", None))
        self.Motion_Path_time_input.setPlaceholderText(_translate("Fixed_Rotation", "<Sample Velocity>", None))
        self.Motion_Path_alt_input.setPlaceholderText(_translate("Fixed_Rotation", "<Sample Metres>", None))
        self.FixedR_.setText(_translate("Fixed_Rotation", "Add Fixed Rotation", None))
        self.FixedR_Remove_btn.setText(_translate("Fixed_Rotation", "Remove from XML", None))
        self.T_Pulse_carrier_clear_2.setText(_translate("Fixed_Rotation", "Clear", None))
        self.label.setText(_translate("Fixed_Rotation", "metres", None))
        self.T_Pulse_file_label_6.setText(_translate("Fixed_Rotation", "Remove existing Fixed Rotation", None))
        self.T_Pulse_carrier_clear.setText(_translate("Fixed_Rotation", "Clear", None))
        self.T_Pulse_file_label_4.setText(_translate("Fixed_Rotation", "Initial Elevation", None))
        self.T_Pulse_file_label_3.setText(_translate("Fixed_Rotation", "Azimuth Angular Velocity", None))
        self.T_Pulse_label_2.setText(_translate("Fixed_Rotation", "Fixed Rotation", None))
        self.T_Pulse_file_label_7.setText(_translate("Fixed_Rotation", "Platform Name", None))
        self.Motion_Path_back_btn.setText(_translate("Fixed_Rotation", "view XML", None))

        ## connects functions to buttons
        self.FixedR_.clicked.connect(self.callAppend)
        self.Motion_Path_back_btn.clicked.connect(self.showEntry)
        self.FixedR_Remove_btn.clicked.connect(self.removeNode) 

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

    ## removes fixed rotation from platform
    def removeNode(self):
        doc = etree.parse(filename)
        sim = doc.getroot()
        tree=etree.ElementTree(sim) 

        for plat in sim.findall('platform'):
            name = plat.get('name')
            if name == str(self.platform_sel.currentText()):
                for fixed in plat.findall('fixedrotation'):
                    plat.remove(fixed)
                    doc.write(filename,pretty_print=True)
                    print '--Fixed Rotation removed--' 
            else:
                print '--Invalid Platform Name. Please Try again--'                       

    ## prints formatted xml to console
    def showEntry(self):
        doc = etree.parse(filename, parser)
        print(etree.tostring(doc, pretty_print=True))         
        
    ## adds fixed rotation to platform
    def callAppend(self):
        initial_azi_angle = str(self.FixedR_Init_Azi_input.text())
        ani_angular_vel = str(self.FixedR_Azi_AV_input.text())
        init_el = str(self.Motion_Path_alt_input.text())
        el_angular_vel = str(self.Motion_Path_time_input.text())
        plat_name = str(self.platform_sel.currentText())
        appendFixedRotation(filename,plat_name, initial_azi_angle, ani_angular_vel, init_el, el_angular_vel)
        print '--Fixed Rotation added--'                     


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Fixed_Rotation = QtGui.QMainWindow()
    ui = Ui_Fixed_Rotation()
    ui.setupUi(Fixed_Rotation)
    Fixed_Rotation.show()
    sys.exit(app.exec_())

