# -- Platform.py as part of FERS XML File I/O as part of FERS Plugin
# -- Created by James Gripper 
# -- November 2016
# -*- coding: utf-8 -*-#


from PyQt4 import QtCore, QtGui
from addNodes import *
from lxml import etree
import FERS_Input
import sys
import os

placeholder = open("filename.txt", "r")
filename = placeholder.read()
placeholder.close() 
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
        MainWindow.resize(537, 354)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout3 = QtGui.QHBoxLayout()
        self.horizontalLayout3.setObjectName(_fromUtf8("horizontalLayout3"))
        self.T_Pulse_label = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_label.setBaseSize(QtCore.QSize(7, 0))
        self.T_Pulse_label.setToolTip(_fromUtf8(""))
        self.T_Pulse_label.setObjectName(_fromUtf8("T_Pulse_label"))
        self.horizontalLayout3.addWidget(self.T_Pulse_label)
        self._2 = QtGui.QGridLayout()
        self._2.setObjectName(_fromUtf8("_2"))
        self.Plat_Remove_btn = QtGui.QPushButton(self.centralwidget)
        self.Plat_Remove_btn.setObjectName(_fromUtf8("Plat_Remove_btn"))
        self._2.addWidget(self.Plat_Remove_btn, 11, 1, 1, 1)
        self.Plat_Fixed_Rot_add_btn = QtGui.QPushButton(self.centralwidget)
        self.Plat_Fixed_Rot_add_btn.setObjectName(_fromUtf8("Plat_Fixed_Rot_add_btn"))
        self._2.addWidget(self.Plat_Fixed_Rot_add_btn, 4, 1, 1, 1)
        self.Plat_Motion_path_add_btn = QtGui.QPushButton(self.centralwidget)
        self.Plat_Motion_path_add_btn.setObjectName(_fromUtf8("Plat_Motion_path_add_btn"))
        self._2.addWidget(self.Plat_Motion_path_add_btn, 3, 1, 1, 1)
        self.T_Pulse_Carrier_label_3 = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_Carrier_label_3.setObjectName(_fromUtf8("T_Pulse_Carrier_label_3"))
        self._2.addWidget(self.T_Pulse_Carrier_label_3, 6, 0, 1, 1)
        self.T_Pulse_Carrier_label = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_Carrier_label.setObjectName(_fromUtf8("T_Pulse_Carrier_label"))
        self._2.addWidget(self.T_Pulse_Carrier_label, 4, 0, 1, 1)
        self.Plat_Rot_WayP_add_btn = QtGui.QPushButton(self.centralwidget)
        self.Plat_Rot_WayP_add_btn.setObjectName(_fromUtf8("Plat_Rot_WayP_add_btn"))
        self._2.addWidget(self.Plat_Rot_WayP_add_btn, 5, 1, 1, 1)
        self.T_Pulse_Carrier_label_2 = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_Carrier_label_2.setObjectName(_fromUtf8("T_Pulse_Carrier_label_2"))
        self._2.addWidget(self.T_Pulse_Carrier_label_2, 5, 0, 1, 1)
        self.T_Pulse_Carrier_label_4 = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_Carrier_label_4.setObjectName(_fromUtf8("T_Pulse_Carrier_label_4"))
        self._2.addWidget(self.T_Pulse_Carrier_label_4, 7, 0, 1, 1)
        self.T_Pulse_name_label = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_name_label.setObjectName(_fromUtf8("T_Pulse_name_label"))
        self._2.addWidget(self.T_Pulse_name_label, 0, 0, 1, 1)
        self.Plat_Target_add_btn = QtGui.QPushButton(self.centralwidget)
        self.Plat_Target_add_btn.setObjectName(_fromUtf8("Plat_Target_add_btn"))
        self._2.addWidget(self.Plat_Target_add_btn, 8, 1, 1, 1)
        self.T_Pulse_filename_clear = QtGui.QPushButton(self.centralwidget)
        self.T_Pulse_filename_clear.setObjectName(_fromUtf8("T_Pulse_filename_clear"))
        self._2.addWidget(self.T_Pulse_filename_clear, 0, 2, 1, 1)
        self.T_Pulse_power_label = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_power_label.setObjectName(_fromUtf8("T_Pulse_power_label"))
        self._2.addWidget(self.T_Pulse_power_label, 3, 0, 1, 1)
        self.T_Pulse_Carrier_label_5 = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_Carrier_label_5.setObjectName(_fromUtf8("T_Pulse_Carrier_label_5"))
        self._2.addWidget(self.T_Pulse_Carrier_label_5, 8, 0, 1, 1)
        self.Plat_Rx_add_btn = QtGui.QPushButton(self.centralwidget)
        self.Plat_Rx_add_btn.setObjectName(_fromUtf8("Plat_Rx_add_btn"))
        self._2.addWidget(self.Plat_Rx_add_btn, 7, 1, 1, 1)
        self.T_Pulse_Carrier_label_6 = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_Carrier_label_6.setObjectName(_fromUtf8("T_Pulse_Carrier_label_6"))
        self._2.addWidget(self.T_Pulse_Carrier_label_6, 9, 0, 1, 1)
        self.Plat_name_input = QtGui.QLineEdit(self.centralwidget)
        self.Plat_name_input.setObjectName(_fromUtf8("Plat_name_input"))
        self._2.addWidget(self.Plat_name_input, 0, 1, 1, 1)
        self.T_Pulse_Carrier_label_7 = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_Carrier_label_7.setObjectName(_fromUtf8("T_Pulse_Carrier_label_7"))
        self._2.addWidget(self.T_Pulse_Carrier_label_7, 10, 0, 1, 1)
        self.Plat_Tx_add_btn = QtGui.QPushButton(self.centralwidget)
        self.Plat_Tx_add_btn.setObjectName(_fromUtf8("Plat_Tx_add_btn"))
        self._2.addWidget(self.Plat_Tx_add_btn, 6, 1, 1, 1)
        self.Plat_Add_btn = QtGui.QPushButton(self.centralwidget)
        self.Plat_Add_btn.setObjectName(_fromUtf8("Plat_Add_btn"))
        self._2.addWidget(self.Plat_Add_btn, 1, 1, 1, 1)
        self.existing_platforms = QtGui.QComboBox(self.centralwidget)
        self.existing_platforms.setObjectName(_fromUtf8("existing_platforms"))
        self._2.addWidget(self.existing_platforms, 2, 1, 1, 1)
        self.T_Pulse_name_label_2 = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_name_label_2.setObjectName(_fromUtf8("T_Pulse_name_label_2"))
        self._2.addWidget(self.T_Pulse_name_label_2, 2, 0, 1, 1)
        self.platform_sel = QtGui.QComboBox(self.centralwidget)
        self.platform_sel.setObjectName(_fromUtf8("platform_sel"))
        self._2.addWidget(self.platform_sel, 10, 1, 1, 1)
        self._2.setColumnStretch(0, 8)
        self.horizontalLayout3.addLayout(self._2)
        self.verticalLayout.addLayout(self.horizontalLayout3)
        self.Plat_view_btn = QtGui.QPushButton(self.centralwidget)
        self.Plat_view_btn.setObjectName(_fromUtf8("Plat_view_btn"))
        self.verticalLayout.addWidget(self.Plat_view_btn)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.T_Pulse_filename_clear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Plat_name_input.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.Plat_name_input, self.Plat_Add_btn)
        MainWindow.setTabOrder(self.Plat_Add_btn, self.existing_platforms)
        MainWindow.setTabOrder(self.existing_platforms, self.Plat_Motion_path_add_btn)
        MainWindow.setTabOrder(self.Plat_Motion_path_add_btn, self.Plat_Fixed_Rot_add_btn)
        MainWindow.setTabOrder(self.Plat_Fixed_Rot_add_btn, self.Plat_Rot_WayP_add_btn)
        MainWindow.setTabOrder(self.Plat_Rot_WayP_add_btn, self.Plat_Tx_add_btn)
        MainWindow.setTabOrder(self.Plat_Tx_add_btn, self.Plat_Rx_add_btn)
        MainWindow.setTabOrder(self.Plat_Rx_add_btn, self.platform_sel)
        MainWindow.setTabOrder(self.platform_sel, self.Plat_Remove_btn)
        MainWindow.setTabOrder(self.Plat_Remove_btn, self.Plat_Remove_btn)
        MainWindow.setTabOrder(self.Plat_Remove_btn, self.T_Pulse_filename_clear)
        MainWindow.setTabOrder(self.T_Pulse_filename_clear, self.Plat_view_btn)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Platform", None))
        self.T_Pulse_label.setText(_translate("MainWindow", "Platform", None))
        self.Plat_Remove_btn.setText(_translate("MainWindow", "Remove from XML", None))
        self.Plat_Fixed_Rot_add_btn.setText(_translate("MainWindow", "Manage", None))
        self.Plat_Motion_path_add_btn.setText(_translate("MainWindow", "Manage", None))
        self.T_Pulse_Carrier_label_3.setText(_translate("MainWindow", "Transmitter", None))
        self.T_Pulse_Carrier_label.setText(_translate("MainWindow", "Fixed Rotation", None))
        self.Plat_Rot_WayP_add_btn.setText(_translate("MainWindow", "Manage", None))
        self.T_Pulse_Carrier_label_2.setText(_translate("MainWindow", "Rotation Waypoint", None))
        self.T_Pulse_Carrier_label_4.setText(_translate("MainWindow", "Receiver", None))
        self.T_Pulse_name_label.setText(_translate("MainWindow", "New Platform Name", None))
        self.Plat_Target_add_btn.setText(_translate("MainWindow", "Manage", None))
        self.T_Pulse_filename_clear.setText(_translate("MainWindow", "Clear", None))
        self.T_Pulse_power_label.setText(_translate("MainWindow", "Motion Path", None))
        self.T_Pulse_Carrier_label_5.setText(_translate("MainWindow", "Target", None))
        self.Plat_Rx_add_btn.setText(_translate("MainWindow", "Manage", None))
        self.T_Pulse_Carrier_label_6.setText(_translate("MainWindow", "Remove existing platform", None))
        self.Plat_name_input.setPlaceholderText(_translate("MainWindow", "<Sample Name>", None))
        self.T_Pulse_Carrier_label_7.setText(_translate("MainWindow", "Name", None))
        self.Plat_Tx_add_btn.setText(_translate("MainWindow", "Manage", None))
        self.Plat_Add_btn.setText(_translate("MainWindow", "Add to XML", None))
        self.T_Pulse_name_label_2.setText(_translate("MainWindow", "Existing Platforms", None))
        self.Plat_view_btn.setText(_translate("MainWindow", "View XML", None))

        self.Plat_Add_btn.clicked.connect(self.callAppend)
        self.Plat_view_btn.clicked.connect(self.showEntry)
        self.Plat_Remove_btn.clicked.connect(self.removeNode)    
        self.Plat_Motion_path_add_btn.clicked.connect(self.manageMPath)
        self.Plat_Fixed_Rot_add_btn.clicked.connect(self.manageFRotation)
        self.Plat_Rot_WayP_add_btn.clicked.connect(self.manageRWP)
        self.Plat_Tx_add_btn.clicked.connect(self.addTx)
        self.Plat_Rx_add_btn.clicked.connect(self.addRx)
        self.Plat_Target_add_btn.clicked.connect(self.addTarget)
        
        
    
        ## adds platform names to selection boxs
        self.platform_sel.clear()
        self.existing_platforms.clear()
        names = []
        doc = etree.parse(filename, parser)
        sim = doc.getroot()
        for plat in sim.findall('platform'):
            name = plat.get('name')
            names.append(name)
        for name in names:
            self.platform_sel.addItem(name)
            self.existing_platforms.addItem(name)
  
    ## calls motionpath to platform program    
    def manageMPath(self):
        doc = etree.parse(filename, parser)
        sim = doc.getroot()     
        platform = str(self.existing_platforms.currentText())
        for plat in sim.findall('platform'):
            name = plat.get('name')
            if platform == name:
                print '--Platform found!--'
                os.system('Motion_Path.py')
            else:
                print "--Platform not found--"   
    
    ## calls fixed rotation to platform program
    def manageFRotation(self):
        doc = etree.parse(filename, parser)
        sim = doc.getroot()     
        platform = str(self.existing_platforms.currentText())
        for plat in sim.findall('platform'):
            name = plat.get('name')
            if platform == name:      
                print '--Platform found!--'  
                os.system('Fixed_Rotation.py')  
            else:
                print "--Platform not found--"                  
            
    ## calls rotation waypoint to platform program
    def manageRWP(self):
        doc = etree.parse(filename, parser)
        sim = doc.getroot()     
        platform = str(self.existing_platforms.currentText())
        for plat in sim.findall('platform'):
            name = plat.get('name')
            if platform == name:      
                print '--Platform found!--'  
                os.system('Rotation_Waypoint.py')  
            else:
                print "--Platform not found--"          
        
    ## calls the receiver to platform program
    def addRx(self):
        doc = etree.parse(filename, parser)
        sim = doc.getroot()     
        platform = str(self.existing_platforms.currentText())
        for plat in sim.findall('platform'):
            name = plat.get('name')
            if platform == name:      
                print '--Platform found!--'  
                os.system('ReceiverPlat.py') 
            else:
                print "--Platform not found--"         
        
    ## calls transmitter to platform program    
    def addTx(self):
        doc = etree.parse(filename, parser)
        sim = doc.getroot()     
        platform = str(self.existing_platforms.currentText())
        for plat in sim.findall('platform'):
            name = plat.get('name')
            if platform == name:      
                print '--Platform found!--'  
                os.system('TransmitterPlat.py') 
            else:
                print "--Platform not found--"               

    ## calls target program   
    def addTarget(self):
        doc = etree.parse(filename, parser)
        sim = doc.getroot()     
        platform = str(self.existing_platforms.currentText())
        for plat in sim.findall('platform'):
            name = plat.get('name')
            if platform == name:      
                print '--Platform found!--'  
                os.system('TargetPlat.py')
            else:
                print "--Platform not found--"        
       
    ## removes chosen platform    
    def removeNode(self):
        doc = etree.parse(filename, parser)
        sim = doc.getroot()
        platform = str(self.platform_sel.currentText())
        for plat in sim.findall('platform'):
            name = plat.get('name')
            if name != platform:    
                print "--Platform not found--"
            else:
                sim.remove(plat)
                doc.write(filename,pretty_print=True)
                print '--Platform removed--'   
        self.platform_sel.clear()
        self.existing_platforms.clear()
        names = []
        doc = etree.parse(filename, parser)
        sim = doc.getroot()
        for plat in sim.findall('platform'):
            name = plat.get('name')
            names.append(name)
        for name in names:
            self.existing_platforms.addItem(name)
            self.platform_sel.addItem(name)        

    ## prints xml to console
    def showEntry(self):
        doc = etree.parse(filename, parser)
        print(etree.tostring(doc, pretty_print=True))       
    
    ## adds platform to simulation
    def callAppend(self):
        name = str(self.Plat_name_input.text())
        appendPlatform(filename, name)
        self.existing_platforms.clear()
        self.platform_sel.clear()
        names = []
        doc = etree.parse(filename, parser)
        sim = doc.getroot()
        for plat in sim.findall('platform'):
            name = plat.get('name')
            names.append(name)
        for name in names:
            self.platform_sel.addItem(name)
            self.existing_platforms.addItem(name)        

        print '--Platform added--'        

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

