# -- Multipath_Surfaces.py as part of FERS XML File I/O as part of FERS Plugin
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

class Ui_Multipath_Surfaces(QtGui.QMainWindow):

    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        
    def setupUi(self, Multipath_Surfaces):
        Multipath_Surfaces.setObjectName(_fromUtf8("Multipath_Surfaces"))
        Multipath_Surfaces.resize(480, 301)
        self.centralwidget = QtGui.QWidget(Multipath_Surfaces)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout3 = QtGui.QHBoxLayout()
        self.horizontalLayout3.setObjectName(_fromUtf8("horizontalLayout3"))
        self._2 = QtGui.QGridLayout()
        self._2.setObjectName(_fromUtf8("_2"))
        self.T_Pulse_file_label_3 = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_file_label_3.setObjectName(_fromUtf8("T_Pulse_file_label_3"))
        self._2.addWidget(self.T_Pulse_file_label_3, 2, 1, 1, 1)
        self.T_Pulse_carrier_clear = QtGui.QPushButton(self.centralwidget)
        self.T_Pulse_carrier_clear.setObjectName(_fromUtf8("T_Pulse_carrier_clear"))
        self._2.addWidget(self.T_Pulse_carrier_clear, 1, 3, 1, 1)
        self.T_Pulse_file_label_2 = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_file_label_2.setObjectName(_fromUtf8("T_Pulse_file_label_2"))
        self._2.addWidget(self.T_Pulse_file_label_2, 1, 1, 1, 1)
        self.T_Pulse_file_label_4 = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_file_label_4.setObjectName(_fromUtf8("T_Pulse_file_label_4"))
        self._2.addWidget(self.T_Pulse_file_label_4, 3, 1, 1, 1)
        self.T_Pulse_carrier_clear_2 = QtGui.QPushButton(self.centralwidget)
        self.T_Pulse_carrier_clear_2.setObjectName(_fromUtf8("T_Pulse_carrier_clear_2"))
        self._2.addWidget(self.T_Pulse_carrier_clear_2, 2, 3, 1, 1)
        self.T_Pulse_carrier_clear_3 = QtGui.QPushButton(self.centralwidget)
        self.T_Pulse_carrier_clear_3.setObjectName(_fromUtf8("T_Pulse_carrier_clear_3"))
        self._2.addWidget(self.T_Pulse_carrier_clear_3, 3, 3, 1, 1)
        self.Motion_Path_alt_input = QtGui.QLineEdit(self.centralwidget)
        self.Motion_Path_alt_input.setObjectName(_fromUtf8("Motion_Path_alt_input"))
        self._2.addWidget(self.Motion_Path_alt_input, 3, 2, 1, 1)
        self.FixedR_Azi_AV_input = QtGui.QLineEdit(self.centralwidget)
        self.FixedR_Azi_AV_input.setObjectName(_fromUtf8("FixedR_Azi_AV_input"))
        self._2.addWidget(self.FixedR_Azi_AV_input, 2, 2, 1, 1)
        self.RWP_elevation_angle_input = QtGui.QLineEdit(self.centralwidget)
        self.RWP_elevation_angle_input.setObjectName(_fromUtf8("RWP_elevation_angle_input"))
        self._2.addWidget(self.RWP_elevation_angle_input, 1, 2, 1, 1)
        self.RWP_plat_name = QtGui.QLineEdit(self.centralwidget)
        self.RWP_plat_name.setObjectName(_fromUtf8("RWP_plat_name"))
        self._2.addWidget(self.RWP_plat_name, 0, 2, 1, 1)
        self.T_Pulse_carrier_clear_4 = QtGui.QPushButton(self.centralwidget)
        self.T_Pulse_carrier_clear_4.setObjectName(_fromUtf8("T_Pulse_carrier_clear_4"))
        self._2.addWidget(self.T_Pulse_carrier_clear_4, 0, 3, 1, 1)
        self.T_Pulse_file_label_6 = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_file_label_6.setObjectName(_fromUtf8("T_Pulse_file_label_6"))
        self._2.addWidget(self.T_Pulse_file_label_6, 6, 1, 1, 1)
        self.T_Pulse_file_label_5 = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_file_label_5.setObjectName(_fromUtf8("T_Pulse_file_label_5"))
        self._2.addWidget(self.T_Pulse_file_label_5, 0, 1, 1, 1)
        self.T_Pulse_file_label_7 = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_file_label_7.setObjectName(_fromUtf8("T_Pulse_file_label_7"))
        self._2.addWidget(self.T_Pulse_file_label_7, 2, 0, 1, 1)
        self.T_Pulse_file_label_8 = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_file_label_8.setObjectName(_fromUtf8("T_Pulse_file_label_8"))
        self._2.addWidget(self.T_Pulse_file_label_8, 4, 1, 1, 1)
        self.T_Pulse_carrier_clear_5 = QtGui.QPushButton(self.centralwidget)
        self.T_Pulse_carrier_clear_5.setObjectName(_fromUtf8("T_Pulse_carrier_clear_5"))
        self._2.addWidget(self.T_Pulse_carrier_clear_5, 4, 3, 1, 1)
        self.Motion_Path_alt_input_2 = QtGui.QLineEdit(self.centralwidget)
        self.Motion_Path_alt_input_2.setObjectName(_fromUtf8("Motion_Path_alt_input_2"))
        self._2.addWidget(self.Motion_Path_alt_input_2, 4, 2, 1, 1)
        self.Add = QtGui.QPushButton(self.centralwidget)
        self.Add.setObjectName(_fromUtf8("Add"))
        self._2.addWidget(self.Add, 5, 2, 1, 1)
        self.Remove = QtGui.QPushButton(self.centralwidget)
        self.Remove.setObjectName(_fromUtf8("Remove"))
        self._2.addWidget(self.Remove, 6, 3, 1, 1)
        self._2.setColumnStretch(0, 8)
        self.horizontalLayout3.addLayout(self._2)
        self.verticalLayout.addLayout(self.horizontalLayout3)
        self.view = QtGui.QPushButton(self.centralwidget)
        self.view.setObjectName(_fromUtf8("view"))
        self.verticalLayout.addWidget(self.view)
        Multipath_Surfaces.setCentralWidget(self.centralwidget)

        self.retranslateUi(Multipath_Surfaces)
        QtCore.QObject.connect(self.T_Pulse_carrier_clear_4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.RWP_plat_name.clear)
        QtCore.QObject.connect(self.T_Pulse_carrier_clear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.RWP_elevation_angle_input.clear)
        QtCore.QObject.connect(self.T_Pulse_carrier_clear_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.FixedR_Azi_AV_input.clear)
        QtCore.QObject.connect(self.T_Pulse_carrier_clear_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Motion_Path_alt_input.clear)
        QtCore.QObject.connect(self.T_Pulse_carrier_clear_5, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Motion_Path_alt_input_2.clear)
        QtCore.QMetaObject.connectSlotsByName(Multipath_Surfaces)
        Multipath_Surfaces.setTabOrder(self.RWP_plat_name, self.RWP_elevation_angle_input)
        Multipath_Surfaces.setTabOrder(self.RWP_elevation_angle_input, self.FixedR_Azi_AV_input)
        Multipath_Surfaces.setTabOrder(self.FixedR_Azi_AV_input, self.Motion_Path_alt_input)
        Multipath_Surfaces.setTabOrder(self.Motion_Path_alt_input, self.Motion_Path_alt_input_2)
        Multipath_Surfaces.setTabOrder(self.Motion_Path_alt_input_2, self.Add)
        Multipath_Surfaces.setTabOrder(self.Add, self.Remove)
        Multipath_Surfaces.setTabOrder(self.Remove, self.view)
        Multipath_Surfaces.setTabOrder(self.view, self.T_Pulse_carrier_clear_4)
        Multipath_Surfaces.setTabOrder(self.T_Pulse_carrier_clear_4, self.T_Pulse_carrier_clear)
        Multipath_Surfaces.setTabOrder(self.T_Pulse_carrier_clear, self.T_Pulse_carrier_clear_2)
        Multipath_Surfaces.setTabOrder(self.T_Pulse_carrier_clear_2, self.T_Pulse_carrier_clear_3)
        Multipath_Surfaces.setTabOrder(self.T_Pulse_carrier_clear_3, self.T_Pulse_carrier_clear_5)

    def retranslateUi(self, Multipath_Surfaces):
        Multipath_Surfaces.setWindowTitle(_translate("Multipath_Surfaces", "Multipath Surfaces", None))
        self.T_Pulse_file_label_3.setText(_translate("Multipath_Surfaces", "Y Value", None))
        self.T_Pulse_carrier_clear.setText(_translate("Multipath_Surfaces", "Clear", None))
        self.T_Pulse_file_label_2.setText(_translate("Multipath_Surfaces", "X Value", None))
        self.T_Pulse_file_label_4.setText(_translate("Multipath_Surfaces", "Z Value", None))
        self.T_Pulse_carrier_clear_2.setText(_translate("Multipath_Surfaces", "Clear", None))
        self.T_Pulse_carrier_clear_3.setText(_translate("Multipath_Surfaces", "Clear", None))
        self.Motion_Path_alt_input.setPlaceholderText(_translate("Multipath_Surfaces", "<Sample Time>", None))
        self.FixedR_Azi_AV_input.setPlaceholderText(_translate("Multipath_Surfaces", "<Sample Velocity>", None))
        self.RWP_elevation_angle_input.setPlaceholderText(_translate("Multipath_Surfaces", "<Sample Value>", None))
        self.RWP_plat_name.setPlaceholderText(_translate("Multipath_Surfaces", "<Sample Value>", None))
        self.T_Pulse_carrier_clear_4.setText(_translate("Multipath_Surfaces", "Clear", None))
        self.T_Pulse_file_label_6.setText(_translate("Multipath_Surfaces", "Remove existing Multipath Surfaces", None))
        self.T_Pulse_file_label_5.setText(_translate("Multipath_Surfaces", "Reflecting Factor", None))
        self.T_Pulse_file_label_7.setText(_translate("Multipath_Surfaces", "Multipath Surfaces", None))
        self.T_Pulse_file_label_8.setText(_translate("Multipath_Surfaces", "Distance", None))
        self.T_Pulse_carrier_clear_5.setText(_translate("Multipath_Surfaces", "Clear", None))
        self.Motion_Path_alt_input_2.setPlaceholderText(_translate("Multipath_Surfaces", "<Sample Time>", None))
        self.Add.setText(_translate("Multipath_Surfaces", "Add to XML", None))
        self.Remove.setText(_translate("Multipath_Surfaces", "Remove from XML", None))
        self.view.setText(_translate("Multipath_Surfaces", "view XML", None))

        ## connects functions to buttons
        self.Add.clicked.connect(self.callAppend)
        self.view.clicked.connect(self.showEntry)
        self.Remove.clicked.connect(self.removeNode)

    ## removes multipath surface from simulation
    def removeNode(self):
        doc = etree.parse(filename, parser)
        sim = doc.getroot()
        tree=etree.ElementTree(sim)  
        for multi in sim.findall('multipath'):
            sim.remove(multi)
            doc.write(filename,pretty_print=True)
            print '--Multipath removed--'

    ## prints formatted xml to console
    def showEntry(self):
        doc = etree.parse(filename, parser)
        print(etree.tostring(doc, pretty_print=True))   

    ## adds multipath surface to simulation
    def callAppend(self):
        refecting_factor = str(self.RWP_plat_name.text())
        x = str(self.RWP_elevation_angle_input.text())
        y = str(self.FixedR_Azi_AV_input.text())
        z = str(self.Motion_Path_alt_input.text())
        d = str(self.Motion_Path_alt_input_2.text())


        appendMultipathSurfaces(filename, refecting_factor, x, y, z,d)
        print '--Multipath Surface added to simulation--'


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Multipath_Surfaces = QtGui.QMainWindow()
    ui = Ui_Multipath_Surfaces()
    ui.setupUi(Multipath_Surfaces)
    Multipath_Surfaces.show()
    sys.exit(app.exec_())

