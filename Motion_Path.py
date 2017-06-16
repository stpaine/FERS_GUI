# -- Motion_Path.py as part of FERS XML File I/O as part of FERS Plugin
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

class Ui_Motion_Path(QtGui.QMainWindow):

    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        
    def setupUi(self, Motion_Path):
        Motion_Path.setObjectName(_fromUtf8("Motion_Path"))
        Motion_Path.resize(614, 325)
        self.centralwidget = QtGui.QWidget(Motion_Path)
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
        self._2.addWidget(self.label_4, 6, 2, 1, 1)
        self.Motion_Path_X_input = QtGui.QLineEdit(self.centralwidget)
        self.Motion_Path_X_input.setObjectName(_fromUtf8("Motion_Path_X_input"))
        self._2.addWidget(self.Motion_Path_X_input, 5, 1, 1, 1)
        self.T_Pulse_carrier_clear = QtGui.QPushButton(self.centralwidget)
        self.T_Pulse_carrier_clear.setObjectName(_fromUtf8("T_Pulse_carrier_clear"))
        self._2.addWidget(self.T_Pulse_carrier_clear, 5, 3, 1, 1)
        self.T_Pulse_file_label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setUnderline(False)
        self.T_Pulse_file_label.setFont(font)
        self.T_Pulse_file_label.setObjectName(_fromUtf8("T_Pulse_file_label"))
        self._2.addWidget(self.T_Pulse_file_label, 4, 0, 1, 1)
        self.T_Pulse_carrier_clear_3 = QtGui.QPushButton(self.centralwidget)
        self.T_Pulse_carrier_clear_3.setObjectName(_fromUtf8("T_Pulse_carrier_clear_3"))
        self._2.addWidget(self.T_Pulse_carrier_clear_3, 7, 3, 1, 1)
        self.Motion_Path_Y_input = QtGui.QLineEdit(self.centralwidget)
        self.Motion_Path_Y_input.setObjectName(_fromUtf8("Motion_Path_Y_input"))
        self._2.addWidget(self.Motion_Path_Y_input, 6, 1, 1, 1)
        self.T_Pulse_file_label_6 = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_file_label_6.setObjectName(_fromUtf8("T_Pulse_file_label_6"))
        self._2.addWidget(self.T_Pulse_file_label_6, 11, 0, 1, 1)
        self.T_Pulse_file_label_2 = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_file_label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.T_Pulse_file_label_2.setObjectName(_fromUtf8("T_Pulse_file_label_2"))
        self._2.addWidget(self.T_Pulse_file_label_2, 5, 0, 1, 1)
        self.T_Pulse_file_label_5 = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_file_label_5.setObjectName(_fromUtf8("T_Pulse_file_label_5"))
        self._2.addWidget(self.T_Pulse_file_label_5, 8, 0, 1, 1)
        self.T_Pulse_file_label_4 = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_file_label_4.setObjectName(_fromUtf8("T_Pulse_file_label_4"))
        self._2.addWidget(self.T_Pulse_file_label_4, 7, 0, 1, 1)
        self.T_Pulse_name_label = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_name_label.setObjectName(_fromUtf8("T_Pulse_name_label"))
        self._2.addWidget(self.T_Pulse_name_label, 2, 0, 1, 1)
        self.Motion_Path_time_input = QtGui.QLineEdit(self.centralwidget)
        self.Motion_Path_time_input.setObjectName(_fromUtf8("Motion_Path_time_input"))
        self._2.addWidget(self.Motion_Path_time_input, 8, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self._2.addWidget(self.label_2, 8, 2, 1, 1)
        self.T_Pulse_name_label_2 = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_name_label_2.setObjectName(_fromUtf8("T_Pulse_name_label_2"))
        self._2.addWidget(self.T_Pulse_name_label_2, 0, 0, 1, 1)
        self.MP_Add_Interp_btn = QtGui.QPushButton(self.centralwidget)
        self.MP_Add_Interp_btn.setObjectName(_fromUtf8("MP_Add_Interp_btn"))
        self._2.addWidget(self.MP_Add_Interp_btn, 3, 1, 1, 3)
        self.T_Pulse_file_label_3 = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_file_label_3.setObjectName(_fromUtf8("T_Pulse_file_label_3"))
        self._2.addWidget(self.T_Pulse_file_label_3, 6, 0, 1, 1)
        self.Motion_Record_btn = QtGui.QPushButton(self.centralwidget)
        self.Motion_Record_btn.setObjectName(_fromUtf8("Motion_Record_btn"))
        self._2.addWidget(self.Motion_Record_btn, 11, 1, 1, 3)
        self.T_Pulse_carrier_clear_4 = QtGui.QPushButton(self.centralwidget)
        self.T_Pulse_carrier_clear_4.setObjectName(_fromUtf8("T_Pulse_carrier_clear_4"))
        self._2.addWidget(self.T_Pulse_carrier_clear_4, 8, 3, 1, 1)
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setEditable(True)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self._2.addWidget(self.comboBox, 2, 1, 1, 3)
        self.Motion_Path_AddW_btn = QtGui.QPushButton(self.centralwidget)
        self.Motion_Path_AddW_btn.setObjectName(_fromUtf8("Motion_Path_AddW_btn"))
        self._2.addWidget(self.Motion_Path_AddW_btn, 9, 1, 1, 3)
        self.T_Pulse_carrier_clear_2 = QtGui.QPushButton(self.centralwidget)
        self.T_Pulse_carrier_clear_2.setObjectName(_fromUtf8("T_Pulse_carrier_clear_2"))
        self._2.addWidget(self.T_Pulse_carrier_clear_2, 6, 3, 1, 1)
        self.Motion_Path_alt_input = QtGui.QLineEdit(self.centralwidget)
        self.Motion_Path_alt_input.setObjectName(_fromUtf8("Motion_Path_alt_input"))
        self._2.addWidget(self.Motion_Path_alt_input, 7, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self._2.addWidget(self.label_3, 5, 2, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self._2.addWidget(self.label, 7, 2, 1, 1)
        self.platform_sel = QtGui.QComboBox(self.centralwidget)
        self.platform_sel.setObjectName(_fromUtf8("platform_sel"))
        self._2.addWidget(self.platform_sel, 0, 1, 1, 1)
        self._2.setColumnStretch(0, 8)
        self.horizontalLayout3.addLayout(self._2)
        self.verticalLayout.addLayout(self.horizontalLayout3)
        self.Motion_Path_back_btn = QtGui.QPushButton(self.centralwidget)
        self.Motion_Path_back_btn.setObjectName(_fromUtf8("Motion_Path_back_btn"))
        self.verticalLayout.addWidget(self.Motion_Path_back_btn)
        Motion_Path.setCentralWidget(self.centralwidget)

        self.retranslateUi(Motion_Path)
        QtCore.QObject.connect(self.T_Pulse_carrier_clear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Motion_Path_X_input.clear)
        QtCore.QObject.connect(self.T_Pulse_carrier_clear_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Motion_Path_Y_input.clear)
        QtCore.QObject.connect(self.T_Pulse_carrier_clear_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Motion_Path_alt_input.clear)
        QtCore.QObject.connect(self.T_Pulse_carrier_clear_4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Motion_Path_time_input.clear)
        QtCore.QObject.connect(self.Motion_Path_AddW_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Motion_Path_time_input.clear)
        QtCore.QObject.connect(self.Motion_Path_AddW_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Motion_Path_alt_input.clear)
        QtCore.QObject.connect(self.Motion_Record_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Motion_Path_Y_input.clear)
        QtCore.QObject.connect(self.Motion_Record_btn, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Motion_Path_X_input.clear)
        QtCore.QMetaObject.connectSlotsByName(Motion_Path)
        Motion_Path.setTabOrder(self.platform_sel, self.comboBox)
        Motion_Path.setTabOrder(self.comboBox, self.MP_Add_Interp_btn)
        Motion_Path.setTabOrder(self.MP_Add_Interp_btn, self.Motion_Path_X_input)
        Motion_Path.setTabOrder(self.Motion_Path_X_input, self.Motion_Path_Y_input)
        Motion_Path.setTabOrder(self.Motion_Path_Y_input, self.Motion_Path_alt_input)
        Motion_Path.setTabOrder(self.Motion_Path_alt_input, self.Motion_Path_time_input)
        Motion_Path.setTabOrder(self.Motion_Path_time_input, self.Motion_Path_AddW_btn)
        Motion_Path.setTabOrder(self.Motion_Path_AddW_btn, self.Motion_Record_btn)
        Motion_Path.setTabOrder(self.Motion_Record_btn, self.T_Pulse_carrier_clear)
        Motion_Path.setTabOrder(self.T_Pulse_carrier_clear, self.T_Pulse_carrier_clear_2)
        Motion_Path.setTabOrder(self.T_Pulse_carrier_clear_2, self.T_Pulse_carrier_clear_3)
        Motion_Path.setTabOrder(self.T_Pulse_carrier_clear_3, self.T_Pulse_carrier_clear_4)
        Motion_Path.setTabOrder(self.T_Pulse_carrier_clear_4, self.Motion_Path_back_btn)

    def retranslateUi(self, Motion_Path):
        Motion_Path.setWindowTitle(_translate("Motion_Path", "Motion_Path", None))
        self.T_Pulse_label.setText(_translate("Motion_Path", "Motion Path", None))
        self.label_4.setText(_translate("Motion_Path", "meters", None))
        self.Motion_Path_X_input.setPlaceholderText(_translate("Motion_Path", "<Sample Value>", None))
        self.T_Pulse_carrier_clear.setText(_translate("Motion_Path", "Clear", None))
        self.T_Pulse_file_label.setText(_translate("Motion_Path", "Position Waypoint within above interpolation", None))
        self.T_Pulse_carrier_clear_3.setText(_translate("Motion_Path", "Clear", None))
        self.Motion_Path_Y_input.setPlaceholderText(_translate("Motion_Path", "<Sample Value>", None))
        self.T_Pulse_file_label_6.setText(_translate("Motion_Path", "Remove existing waypoints from above interpolation", None))
        self.T_Pulse_file_label_2.setText(_translate("Motion_Path", "X coord", None))
        self.T_Pulse_file_label_5.setText(_translate("Motion_Path", "Time", None))
        self.T_Pulse_file_label_4.setText(_translate("Motion_Path", "Altitude", None))
        self.T_Pulse_name_label.setText(_translate("Motion_Path", "Interpolation", None))
        self.Motion_Path_time_input.setPlaceholderText(_translate("Motion_Path", "<Sample Seconds>", None))
        self.label_2.setText(_translate("Motion_Path", "seconds", None))
        self.T_Pulse_name_label_2.setText(_translate("Motion_Path", "Platform Name", None))
        self.MP_Add_Interp_btn.setText(_translate("Motion_Path", "Add Interpolation type", None))
        self.T_Pulse_file_label_3.setText(_translate("Motion_Path", "Y coord", None))
        self.Motion_Record_btn.setText(_translate("Motion_Path", "Remove from XML", None))
        self.T_Pulse_carrier_clear_4.setText(_translate("Motion_Path", "Clear", None))
        self.comboBox.setItemText(0, _translate("Motion_Path", "Linear", None))
        self.comboBox.setItemText(1, _translate("Motion_Path", "Static", None))
        self.comboBox.setItemText(2, _translate("Motion_Path", "Cubic", None))
        self.comboBox.setItemText(3, _translate("Motion_Path", "Python", None))
        self.Motion_Path_AddW_btn.setText(_translate("Motion_Path", "Add Waypoint", None))
        self.T_Pulse_carrier_clear_2.setText(_translate("Motion_Path", "Clear", None))
        self.Motion_Path_alt_input.setPlaceholderText(_translate("Motion_Path", "<Sample Metres>", None))
        self.label_3.setText(_translate("Motion_Path", "meters", None))
        self.label.setText(_translate("Motion_Path", "metres", None))
        self.Motion_Path_back_btn.setText(_translate("Motion_Path", "View XML", None))

        ## connects functions to buttons
        self.Motion_Path_AddW_btn.clicked.connect(self.callAppendWP)
        self.Motion_Path_back_btn.clicked.connect(self.showEntry)
        self.Motion_Record_btn.clicked.connect(self.removeNode) 
        
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
            
    ## removes position waypoint from platform
    def removeNode(self):
        doc = etree.parse(filename, parser)
        sim = doc.getroot()
        tree=etree.ElementTree(sim)  
        for plat in sim.findall('platform'):
            name = plat.get('name')
            if name == str(self.Motion_Path_plat_name.text()):
                for rot in plat.findall('motionpath'):
                    i=0
                    type = rot.get('interpolation')
                    if type==str(self.comboBox.currentText()):
                        for pwp in rot.findall('positionwaypoint'):
                            i += 1
                            plat.remove(rot)
                            doc.write(filename,pretty_print=True)
                            print '--Position Waypoint removed from Platform--'  
                            if i > 0:
                                break
                            break
                    else:
                        print '--Invalid Interpolation Type--'
            else:
                print '--Invalid Platform Name. Please Try Again--'


    ## prints formatted xml to console
    def showEntry(self):
        doc = etree.parse(filename, parser)
        print(etree.tostring(doc, pretty_print=True))           

    ## adds Wapoint to motionpath and motionpath to platform
    def callAppendWP(self):
        x_val = str(self.Motion_Path_X_input.text())
        y_val = str(self.Motion_Path_Y_input.text())
        alt_val = str(self.Motion_Path_alt_input.text())
        t_val= str(self.Motion_Path_time_input.text())
        interp  = str(self.comboBox.currentText())
        plat_name = str(self.platform_sel.currentText()) 
        appendMotionPath(filename, plat_name, interp, x_val, y_val, alt_val, t_val)
        print '--Motion Path Added--'


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Motion_Path = QtGui.QMainWindow()
    ui = Ui_Motion_Path()
    ui.setupUi(Motion_Path)
    Motion_Path.show()
    sys.exit(app.exec_())

