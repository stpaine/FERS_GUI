# -- Rotation_Waypoint.py as part of FERS XML File I/O as part of FERS Plugin
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
        MainWindow.resize(481, 277)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout3 = QtGui.QHBoxLayout()
        self.horizontalLayout3.setObjectName(_fromUtf8("horizontalLayout3"))
        self._2 = QtGui.QGridLayout()
        self._2.setObjectName(_fromUtf8("_2"))
        self.T_Pulse_file_label_3 = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_file_label_3.setObjectName(_fromUtf8("T_Pulse_file_label_3"))
        self._2.addWidget(self.T_Pulse_file_label_3, 2, 0, 1, 1)
        self.T_Pulse_carrier_clear = QtGui.QPushButton(self.centralwidget)
        self.T_Pulse_carrier_clear.setObjectName(_fromUtf8("T_Pulse_carrier_clear"))
        self._2.addWidget(self.T_Pulse_carrier_clear, 1, 3, 1, 1)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self._2.addWidget(self.label_3, 1, 2, 1, 1)
        self.RWP_Remove_btn = QtGui.QPushButton(self.centralwidget)
        self.RWP_Remove_btn.setObjectName(_fromUtf8("RWP_Remove_btn"))
        self._2.addWidget(self.RWP_Remove_btn, 5, 3, 1, 1)
        self.T_Pulse_file_label_2 = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_file_label_2.setObjectName(_fromUtf8("T_Pulse_file_label_2"))
        self._2.addWidget(self.T_Pulse_file_label_2, 1, 0, 1, 1)
        self.T_Pulse_file_label_4 = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_file_label_4.setObjectName(_fromUtf8("T_Pulse_file_label_4"))
        self._2.addWidget(self.T_Pulse_file_label_4, 3, 0, 1, 1)
        self.T_Pulse_carrier_clear_2 = QtGui.QPushButton(self.centralwidget)
        self.T_Pulse_carrier_clear_2.setObjectName(_fromUtf8("T_Pulse_carrier_clear_2"))
        self._2.addWidget(self.T_Pulse_carrier_clear_2, 2, 3, 1, 1)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self._2.addWidget(self.label_4, 2, 2, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self._2.addWidget(self.label, 3, 2, 1, 1)
        self.T_Pulse_carrier_clear_3 = QtGui.QPushButton(self.centralwidget)
        self.T_Pulse_carrier_clear_3.setObjectName(_fromUtf8("T_Pulse_carrier_clear_3"))
        self._2.addWidget(self.T_Pulse_carrier_clear_3, 3, 3, 1, 1)
        self.FixedR_Azi_AV_input = QtGui.QLineEdit(self.centralwidget)
        self.FixedR_Azi_AV_input.setObjectName(_fromUtf8("FixedR_Azi_AV_input"))
        self._2.addWidget(self.FixedR_Azi_AV_input, 2, 1, 1, 1)
        self.Motion_Path_alt_input = QtGui.QLineEdit(self.centralwidget)
        self.Motion_Path_alt_input.setObjectName(_fromUtf8("Motion_Path_alt_input"))
        self._2.addWidget(self.Motion_Path_alt_input, 3, 1, 1, 1)
        self.RWP_elevation_angle_input = QtGui.QLineEdit(self.centralwidget)
        self.RWP_elevation_angle_input.setObjectName(_fromUtf8("RWP_elevation_angle_input"))
        self._2.addWidget(self.RWP_elevation_angle_input, 1, 1, 1, 1)
        self.RWP_Add_btn = QtGui.QPushButton(self.centralwidget)
        self.RWP_Add_btn.setObjectName(_fromUtf8("RWP_Add_btn"))
        self._2.addWidget(self.RWP_Add_btn, 4, 1, 1, 1)
        self.T_Pulse_file_label_6 = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_file_label_6.setObjectName(_fromUtf8("T_Pulse_file_label_6"))
        self._2.addWidget(self.T_Pulse_file_label_6, 5, 0, 1, 1)
        self.T_Pulse_file_label_5 = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_file_label_5.setObjectName(_fromUtf8("T_Pulse_file_label_5"))
        self._2.addWidget(self.T_Pulse_file_label_5, 0, 0, 1, 1)
        self.platform_sel = QtGui.QComboBox(self.centralwidget)
        self.platform_sel.setObjectName(_fromUtf8("platform_sel"))
        self._2.addWidget(self.platform_sel, 0, 1, 1, 3)
        self._2.setColumnStretch(0, 8)
        self.horizontalLayout3.addLayout(self._2)
        self.verticalLayout.addLayout(self.horizontalLayout3)
        self.RWP_View_btn = QtGui.QPushButton(self.centralwidget)
        self.RWP_View_btn.setObjectName(_fromUtf8("RWP_View_btn"))
        self.verticalLayout.addWidget(self.RWP_View_btn)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.T_Pulse_carrier_clear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.RWP_elevation_angle_input.clear)
        QtCore.QObject.connect(self.T_Pulse_carrier_clear_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.FixedR_Azi_AV_input.clear)
        QtCore.QObject.connect(self.T_Pulse_carrier_clear_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Motion_Path_alt_input.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.RWP_elevation_angle_input, self.FixedR_Azi_AV_input)
        MainWindow.setTabOrder(self.FixedR_Azi_AV_input, self.Motion_Path_alt_input)
        MainWindow.setTabOrder(self.Motion_Path_alt_input, self.RWP_Add_btn)
        MainWindow.setTabOrder(self.RWP_Add_btn, self.T_Pulse_carrier_clear)
        MainWindow.setTabOrder(self.T_Pulse_carrier_clear, self.T_Pulse_carrier_clear_2)
        MainWindow.setTabOrder(self.T_Pulse_carrier_clear_2, self.T_Pulse_carrier_clear_3)
        MainWindow.setTabOrder(self.T_Pulse_carrier_clear_3, self.RWP_Remove_btn)
        MainWindow.setTabOrder(self.RWP_Remove_btn, self.RWP_View_btn)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Rotation_Waypoint", None))
        self.T_Pulse_file_label_3.setText(_translate("MainWindow", "Azimuth Angle", None))
        self.T_Pulse_carrier_clear.setText(_translate("MainWindow", "Clear", None))
        self.label_3.setText(_translate("MainWindow", "degrees", None))
        self.RWP_Remove_btn.setText(_translate("MainWindow", "Remove from XML", None))
        self.T_Pulse_file_label_2.setText(_translate("MainWindow", "Elevation Angle", None))
        self.T_Pulse_file_label_4.setText(_translate("MainWindow", "Time ", None))
        self.T_Pulse_carrier_clear_2.setText(_translate("MainWindow", "Clear", None))
        self.label_4.setText(_translate("MainWindow", "m/s", None))
        self.label.setText(_translate("MainWindow", "seconds", None))
        self.T_Pulse_carrier_clear_3.setText(_translate("MainWindow", "Clear", None))
        self.FixedR_Azi_AV_input.setPlaceholderText(_translate("MainWindow", "<Sample Velocity>", None))
        self.Motion_Path_alt_input.setPlaceholderText(_translate("MainWindow", "<Sample Time>", None))
        self.RWP_elevation_angle_input.setPlaceholderText(_translate("MainWindow", "<Sample Value>", None))
        self.RWP_Add_btn.setText(_translate("MainWindow", "Add Rotation Waypoint", None))
        self.T_Pulse_file_label_6.setText(_translate("MainWindow", "Remove existing Rotation Waypoints", None))
        self.T_Pulse_file_label_5.setText(_translate("MainWindow", "Platform Name", None))
        self.RWP_View_btn.setText(_translate("MainWindow", "view XML", None))

    
        ## binding functions to buttons
        self.RWP_Add_btn.clicked.connect(self.callAppendWP)
        self.RWP_View_btn.clicked.connect(self.showEntry)
        self.RWP_Remove_btn.clicked.connect(self.removeNode)  
    
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
    
    ## removes Rotation Wapoint from platform       
    def removeNode(self):
        doc = etree.parse(filename, parser)
        sim = doc.getroot()
        tree=etree.ElementTree(sim)  
        for plat in sim.findall('platform'):
            name = plat.get('name')
            if name == str(self.platform_sel.currentText()):
                i = 0
                for rot in plat.findall('rotationwaypoint'):
                    i += 1
                    plat.remove(rot)
                    doc.write(filename,pretty_print=True)
                    print '--Rotation Waypoint removed--'  
                    if i > 0:
                        break
                    break
            else:
                print'--Invalid Platform. Please Try Again--'

    ## prints formatted xml to console
    def showEntry(self):
        doc = etree.parse(filename, parser)
        print(etree.tostring(doc, pretty_print=True))   

    ## adds Wapoint to motionpath and motionpath to platform
    def callAppendWP(self):
        el_angle = str(self.RWP_elevation_angle_input.text())
        azi_angle = str(self.FixedR_Azi_AV_input.text())
        t= str(self.Motion_Path_alt_input.text())
        plat_name = str(self.platform_sel.currentText())
        appendRotationWaypoint(filename,plat_name, el_angle, azi_angle, t)
        print '--Rotation Waypoint Added--'     


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

