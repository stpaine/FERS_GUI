#-- Visualiser 2.0 as part of FERS Plugin
# -- Created by James Gripper 
# -- November 2016
# -*- coding: utf-8 -*-#


from PyQt4 import QtCore, QtGui
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from geopy.distance import vincenty
import sys

def printf(format, *args):
    sys.stdout.write(format % args)
num_tx = str(0)    
num_rx = str(0)

a = []  ## stores tx names for drop downs
b = []  ## stores rx names for drop downs

num_transmitters = 0
num_receivers = 0

tx_names = []   ## tx names
rx_names = []   ## rx names

## tx arrays
tx     = []
ty     = []
tz     = []

## rx arrays
rx = []
ry = []
rz = []


## target arrays
rcs =''
ox = ['0']
oy = ['0']
oz = ['0']



## caluclates the distance between two coordinates on earth
def distance(x,y,x1, y1, x2, y2):
    x = (x1, y1)
    y = (x2, y2) 
    print(vincenty(x, y).kilometers)
    print 'kilometers'     
    
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
        MainWindow.resize(667, 847)
        MainWindow.setToolTip(_fromUtf8(""))
        MainWindow.setStatusTip(_fromUtf8(""))
        MainWindow.setWhatsThis(_fromUtf8(""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.FERS_Input_2 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FERS_Input_2.sizePolicy().hasHeightForWidth())
        self.FERS_Input_2.setSizePolicy(sizePolicy)
        self.FERS_Input_2.setBaseSize(QtCore.QSize(7, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.FERS_Input_2.setFont(font)
        self.FERS_Input_2.setObjectName(_fromUtf8("FERS_Input_2"))
        self.verticalLayout.addWidget(self.FERS_Input_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.Tx_Num = QtGui.QSpinBox(self.centralwidget)
        self.Tx_Num.setObjectName(_fromUtf8("Tx_Num"))
        self.horizontalLayout.addWidget(self.Tx_Num)
        self.tx_num_btn = QtGui.QPushButton(self.centralwidget)
        self.tx_num_btn.setObjectName(_fromUtf8("tx_num_btn"))
        self.horizontalLayout.addWidget(self.tx_num_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.Rx_Num = QtGui.QSpinBox(self.centralwidget)
        self.Rx_Num.setObjectName(_fromUtf8("Rx_Num"))
        self.horizontalLayout_2.addWidget(self.Rx_Num)
        self.rx_num_btn = QtGui.QPushButton(self.centralwidget)
        self.rx_num_btn.setObjectName(_fromUtf8("rx_num_btn"))
        self.horizontalLayout_2.addWidget(self.rx_num_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.line_6 = QtGui.QFrame(self.centralwidget)
        self.line_6.setFrameShape(QtGui.QFrame.HLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.verticalLayout.addWidget(self.line_6)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.T_Pulse_name_label_4 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.T_Pulse_name_label_4.sizePolicy().hasHeightForWidth())
        self.T_Pulse_name_label_4.setSizePolicy(sizePolicy)
        self.T_Pulse_name_label_4.setObjectName(_fromUtf8("T_Pulse_name_label_4"))
        self.horizontalLayout_4.addWidget(self.T_Pulse_name_label_4)
        self.rcs = QtGui.QLineEdit(self.centralwidget)
        self.rcs.setObjectName(_fromUtf8("rcs"))
        self.horizontalLayout_4.addWidget(self.rcs)
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout_4.addWidget(self.pushButton_2)
        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)
        self.horizontalLayout_21 = QtGui.QHBoxLayout()
        self.horizontalLayout_21.setObjectName(_fromUtf8("horizontalLayout_21"))
        self.pushButton_6 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.horizontalLayout_21.addWidget(self.pushButton_6)
        self.target_remove = QtGui.QPushButton(self.centralwidget)
        self.target_remove.setObjectName(_fromUtf8("target_remove"))
        self.horizontalLayout_21.addWidget(self.target_remove)
        self.gridLayout.addLayout(self.horizontalLayout_21, 5, 0, 1, 1)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.T_Pulse_name_label_6 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.T_Pulse_name_label_6.sizePolicy().hasHeightForWidth())
        self.T_Pulse_name_label_6.setSizePolicy(sizePolicy)
        self.T_Pulse_name_label_6.setObjectName(_fromUtf8("T_Pulse_name_label_6"))
        self.horizontalLayout_6.addWidget(self.T_Pulse_name_label_6)
        self.y = QtGui.QLineEdit(self.centralwidget)
        self.y.setObjectName(_fromUtf8("y"))
        self.horizontalLayout_6.addWidget(self.y)
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.horizontalLayout_6.addWidget(self.pushButton_4)
        self.gridLayout.addLayout(self.horizontalLayout_6, 3, 0, 1, 1)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.T_Pulse_name_label_7 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.T_Pulse_name_label_7.sizePolicy().hasHeightForWidth())
        self.T_Pulse_name_label_7.setSizePolicy(sizePolicy)
        self.T_Pulse_name_label_7.setObjectName(_fromUtf8("T_Pulse_name_label_7"))
        self.horizontalLayout_7.addWidget(self.T_Pulse_name_label_7)
        self.alt = QtGui.QLineEdit(self.centralwidget)
        self.alt.setObjectName(_fromUtf8("alt"))
        self.horizontalLayout_7.addWidget(self.alt)
        self.pushButton_5 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.horizontalLayout_7.addWidget(self.pushButton_5)
        self.gridLayout.addLayout(self.horizontalLayout_7, 4, 0, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.T_Pulse_name_label_5 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.T_Pulse_name_label_5.sizePolicy().hasHeightForWidth())
        self.T_Pulse_name_label_5.setSizePolicy(sizePolicy)
        self.T_Pulse_name_label_5.setBaseSize(QtCore.QSize(13, 0))
        self.T_Pulse_name_label_5.setObjectName(_fromUtf8("T_Pulse_name_label_5"))
        self.horizontalLayout_5.addWidget(self.T_Pulse_name_label_5)
        self.x = QtGui.QLineEdit(self.centralwidget)
        self.x.setObjectName(_fromUtf8("x"))
        self.horizontalLayout_5.addWidget(self.x)
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout_5.addWidget(self.pushButton_3)
        self.gridLayout.addLayout(self.horizontalLayout_5, 2, 0, 1, 1)
        self.T_Pulse_name_label_3 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.T_Pulse_name_label_3.setFont(font)
        self.T_Pulse_name_label_3.setObjectName(_fromUtf8("T_Pulse_name_label_3"))
        self.gridLayout.addWidget(self.T_Pulse_name_label_3, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.line_5 = QtGui.QFrame(self.centralwidget)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.verticalLayout.addWidget(self.line_5)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.T_Pulse_name_label_11 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.T_Pulse_name_label_11.setFont(font)
        self.T_Pulse_name_label_11.setObjectName(_fromUtf8("T_Pulse_name_label_11"))
        self.horizontalLayout_11.addWidget(self.T_Pulse_name_label_11)
        self.gridLayout_3.addLayout(self.horizontalLayout_11, 0, 0, 1, 1)
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.T_Pulse_name_label_16 = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_name_label_16.setObjectName(_fromUtf8("T_Pulse_name_label_16"))
        self.horizontalLayout_14.addWidget(self.T_Pulse_name_label_16)
        self.Rx_sel_3 = QtGui.QComboBox(self.centralwidget)
        self.Rx_sel_3.setObjectName(_fromUtf8("Rx_sel_3"))
        self.horizontalLayout_14.addWidget(self.Rx_sel_3)
        self.gridLayout_3.addLayout(self.horizontalLayout_14, 1, 0, 1, 1)
        self.horizontalLayout_18 = QtGui.QHBoxLayout()
        self.horizontalLayout_18.setObjectName(_fromUtf8("horizontalLayout_18"))
        self.T_Pulse_name_label_20 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.T_Pulse_name_label_20.sizePolicy().hasHeightForWidth())
        self.T_Pulse_name_label_20.setSizePolicy(sizePolicy)
        self.T_Pulse_name_label_20.setObjectName(_fromUtf8("T_Pulse_name_label_20"))
        self.horizontalLayout_18.addWidget(self.T_Pulse_name_label_20)
        self.tx_name = QtGui.QLineEdit(self.centralwidget)
        self.tx_name.setObjectName(_fromUtf8("tx_name"))
        self.horizontalLayout_18.addWidget(self.tx_name)
        self.pushButton_12 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_12.setObjectName(_fromUtf8("pushButton_12"))
        self.horizontalLayout_18.addWidget(self.pushButton_12)
        self.gridLayout_3.addLayout(self.horizontalLayout_18, 2, 0, 1, 1)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.T_Pulse_name_label_12 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.T_Pulse_name_label_12.sizePolicy().hasHeightForWidth())
        self.T_Pulse_name_label_12.setSizePolicy(sizePolicy)
        self.T_Pulse_name_label_12.setObjectName(_fromUtf8("T_Pulse_name_label_12"))
        self.horizontalLayout_12.addWidget(self.T_Pulse_name_label_12)
        self.tx_x = QtGui.QLineEdit(self.centralwidget)
        self.tx_x.setObjectName(_fromUtf8("tx_x"))
        self.horizontalLayout_12.addWidget(self.tx_x)
        self.pushButton_9 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.horizontalLayout_12.addWidget(self.pushButton_9)
        self.gridLayout_3.addLayout(self.horizontalLayout_12, 3, 0, 1, 1)
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        self.T_Pulse_name_label_17 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.T_Pulse_name_label_17.sizePolicy().hasHeightForWidth())
        self.T_Pulse_name_label_17.setSizePolicy(sizePolicy)
        self.T_Pulse_name_label_17.setObjectName(_fromUtf8("T_Pulse_name_label_17"))
        self.horizontalLayout_15.addWidget(self.T_Pulse_name_label_17)
        self.tx_y = QtGui.QLineEdit(self.centralwidget)
        self.tx_y.setObjectName(_fromUtf8("tx_y"))
        self.horizontalLayout_15.addWidget(self.tx_y)
        self.pushButton_10 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
        self.horizontalLayout_15.addWidget(self.pushButton_10)
        self.gridLayout_3.addLayout(self.horizontalLayout_15, 4, 0, 1, 1)
        self.horizontalLayout_23 = QtGui.QHBoxLayout()
        self.horizontalLayout_23.setObjectName(_fromUtf8("horizontalLayout_23"))
        self.T_Pulse_name_label_21 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.T_Pulse_name_label_21.sizePolicy().hasHeightForWidth())
        self.T_Pulse_name_label_21.setSizePolicy(sizePolicy)
        self.T_Pulse_name_label_21.setObjectName(_fromUtf8("T_Pulse_name_label_21"))
        self.horizontalLayout_23.addWidget(self.T_Pulse_name_label_21)
        self.tx_z = QtGui.QLineEdit(self.centralwidget)
        self.tx_z.setObjectName(_fromUtf8("tx_z"))
        self.horizontalLayout_23.addWidget(self.tx_z)
        self.pushButton_14 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_14.setObjectName(_fromUtf8("pushButton_14"))
        self.horizontalLayout_23.addWidget(self.pushButton_14)
        self.gridLayout_3.addLayout(self.horizontalLayout_23, 5, 0, 1, 1)
        self.horizontalLayout_19 = QtGui.QHBoxLayout()
        self.horizontalLayout_19.setObjectName(_fromUtf8("horizontalLayout_19"))
        self.tx_record = QtGui.QPushButton(self.centralwidget)
        self.tx_record.setObjectName(_fromUtf8("tx_record"))
        self.horizontalLayout_19.addWidget(self.tx_record)
        self.tx_remove = QtGui.QPushButton(self.centralwidget)
        self.tx_remove.setObjectName(_fromUtf8("tx_remove"))
        self.horizontalLayout_19.addWidget(self.tx_remove)
        self.gridLayout_3.addLayout(self.horizontalLayout_19, 6, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.T_Pulse_name_label_8 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.T_Pulse_name_label_8.setFont(font)
        self.T_Pulse_name_label_8.setObjectName(_fromUtf8("T_Pulse_name_label_8"))
        self.horizontalLayout_8.addWidget(self.T_Pulse_name_label_8)
        self.gridLayout_2.addLayout(self.horizontalLayout_8, 0, 0, 1, 1)
        self.horizontalLayout_17 = QtGui.QHBoxLayout()
        self.horizontalLayout_17.setObjectName(_fromUtf8("horizontalLayout_17"))
        self.T_Pulse_name_label_19 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.T_Pulse_name_label_19.sizePolicy().hasHeightForWidth())
        self.T_Pulse_name_label_19.setSizePolicy(sizePolicy)
        self.T_Pulse_name_label_19.setObjectName(_fromUtf8("T_Pulse_name_label_19"))
        self.horizontalLayout_17.addWidget(self.T_Pulse_name_label_19)
        self.rx_name = QtGui.QLineEdit(self.centralwidget)
        self.rx_name.setObjectName(_fromUtf8("rx_name"))
        self.horizontalLayout_17.addWidget(self.rx_name)
        self.pushButton_11 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))
        self.horizontalLayout_17.addWidget(self.pushButton_11)
        self.gridLayout_2.addLayout(self.horizontalLayout_17, 2, 0, 1, 1)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.T_Pulse_name_label_9 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.T_Pulse_name_label_9.sizePolicy().hasHeightForWidth())
        self.T_Pulse_name_label_9.setSizePolicy(sizePolicy)
        self.T_Pulse_name_label_9.setObjectName(_fromUtf8("T_Pulse_name_label_9"))
        self.horizontalLayout_9.addWidget(self.T_Pulse_name_label_9)
        self.rx_x = QtGui.QLineEdit(self.centralwidget)
        self.rx_x.setObjectName(_fromUtf8("rx_x"))
        self.horizontalLayout_9.addWidget(self.rx_x)
        self.pushButton_7 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.horizontalLayout_9.addWidget(self.pushButton_7)
        self.gridLayout_2.addLayout(self.horizontalLayout_9, 3, 0, 1, 1)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.T_Pulse_name_label_10 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.T_Pulse_name_label_10.sizePolicy().hasHeightForWidth())
        self.T_Pulse_name_label_10.setSizePolicy(sizePolicy)
        self.T_Pulse_name_label_10.setObjectName(_fromUtf8("T_Pulse_name_label_10"))
        self.horizontalLayout_10.addWidget(self.T_Pulse_name_label_10)
        self.rx_y = QtGui.QLineEdit(self.centralwidget)
        self.rx_y.setObjectName(_fromUtf8("rx_y"))
        self.horizontalLayout_10.addWidget(self.rx_y)
        self.pushButton_8 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.horizontalLayout_10.addWidget(self.pushButton_8)
        self.gridLayout_2.addLayout(self.horizontalLayout_10, 4, 0, 1, 1)
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.T_Pulse_name_label_18 = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_name_label_18.setObjectName(_fromUtf8("T_Pulse_name_label_18"))
        self.horizontalLayout_13.addWidget(self.T_Pulse_name_label_18)
        self.Rx_sel_2 = QtGui.QComboBox(self.centralwidget)
        self.Rx_sel_2.setObjectName(_fromUtf8("Rx_sel_2"))
        self.horizontalLayout_13.addWidget(self.Rx_sel_2)
        self.gridLayout_2.addLayout(self.horizontalLayout_13, 1, 0, 1, 1)
        self.horizontalLayout_20 = QtGui.QHBoxLayout()
        self.horizontalLayout_20.setObjectName(_fromUtf8("horizontalLayout_20"))
        self.rx_record = QtGui.QPushButton(self.centralwidget)
        self.rx_record.setObjectName(_fromUtf8("rx_record"))
        self.horizontalLayout_20.addWidget(self.rx_record)
        self.rx_remove = QtGui.QPushButton(self.centralwidget)
        self.rx_remove.setEnabled(True)
        self.rx_remove.setStatusTip(_fromUtf8(""))
        self.rx_remove.setWhatsThis(_fromUtf8(""))
        self.rx_remove.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.rx_remove.setObjectName(_fromUtf8("rx_remove"))
        self.horizontalLayout_20.addWidget(self.rx_remove)
        self.gridLayout_2.addLayout(self.horizontalLayout_20, 6, 0, 1, 1)
        self.horizontalLayout_22 = QtGui.QHBoxLayout()
        self.horizontalLayout_22.setObjectName(_fromUtf8("horizontalLayout_22"))
        self.T_Pulse_name_label_15 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.T_Pulse_name_label_15.sizePolicy().hasHeightForWidth())
        self.T_Pulse_name_label_15.setSizePolicy(sizePolicy)
        self.T_Pulse_name_label_15.setObjectName(_fromUtf8("T_Pulse_name_label_15"))
        self.horizontalLayout_22.addWidget(self.T_Pulse_name_label_15)
        self.rx_z = QtGui.QLineEdit(self.centralwidget)
        self.rx_z.setObjectName(_fromUtf8("rx_z"))
        self.horizontalLayout_22.addWidget(self.rx_z)
        self.pushButton_13 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_13.setObjectName(_fromUtf8("pushButton_13"))
        self.horizontalLayout_22.addWidget(self.pushButton_13)
        self.gridLayout_2.addLayout(self.horizontalLayout_22, 5, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout.addWidget(self.line_2)
        self.View_btn = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.View_btn.setFont(font)
        self.View_btn.setObjectName(_fromUtf8("View_btn"))
        self.verticalLayout.addWidget(self.View_btn)
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.verticalLayout.addWidget(self.line_3)
        self.horizontalLayout_16 = QtGui.QHBoxLayout()
        self.horizontalLayout_16.setObjectName(_fromUtf8("horizontalLayout_16"))
        self.T_Pulse_name_label_2 = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_name_label_2.setObjectName(_fromUtf8("T_Pulse_name_label_2"))
        self.horizontalLayout_16.addWidget(self.T_Pulse_name_label_2)
        self.Tx_sel = QtGui.QComboBox(self.centralwidget)
        self.Tx_sel.setObjectName(_fromUtf8("Tx_sel"))
        self.horizontalLayout_16.addWidget(self.Tx_sel)
        self.T_Pulse_name_label_13 = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_name_label_13.setObjectName(_fromUtf8("T_Pulse_name_label_13"))
        self.horizontalLayout_16.addWidget(self.T_Pulse_name_label_13)
        self.Rx_sel = QtGui.QComboBox(self.centralwidget)
        self.Rx_sel.setObjectName(_fromUtf8("Rx_sel"))
        self.horizontalLayout_16.addWidget(self.Rx_sel)
        self.T_Pulse_name_label_14 = QtGui.QLabel(self.centralwidget)
        self.T_Pulse_name_label_14.setObjectName(_fromUtf8("T_Pulse_name_label_14"))
        self.horizontalLayout_16.addWidget(self.T_Pulse_name_label_14)
        self.distance_calc = QtGui.QPushButton(self.centralwidget)
        self.distance_calc.setObjectName(_fromUtf8("distance_calc"))
        self.horizontalLayout_16.addWidget(self.distance_calc)
        self.verticalLayout.addLayout(self.horizontalLayout_16)
        self.line_4 = QtGui.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.verticalLayout.addWidget(self.line_4)
        self.show = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.show.setFont(font)
        self.show.setObjectName(_fromUtf8("show"))
        self.verticalLayout.addWidget(self.show)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.rcs.clear)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.x.clear)
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.y.clear)
        QtCore.QObject.connect(self.pushButton_5, QtCore.SIGNAL(_fromUtf8("clicked()")), self.alt.clear)
        QtCore.QObject.connect(self.pushButton_11, QtCore.SIGNAL(_fromUtf8("clicked()")), self.rx_name.clear)
        QtCore.QObject.connect(self.pushButton_7, QtCore.SIGNAL(_fromUtf8("clicked()")), self.rx_x.clear)
        QtCore.QObject.connect(self.pushButton_8, QtCore.SIGNAL(_fromUtf8("clicked()")), self.rx_y.clear)
        QtCore.QObject.connect(self.pushButton_12, QtCore.SIGNAL(_fromUtf8("clicked()")), self.tx_name.clear)
        QtCore.QObject.connect(self.pushButton_9, QtCore.SIGNAL(_fromUtf8("clicked()")), self.tx_x.clear)
        QtCore.QObject.connect(self.pushButton_10, QtCore.SIGNAL(_fromUtf8("clicked()")), self.tx_y.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.Tx_Num, self.tx_num_btn)
        MainWindow.setTabOrder(self.tx_num_btn, self.Rx_Num)
        MainWindow.setTabOrder(self.Rx_Num, self.rx_num_btn)
        MainWindow.setTabOrder(self.rx_num_btn, self.rcs)
        MainWindow.setTabOrder(self.rcs, self.pushButton_2)
        MainWindow.setTabOrder(self.pushButton_2, self.x)
        MainWindow.setTabOrder(self.x, self.pushButton_3)
        MainWindow.setTabOrder(self.pushButton_3, self.y)
        MainWindow.setTabOrder(self.y, self.pushButton_4)
        MainWindow.setTabOrder(self.pushButton_4, self.alt)
        MainWindow.setTabOrder(self.alt, self.pushButton_5)
        MainWindow.setTabOrder(self.pushButton_5, self.pushButton_6)
        MainWindow.setTabOrder(self.pushButton_6, self.target_remove)
        MainWindow.setTabOrder(self.target_remove, self.Rx_sel_3)
        MainWindow.setTabOrder(self.Rx_sel_3, self.tx_name)
        MainWindow.setTabOrder(self.tx_name, self.pushButton_12)
        MainWindow.setTabOrder(self.pushButton_12, self.tx_x)
        MainWindow.setTabOrder(self.tx_x, self.pushButton_9)
        MainWindow.setTabOrder(self.pushButton_9, self.tx_y)
        MainWindow.setTabOrder(self.tx_y, self.pushButton_10)
        MainWindow.setTabOrder(self.pushButton_10, self.tx_record)
        MainWindow.setTabOrder(self.tx_record, self.tx_remove)
        MainWindow.setTabOrder(self.tx_remove, self.Rx_sel_2)
        MainWindow.setTabOrder(self.Rx_sel_2, self.rx_name)
        MainWindow.setTabOrder(self.rx_name, self.pushButton_11)
        MainWindow.setTabOrder(self.pushButton_11, self.rx_x)
        MainWindow.setTabOrder(self.rx_x, self.pushButton_7)
        MainWindow.setTabOrder(self.pushButton_7, self.rx_y)
        MainWindow.setTabOrder(self.rx_y, self.pushButton_8)
        MainWindow.setTabOrder(self.pushButton_8, self.rx_record)
        MainWindow.setTabOrder(self.rx_record, self.rx_remove)
        MainWindow.setTabOrder(self.rx_remove, self.View_btn)
        MainWindow.setTabOrder(self.View_btn, self.Tx_sel)
        MainWindow.setTabOrder(self.Tx_sel, self.Rx_sel)
        MainWindow.setTabOrder(self.Rx_sel, self.distance_calc)
        MainWindow.setTabOrder(self.distance_calc, self.show)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "FERS Based Radar Visualiser", None))
        self.FERS_Input_2.setText(_translate("MainWindow", "FERS Based Radar Visualiser - Cartesian Coordinate System", None))
        self.label.setText(_translate("MainWindow", "Number of Transmitters", None))
        self.tx_num_btn.setText(_translate("MainWindow", "Set", None))
        self.label_2.setText(_translate("MainWindow", "Number of Receivers", None))
        self.rx_num_btn.setText(_translate("MainWindow", "Set", None))
        self.T_Pulse_name_label_4.setText(_translate("MainWindow", "RCS Value:", None))
        self.rcs.setPlaceholderText(_translate("MainWindow", "< Sample Value (m^2) >", None))
        self.pushButton_2.setText(_translate("MainWindow", "Clear", None))
        self.pushButton_6.setText(_translate("MainWindow", "Record Target Info", None))
        self.target_remove.setToolTip(_translate("MainWindow", "<html><head/><body><p>Remove the target from the environment.</p></body></html>", None))
        self.target_remove.setText(_translate("MainWindow", "Remove Target", None))
        self.T_Pulse_name_label_6.setText(_translate("MainWindow", "Y Value:", None))
        self.y.setPlaceholderText(_translate("MainWindow", "< Sample Metres >", None))
        self.pushButton_4.setText(_translate("MainWindow", "Clear", None))
        self.T_Pulse_name_label_7.setText(_translate("MainWindow", "Z Value:", None))
        self.alt.setPlaceholderText(_translate("MainWindow", "< Sample Metres >", None))
        self.pushButton_5.setText(_translate("MainWindow", "Clear", None))
        self.T_Pulse_name_label_5.setText(_translate("MainWindow", "X Value:", None))
        self.x.setPlaceholderText(_translate("MainWindow", "< Sample Metres >", None))
        self.pushButton_3.setText(_translate("MainWindow", "Clear", None))
        self.T_Pulse_name_label_3.setText(_translate("MainWindow", "Target information entry:", None))
        self.T_Pulse_name_label_11.setText(_translate("MainWindow", "Transmitter information entry", None))
        self.T_Pulse_name_label_16.setText(_translate("MainWindow", "Transmitter number:", None))
        self.T_Pulse_name_label_20.setText(_translate("MainWindow", "Name:", None))
        self.tx_name.setPlaceholderText(_translate("MainWindow", "< Sample Name >", None))
        self.pushButton_12.setText(_translate("MainWindow", "Clear", None))
        self.T_Pulse_name_label_12.setText(_translate("MainWindow", "X Value:", None))
        self.tx_x.setPlaceholderText(_translate("MainWindow", "< Sample Metres >", None))
        self.pushButton_9.setText(_translate("MainWindow", "Clear", None))
        self.T_Pulse_name_label_17.setText(_translate("MainWindow", "Y Value:", None))
        self.tx_y.setPlaceholderText(_translate("MainWindow", "< Sample Metres >", None))
        self.pushButton_10.setText(_translate("MainWindow", "Clear", None))
        self.T_Pulse_name_label_21.setText(_translate("MainWindow", "Z Value:", None))
        self.tx_z.setPlaceholderText(_translate("MainWindow", "< Sample Metres >", None))
        self.pushButton_14.setText(_translate("MainWindow", "Clear", None))
        self.tx_record.setText(_translate("MainWindow", "Record Transmitter info", None))
        self.tx_remove.setToolTip(_translate("MainWindow", "<html><head/><body><p>Removes transmitter corresponding to the selected number.</p></body></html>", None))
        self.tx_remove.setText(_translate("MainWindow", "Remove Transmitter", None))
        self.T_Pulse_name_label_8.setText(_translate("MainWindow", "Receiver information entry", None))
        self.T_Pulse_name_label_19.setText(_translate("MainWindow", "Name:", None))
        self.rx_name.setPlaceholderText(_translate("MainWindow", "< Sample Name >", None))
        self.pushButton_11.setText(_translate("MainWindow", "Clear", None))
        self.T_Pulse_name_label_9.setText(_translate("MainWindow", "X Value:", None))
        self.rx_x.setPlaceholderText(_translate("MainWindow", "< Sample Metres >", None))
        self.pushButton_7.setText(_translate("MainWindow", "Clear", None))
        self.T_Pulse_name_label_10.setText(_translate("MainWindow", "Y Value:", None))
        self.rx_y.setPlaceholderText(_translate("MainWindow", "< Sample Metres >", None))
        self.pushButton_8.setText(_translate("MainWindow", "Clear", None))
        self.T_Pulse_name_label_18.setText(_translate("MainWindow", "Receiver number:", None))
        self.rx_record.setText(_translate("MainWindow", "Record Receiver Info", None))
        self.rx_remove.setToolTip(_translate("MainWindow", "<html><head/><body><p>Removes the receiver corresponding to the selected number.</p></body></html>", "sdfssfsdf"))
        self.rx_remove.setText(_translate("MainWindow", "Remove Receiver", None))
        self.T_Pulse_name_label_15.setText(_translate("MainWindow", "Z Value:", None))
        self.rx_z.setPlaceholderText(_translate("MainWindow", "< Sample Metres >", None))
        self.pushButton_13.setText(_translate("MainWindow", "Clear", None))
        self.View_btn.setText(_translate("MainWindow", "View Input Data ", None))
        self.T_Pulse_name_label_2.setText(_translate("MainWindow", "Distance between:", None))
        self.T_Pulse_name_label_13.setText(_translate("MainWindow", "tx and", None))
        self.T_Pulse_name_label_14.setText(_translate("MainWindow", "rx in kiometers", None))
        self.distance_calc.setText(_translate("MainWindow", "Calculate", None))
        self.show.setText(_translate("MainWindow", "Show Visualisation", None))
  
        self.tx_remove.clicked.connect(self.removeTransmitter)
        self.target_remove.clicked.connect(self.removeTarget)
        self.rx_remove.clicked.connect(self.removeReceiver)
        self.pushButton_6.clicked.connect(self.addTarget)
        self.tx_record.clicked.connect(self.addTransmitter)
        self.rx_record.clicked.connect(self.addReceiver)
        self.tx_num_btn.clicked.connect(self.setTxNum)
        self.rx_num_btn.clicked.connect(self.setRxNum)
        self.show.clicked.connect(self.generatePlot)
        self.View_btn.clicked.connect(self.showEnvironment)
        self.distance_calc.clicked.connect(self.showDistance)
        
    
    ##generates 3d plot in degrees    
    def generatePlot(self):
        tx_val=[]
        ty_val=[]
        tz_val=[]
        rx_val=[]
        ry_val=[]
        rz_val=[]
        ox_val=[]
        oy_val=[]
        oz_val=[]
        ## figure object which plots are added to
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        for i in range(len(tx)):
            try:
                ##adding integer values to tx arrays
                tx_val.insert(i,float(tx[i]))
                ty_val.insert(i,float(ty[i]))
                tz_val.insert(i,float(tz[i]))
            except ValueError:
                print '--Please insert correct transmitter information--'
                return
            
        ## create scatter plot for transmitters within ax, which is in fig
        ax.scatter(tx_val, ty_val, tz_val, c='yellow', depthshade=False, marker='o', label='transmitters')
            
        for j in range(len(rx)):
            ##adding integer values to rx arrays
            rx_val.insert(j,float(rx[j]))
            ry_val.insert(j,float(ry[j]))
            rz_val.insert(j,float(rz[j]))
        
        ## create scatter plot for receivers within ax, which is in fig   
        ax.scatter(rx_val, ry_val, rz_val, c='blue',depthshade=False, marker='o', label='receivers')
        
        ##adding integer values to target arrays
        ox_val.insert(0,float(ox[0]))
        oy_val.insert(0,float(oy[0]))
        oz_val.insert(0,float(oz[0]))  
        
        ## create scatter plot for target within ax, which is in fig   
        ax.scatter(ox_val, oy_val, oz_val, c='red',depthshade=False, marker='o', label = 'targets')
        
        ## create straight lines between tx positions and target
        for i in range(len(tx_val)):
            ax.plot([tx_val[i],ox_val[0]],[ty_val[i],oy_val[0]],[tz_val[i],oz_val[0]], c = 'b')
        
        ## create straight lines between rx positions and target
        for i in range(len(rx_val)):
            ax.plot([rx_val[i],ox_val[0]],[ry_val[i],oy_val[0]],[rz_val[i],oz_val[0]], c='g')
    
        ## axis labels
        ax.set_xlabel('Longitude (m)') 
        ax.set_ylabel('Latitude (m)')
        ax.set_zlabel('Height (m)')
        
        plt.legend(loc='upper left') ## legend and position
        
        plt.show()
                
    ## sets number of transmitters in environment    
    def setTxNum(self): 
        val = str(self.Tx_Num.text())
        self.Rx_sel_3.clear()
        self.Tx_sel.clear()
        
        ## a[] keeps record of the transmitter numbers. num_tx string populates a[]
        if (int(val)>len(a)):
            dif = (int(val)-len(a))
            for i in range(dif):
                global num_tx
                a.append(num_tx)
                lol = int(num_tx) +1
                num_tx=str(lol) ## increment num_tx
                tx.insert(i+dif, '')
                ty.insert(i+dif, '')
                tz.insert(i+dif, '')
                tx_names.insert(i,'')
        elif(int(val)<len(a)):
            while int(val)<len(a):
                lol = int(num_tx) -1
                num_tx = str(lol) ## decrement num_tx
                a.pop(len(a)-1)
                tx.pop(len(a))
                ty.pop(len(a))
                tz.pop(len(a))
                tx_names.pop(len(a))
        
        ##adds names to dropdown box        
        for i in range(len(a)):
            self.Rx_sel_3.addItem(a[i])
            self.Tx_sel.addItem(a[i])
            
        print '--Number of transmitters set--'
        
   
    ## sets number of receivers in environment    
    def setRxNum(self):
        
        val = str(self.Rx_Num.text())
        self.Rx_sel_2.clear()
        self.Rx_sel.clear()
        
        ## b[] keeps record of the transmitter numbers. num_rx string populates b[]
        if (int(val)>len(b)):
            dif = (int(val)-len(b))
            for i in range(dif):
                ##num_rx used for drop downs
                global num_rx
                b.append(num_rx)
                lol = int(num_rx) +1
                num_rx=str(lol) ## increment num_rx
                ##inserting blanks into rx
                rx.insert(i+dif, '')
                ry.insert(i+dif, '')
                rz.insert(i+dif, '')
                rx_names.insert(i+dif,'')
        elif(int(val)<len(b)):
            wiz = len(b)-int(val)
            for i in range(wiz):
                lol = int(num_rx) -1
                num_rx = str(lol)## decrement num_tx
                b.pop(len(b)-1)
                rx.pop(len(b))
                ry.pop(len(b))
                rz.pop(len(b))
                rx_names.pop(len(b))
        
        ##adds names to dropdown box
        for i in range(len(b)):
            self.Rx_sel_2.addItem(b[i])
            self.Rx_sel.addItem(b[i])
    
        print '--Number of receiver set--'
    
     
        
        
    ## removes recveivers from rx[], ry[], rz[], rz_names[]
    def removeReceiver(self):
        
        num = str(self.Rx_sel_2.currentText())
        try:
            rx_names[int(num)]='' ##removes name of receiver from rx_names
            rx[int(num)] = '' ##removes longitude of receiver
            ry[int(num)] = ''   ##removes latitude of receiver
            rz[int(num)] = ''  ##removes altitude of receiver

            print'--Receiver Removed--'
        except KeyError:
            print'--Please select correct receiver to remove--'
    
    ## removes transmitter from environment
    def removeTransmitter(self):
        num = str(self.Rx_sel_3.currentText())
        try:
            tx_names[int(num)]='' ##removes name of transmitter from tx_names
            tx[int(num)] = '' ##removes longitude of transmitter
            ty[int(num)] = ''   ##removes latitude of transmitter
            tz[int(num)] = ''  ##removes altitude of transmitter
            
            print'--Receiver Removed--'
        except KeyError:
            print'--Please select correct receiver to remove--'           

    ## removes target from environment
    def removeTarget(self):
        rcs = ''
        ox[0]=['']
        oy[0]=['']
        oz[0]=['']
        print'--Target Removed--' 
    
    ## removes receiver from environment    
    def addReceiver(self):
        num = str(self.Rx_sel_2.currentText())
        name = str(self.rx_name.text())
        rx_names[int(num)]=name
        longi = str(self.rx_x.text())
        lat = str(self.rx_y.text())
        z = str(self.rx_z.text())
        
        rx[int(num)]=longi          ##sets rx x value in metres
        ry[int(num)]=lat            ##sets rx y value in metres
        rz[int(num)] = z            ##sets rx z value in metres 

        print'--Receiver Added--'
    
    ## adds transmitter to environment
    def addTransmitter(self):
        num = str(self.Rx_sel_3.currentText())
        name = str(self.tx_name.text())
        
        tx_names[int(num)]=name
        longi = str(self.tx_x.text())
        lat = str(self.tx_y.text())
        z = str(self.tx_z.text())
        
        tx[int(num)]=longi          ##sets tx x value in metres
        ty[int(num)]=lat            ##sets tx y value in metres
        tz[int(num)] = z            ##sets tx z value in metres
        ##add tx to array at position num
        print'--Transmitter Added--'    

    ## adds target to environment
    def addTarget(self):
        global rcs
        rcs = str(self.rcs.text())
        longit = str(self.x.text())
        latt = str(self.y.text())
        alti = str(self.alt.text())
        ox[0]=longit    ## target x value in metres
        oy[0]=latt      ## target y value in metres
        oz[0]=alti      ## target z value in metres
      
        print'--Target Added--'
   
      
    
    def showDistance(self):
        t = str(self.Tx_sel.currentText())
        print t
        r = str(self.Rx_sel.currentText())
        print r
        try:
            x1 = float(tx[int(t)])
            y1 = float(ty[int(t)])
            x2 = float(rx[int(r)])
            y2 = float(ry[int(r)])
            
            distance(t, r, x1, y1, x2, y2)
        except ValueError:
            print '--Please ensure the data for the selected tx and rx is valid--'
        
         

    ## prints the environment  
    def showEnvironment(self):
        ##print a         ##tx_numbers
        ##print b         ##rx_numbers
        ##print tx        ##tx_x values []
        ##print ty        ##tx_y values []
        ##print tz        ##tx_z values []
        ##print rx        ##rx_x values []
        ##print ry        ##rx_y values []
        ##print rz        ##rx_z values []
        
        ##print ox        ##target x values []
        ##print oy        ##target y values []
        ##print oz        ##target z values []
        print '--Environment for visualisation--'
        print''
        for i in range(len(a)):
            print'--Transmitters--'
            printf ('{: <20}'.format('Name:'))
            printf ('%s\n',tx_names[i])                
            printf ('{: <20}'.format('Longitude:'))
            printf ('%s\n',tx[i])
            printf ('{: <20}'.format('Latitude:'))
            printf ('%s\n',ty[i])
            printf ('{: <20}'.format('Altitude:'))
            printf ('%s\n',tz[i])    
        
        print''    
        for i in range(len(b)):
            print'--Receivers--'
            printf ('{: <20}'.format('Name:'))
            printf ('%s\n',rx_names[i])                
            printf ('{: <20}'.format('Longitude:'))
            printf ('%s\n',rx[i])
            printf ('{: <20}'.format('Latitude:'))
            printf ('%s\n',ry[i])
            printf ('{: <20}'.format('Altitude:'))
            printf ('%s\n',rz[i])                      
        
        print ''    
        print '--Target--'
        printf ('{: <20}'.format('Name:'))
        printf ('%s\n',rcs)
        printf ('{: <20}'.format('Longitude:'))
        printf ('%s\n',ox[0])
        printf ('{: <20}'.format('Latitude:'))
        printf ('%s\n',oy[0])
        printf ('{: <20}'.format('Altitude:'))
        printf ('%s\n',oz[0])
    
   

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

