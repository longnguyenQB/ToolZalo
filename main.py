from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from SqliteHelper.SqliteHelper import *
from utils import *
from Widgets.Widgets import *
from Widgets.Threads import *
from ZaloController.ZaloController import AutoZalo
import unidecode
import os
import sys

PATH = os.getcwd()
config = read_js("config.json")


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1071, 844)
        # set logo
        MainWindow.setWindowIcon(QtGui.QIcon(PATH + '/img/item.png'))
        
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # self.centralwidget.setStyleSheet('QWidget#centralwidget { background-image: url(bg1.jpg)}')
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        
        # groupbox setting
        self.groupBox_setting = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_setting.setMaximumSize(QtCore.QSize(16777215, 200))
        self.groupBox_setting.setObjectName("groupBox_setting")
        self.groupBox_setting.setStyleSheet("background-color:white")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_setting)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox_setting)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 3)
        self.label = QtWidgets.QLabel(parent=self.groupBox_setting)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 3, 0, 1, 1)
        
        self.spinBox_setting_1 = QtWidgets.QSpinBox(parent=self.groupBox_setting)
        self.spinBox_setting_1.setObjectName("spinBox_setting_1")
        self.spinBox_setting_1.setProperty("value", 5)
        self.gridLayout_2.addWidget(self.spinBox_setting_1, 0, 3, 1, 1)
        
        self.comboBox_typelogin = QtWidgets.QComboBox(parent=self.groupBox_setting)
        self.comboBox_typelogin.setObjectName("comboBox_typelogin")
        self.comboBox_typelogin.addItem("")
        self.comboBox_typelogin.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_typelogin, 2, 2, 1, 2)
        
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox_setting)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 2)
        
        # Set time open
        self.spinBox_setting_2 = QtWidgets.QSpinBox(parent=self.groupBox_setting)
        self.spinBox_setting_2.setObjectName("spinBox_setting_2")
        self.spinBox_setting_2.setProperty("value", 3)
        self.gridLayout_2.addWidget(self.spinBox_setting_2, 1, 3, 1, 1)
        
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox_setting)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 2)
        
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox_setting)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 3, 2, 1, 1)
        
        # Set size windowns
        self.spinBox_setting_3 = QtWidgets.QSpinBox(parent=self.groupBox_setting)
        self.spinBox_setting_3.setMinimum(100)
        self.spinBox_setting_3.setMaximum(1000)
        self.spinBox_setting_3.setProperty("value", 200)
        self.spinBox_setting_3.setObjectName("spinBox_setting_3")
        self.gridLayout_2.addWidget(self.spinBox_setting_3, 3, 1, 1, 1)
        
        self.spinBox_setting_4 = QtWidgets.QSpinBox(parent=self.groupBox_setting)
        self.spinBox_setting_4.setMinimum(100)
        self.spinBox_setting_4.setMaximum(1000)
        self.spinBox_setting_4.setProperty("value", 300)
        self.spinBox_setting_4.setObjectName("spinBox_2")
        self.gridLayout_2.addWidget(self.spinBox_setting_4, 3, 3, 1, 1)
        
        self.gridLayout.addWidget(self.groupBox_setting, 0, 0, 1, 1)
        
        # Create action frame
        self.scrollArea = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.scrollArea.setMinimumSize(QtCore.QSize(800, 300))
        self.scrollArea.setMinimumSize(QtCore.QSize(800, 300))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1018, 381))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 1, 4, 1)
        self.groupBox_action = QtWidgets.QGroupBox(parent=self.scrollAreaWidgetContents)
        self.groupBox_action.setTitle("Chọn hành động: ")
        self.groupBox_action.setObjectName(f"groupBox_action")
        
        self.horizontalLayout_action = QtWidgets.QHBoxLayout(self.groupBox_action)
        self.horizontalLayout_action.setObjectName(f"horizontalLayout_action")
        
        self.comboBox_action = QtWidgets.QComboBox(parent=self.groupBox_action)
        self.comboBox_action.setMaximumSize(QtCore.QSize(200, 20))
        self.comboBox_action.setLocale(QtCore.QLocale(QtCore.QLocale.Language.Vietnamese, QtCore.QLocale.Country.Vietnam))
        self.comboBox_action.setObjectName(f"groupBox_action")
        self.comboBox_action.addItem("Chọn hành động")
        self.comboBox_action.addItem("Kết bạn")
        self.comboBox_action.addItem("Spam tin nhắn")
        self.horizontalLayout_action.addWidget(self.comboBox_action)
        self.verticalLayout.addWidget(self.groupBox_action)
        
        # pushButton import acc
        self.pushButton_import_acc = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_import_acc.setStyleSheet("background-color:rgb(255, 255, 0)")
        self.pushButton_import_acc.setObjectName("pushButton_import_acc")
        self.gridLayout.addWidget(self.pushButton_import_acc, 1, 0, 1, 1)
        
        # pushButton scan group
        self.pushButton_scan = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_scan.setStyleSheet("background-color:rgb(255, 100, 0)")
        self.pushButton_scan.setObjectName("pushButton_scan")
        self.gridLayout.addWidget(self.pushButton_scan, 2, 0, 1, 1)
        
        # pushButton for Run
        self.pushButton_Run = QtWidgets.QPushButton(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Run.setFont(font)
        self.pushButton_Run.setStyleSheet("background-color:rgb(0, 170, 127)")
        self.pushButton_Run.setObjectName("pushButton_Run")
        self.gridLayout.addWidget(self.pushButton_Run, 3, 0, 1, 1)
        
        self.pushButton_Stop = QtWidgets.QPushButton(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_Stop.setFont(font)
        self.pushButton_Stop.setStyleSheet("background-color:rgb(255, 0, 0)")
        self.pushButton_Stop.setObjectName("pushButton_Stop")
        self.gridLayout.addWidget(self.pushButton_Stop, 4, 0, 1, 1)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        # Create layout for filter
        
        # Load data
        self.table_name = "Nhom"
        self.query = f"SELECT * FROM {self.table_name}"
        if os.path.isfile(f".\database\database_{self.table_name}.db"):
            self.load_data(self.table_name, self.query)
        # Connect
        self.comboBox_action.activated.connect(self.show_setting_action)
        self.pushButton_import_acc.clicked.connect(self.import_acc)
        self.pushButton_scan.clicked.connect(self.scan_group)
        self.pushButton_Run.clicked.connect(self.run_actions)
        self.pushButton_Stop.clicked.connect(self.stop_actions)
        
    
    def import_acc(self):
        self.ui_run = Ui_ImportWindown()
        self.ui_run.setupUi("ImportAcc")
        self.ui_run.ImportAcc.show()

    def scan_group(self):
        self.time_open =  int(self.spinBox_setting_2.value())
        self.autoZalo = ThreadScan(time_open=self.time_open)
        self.autoZalo.start()
        self.autoZalo.signal_state.connect(self.load_data)        
    
    def run_actions(self):
        try:
            type_action = self.comboBox_TypeAction.currentText() 
            action = self.comboBox_action.currentText() 
            time_distance = [self.spinBox_action_time_distance1.value(),
                            self.spinBox_action_time_distance2.value()]
            self.time_open =  int(self.spinBox_setting_2.value())

            if action == "Spam tin nhắn":
                if type_action == "Theo danh sách SĐT":
                    action = 'send_mess_to_phonenumbers'
                elif type_action == "Theo danh sách Nhóm":
                    action = 'send_mess_to_members'
            elif action == "Kết bạn":
                if type_action == "Theo danh sách SĐT":
                    action = 'add_friend_from_phonenumbers'
                elif type_action == "Theo danh sách Nhóm":
                    action = 'add_friend_from_members'
            
                    
            rows = self.tableWidget.selectionModel().selectedIndexes()
            index_selected = list(set([row.row() for row in rows]))
            index_selected.sort()
            self.IDs = {}
            for index_row in index_selected:
                self.IDs[self.tableWidget.item(index_row, 0).text()] = index_row
            
            self.autoZalo = ThreadsZalo(IDs = list(self.IDs.keys()),
                            action= action,
                            time_distance = time_distance,
                            time_open= self.time_open)
            self.autoZalo.start()
            self.autoZalo.signal_state.connect(self.update_table)
        except:
            self.show_warning_messagebox("Hãy chọn hành động trước!")
    
    def update_table(self, ID, state):
        state_index = self.get_index_by_column_name("Trạng thái")
        self.tableWidget.setItem(self.IDs[ID], state_index, QtWidgets.QTableWidgetItem(state))
    
    def stop_actions(self):
        self.autoZalo.stop()
        
        
    def show_setting_action(self, index):
        if index == 0:
            pass
        elif index == 1:
            self.show_action_addfriend()
        elif index == 2:
            self.show_action_spamtext()    
        else:
            pass
        
        
    def show_action_addfriend(self):
        try:
            self.frame_action.deleteLater()
        except:
            pass
        self.frame_action = QtWidgets.QFrame(parent=self.groupBox_action)
        self.frame_action.setMaximumSize(QtCore.QSize(600, 500))
        self.frame_action.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_action.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_action.setObjectName("frame")
        
        self.gridLayout_action = QtWidgets.QGridLayout(self.frame_action)
        self.gridLayout_action.setObjectName(f"gridLayout_action")
        
        self.label_6 = QtWidgets.QLabel(parent=self.frame_action)
        self.label_6.setText("Chọn phương thức kết bạn:")
        self.label_6.setMaximumSize(QtCore.QSize(180, 20))
        self.label_6.setObjectName("label_6")
        self.gridLayout_action.addWidget(self.label_6, 0, 0, 1, 1)
        
        self.comboBox_TypeAction = QtWidgets.QComboBox(parent=self.frame_action)
        self.comboBox_TypeAction.setMaximumSize(QtCore.QSize(300, 20))
        self.comboBox_TypeAction.setLocale(QtCore.QLocale(QtCore.QLocale.Language.Vietnamese, QtCore.QLocale.Country.Vietnam))
        self.comboBox_TypeAction.setObjectName(f"groupBox_action")
        self.comboBox_TypeAction.addItem("Chọn phương thức")
        self.comboBox_TypeAction.addItem("Theo danh sách SĐT")
        self.comboBox_TypeAction.addItem("Theo danh sách Nhóm")
        self.gridLayout_action.addWidget(self.comboBox_TypeAction, 0, 1, 1, 1)
        
        self.comboBox_TypeAction.activated.connect(self.show_by_type_action)
        
        # self.label_8 = QtWidgets.QLabel(parent=self.frame_action)
        # self.label_8.setMaximumSize(QtCore.QSize(180, 20))
        # self.label_8.setText("Số lượng kết bạn:")
        # self.label_8.setObjectName("label_8")
        # self.gridLayout_action.addWidget(self.label_8, 2, 0, 1, 1)
        
        # self.spinBox_action_addfriend1 = QtWidgets.QSpinBox(parent=self.frame_action)
        # self.spinBox_action_addfriend1.setMinimumSize(QtCore.QSize(30, 25))
        # self.spinBox_action_addfriend1.setMaximumSize(QtCore.QSize(40, 30))
        # self.spinBox_action_addfriend1.setObjectName(f"spinBox_action_addfriend1")
        # self.spinBox_action_addfriend1.setProperty("value", 3)
        # self.gridLayout_action.addWidget(self.spinBox_action_addfriend1, 2, 1, 1, 1)

        # self.label_sign1 = QtWidgets.QLabel(parent=self.frame_action)
        # self.label_sign1.setMinimumSize(QtCore.QSize(10, 20))
        # self.label_sign1.setMaximumSize(QtCore.QSize(10, 20))
        # self.label_sign1.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:8pt; font-weight:600;\">&gt;</span></p></body></html>")
        # self.label_sign1.setObjectName("label_sign1")
        # self.gridLayout_action.addWidget(self.label_sign1, 2, 2, 1, 1)

        # self.spinBox_action_addfriend2 = QtWidgets.QSpinBox(parent=self.frame_action)
        # self.spinBox_action_addfriend2.setMinimumSize(QtCore.QSize(30, 25))
        # self.spinBox_action_addfriend2.setMaximumSize(QtCore.QSize(40, 30))
        # self.spinBox_action_addfriend2.setObjectName(f"spinBox_action_addfriend2")
        # self.spinBox_action_addfriend2.setProperty("value", 5)
        # self.gridLayout_action.addWidget(self.spinBox_action_addfriend2, 2, 3, 1, 1)
        
        self.label_9 = QtWidgets.QLabel(parent=self.frame_action)
        self.label_9.setMaximumSize(QtCore.QSize(180, 20))
        self.label_9.setText("Khoảng cách (s):")
        self.label_9.setObjectName("label_9")
        self.gridLayout_action.addWidget(self.label_9, 3, 0, 1, 1)
        
        self.spinBox_action_time_distance1 = QtWidgets.QSpinBox(parent=self.frame_action)
        self.spinBox_action_time_distance1.setMinimumSize(QtCore.QSize(30, 25))
        self.spinBox_action_time_distance1.setMaximumSize(QtCore.QSize(40, 30))
        self.spinBox_action_time_distance1.setMinimum(0)
        self.spinBox_action_time_distance1.setObjectName(f"spinBox_action_time_distance1")
        self.spinBox_action_time_distance1.setProperty("value", 0)
        self.gridLayout_action.addWidget(self.spinBox_action_time_distance1, 3, 1, 1, 1)
        
        self.label_sign2 = QtWidgets.QLabel(parent=self.frame_action)
        self.label_sign2.setMinimumSize(QtCore.QSize(10, 20))
        self.label_sign2.setMaximumSize(QtCore.QSize(10, 20))
        self.label_sign2.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:8pt; font-weight:600;\">&gt;</span></p></body></html>")
        self.label_sign2.setObjectName("label_sign1")
        self.gridLayout_action.addWidget(self.label_sign2, 3, 2, 1, 1)
        
        self.spinBox_action_time_distance2 = QtWidgets.QSpinBox(parent=self.frame_action)
        self.spinBox_action_time_distance2.setMinimumSize(QtCore.QSize(30, 25))
        self.spinBox_action_time_distance2.setMaximumSize(QtCore.QSize(40, 30))
        self.spinBox_action_time_distance2.setMinimum(0)
        self.spinBox_action_time_distance2.setObjectName(f"spinBox_action_time_distance2")
        self.spinBox_action_time_distance2.setProperty("value", 0)
        self.gridLayout_action.addWidget(self.spinBox_action_time_distance2, 3, 3, 1, 1)
        
        self.horizontalLayout_action.addWidget(self.frame_action)
        
    def show_action_spamtext(self):
        try:
            self.frame_action.deleteLater()
        except:
            pass
        
        self.frame_action = QtWidgets.QFrame(parent=self.groupBox_action)
        self.frame_action.setMaximumSize(QtCore.QSize(600, 500))
        self.frame_action.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_action.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_action.setObjectName("frame")
        
        self.gridLayout_action = QtWidgets.QGridLayout(self.frame_action)
        self.gridLayout_action.setObjectName(f"gridLayout_action")
        
        self.label_6 = QtWidgets.QLabel(parent=self.frame_action)
        self.label_6.setText("Chọn phương thức nhắn tin:")
        self.label_6.setMaximumSize(QtCore.QSize(180, 20))
        self.label_6.setObjectName("label_6")
        self.gridLayout_action.addWidget(self.label_6, 0, 0, 1, 1)
        
        self.comboBox_TypeAction = QtWidgets.QComboBox(parent=self.frame_action)
        self.comboBox_TypeAction.setMaximumSize(QtCore.QSize(300, 20))
        self.comboBox_TypeAction.setLocale(QtCore.QLocale(QtCore.QLocale.Language.Vietnamese, QtCore.QLocale.Country.Vietnam))
        self.comboBox_TypeAction.setObjectName(f"groupBox_action")
        self.comboBox_TypeAction.addItem("Chọn phương thức")
        self.comboBox_TypeAction.addItem("Theo danh sách SĐT")
        self.comboBox_TypeAction.addItem("Theo danh sách Nhóm")
        self.gridLayout_action.addWidget(self.comboBox_TypeAction, 0, 1, 1, 1)
        
        self.comboBox_TypeAction.activated.connect(self.show_by_type_action)
        
        # self.label_8 = QtWidgets.QLabel(parent=self.frame_action)
        # self.label_8.setMaximumSize(QtCore.QSize(180, 20))
        # self.label_8.setText("Số lượng nhắn tin:")
        # self.label_8.setObjectName("label_8")
        # self.gridLayout_action.addWidget(self.label_8, 2, 0, 1, 1)
        
        # self.spinBox_action_addfriend1 = QtWidgets.QSpinBox(parent=self.frame_action)
        # self.spinBox_action_addfriend1.setMinimumSize(QtCore.QSize(30, 25))
        # self.spinBox_action_addfriend1.setMaximumSize(QtCore.QSize(40, 30))
        # self.spinBox_action_addfriend1.setObjectName(f"spinBox_action_addfriend1")
        # self.spinBox_action_addfriend1.setProperty("value", 3)
        # self.gridLayout_action.addWidget(self.spinBox_action_addfriend1, 2, 1, 1, 1)

        # self.label_sign1 = QtWidgets.QLabel(parent=self.frame_action)
        # self.label_sign1.setMinimumSize(QtCore.QSize(10, 20))
        # self.label_sign1.setMaximumSize(QtCore.QSize(10, 20))
        # self.label_sign1.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:8pt; font-weight:600;\">&gt;</span></p></body></html>")
        # self.label_sign1.setObjectName("label_sign1")
        # self.gridLayout_action.addWidget(self.label_sign1, 2, 2, 1, 1)

        # self.spinBox_action_addfriend2 = QtWidgets.QSpinBox(parent=self.frame_action)
        # self.spinBox_action_addfriend2.setMinimumSize(QtCore.QSize(30, 25))
        # self.spinBox_action_addfriend2.setMaximumSize(QtCore.QSize(40, 30))
        # self.spinBox_action_addfriend2.setObjectName(f"spinBox_action_addfriend2")
        # self.spinBox_action_addfriend2.setProperty("value", 5)
        # self.gridLayout_action.addWidget(self.spinBox_action_addfriend2, 2, 3, 1, 1)
        
        self.label_9 = QtWidgets.QLabel(parent=self.frame_action)
        self.label_9.setMaximumSize(QtCore.QSize(180, 20))
        self.label_9.setText("Khoảng cách (s):")
        self.label_9.setObjectName("label_9")
        self.gridLayout_action.addWidget(self.label_9, 3, 0, 1, 1)
        
        self.spinBox_action_time_distance1 = QtWidgets.QSpinBox(parent=self.frame_action)
        self.spinBox_action_time_distance1.setMinimumSize(QtCore.QSize(30, 25))
        self.spinBox_action_time_distance1.setMaximumSize(QtCore.QSize(40, 30))
        self.spinBox_action_time_distance1.setMinimum(0)
        self.spinBox_action_time_distance1.setObjectName(f"spinBox_action_time_distance1")
        self.spinBox_action_time_distance1.setProperty("value", 0)
        self.gridLayout_action.addWidget(self.spinBox_action_time_distance1, 3, 1, 1, 1)
        
        self.label_sign2 = QtWidgets.QLabel(parent=self.frame_action)
        self.label_sign2.setMinimumSize(QtCore.QSize(10, 20))
        self.label_sign2.setMaximumSize(QtCore.QSize(10, 20))
        self.label_sign2.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:8pt; font-weight:600;\">&gt;</span></p></body></html>")
        self.label_sign2.setObjectName("label_sign1")
        self.gridLayout_action.addWidget(self.label_sign2, 3, 2, 1, 1)
        
        self.spinBox_action_time_distance2 = QtWidgets.QSpinBox(parent=self.frame_action)
        self.spinBox_action_time_distance2.setMinimumSize(QtCore.QSize(30, 25))
        self.spinBox_action_time_distance2.setMaximumSize(QtCore.QSize(40, 30))
        self.spinBox_action_time_distance2.setMinimum(0)
        self.spinBox_action_time_distance2.setObjectName(f"spinBox_action_time_distance2")
        self.spinBox_action_time_distance2.setProperty("value", 0)
        self.gridLayout_action.addWidget(self.spinBox_action_time_distance2, 3, 3, 1, 1)
        
        self.horizontalLayout_action.addWidget(self.frame_action)
    
    def show_by_type_action(self):
        self.type_action = self.comboBox_TypeAction.currentText() 
        self.type_action = unidecode.unidecode(self.type_action).replace(" ", "_")
        try:
            self.label_7_.deleteLater()
            self.pushButton_open_dialog.pushButton_open.deleteLater()
        except:
            pass
        try:
            self.label_7.deleteLater()
            self.pushButton_open.pushButton_open.deleteLater()
        except:
            pass
        
        # load data
        if "Nhom" in self.type_action:
            group_name = "Nhom"
            number = 1
        elif "SDT" in self.type_action:
            group_name = "SDT"
            self.label_7_ = QtWidgets.QLabel(parent=self.frame_action)
            self.label_7_.setMaximumSize(QtCore.QSize(180, 20))
            self.label_7_.setText("Nhập danh sách mới:")
            self.label_7_.setObjectName("label_7_")
            self.gridLayout_action.addWidget(self.label_7_, 1, 0, 1, 1)
            # pushButton for open dialog boxes
            self.pushButton_open_dialog = ButtonOpenFileDialog()
            self.pushButton_open_dialog.setupUi(parent = self.centralwidget, 
                                                group_name=group_name)
            self.gridLayout_action.addWidget(self.pushButton_open_dialog.pushButton_open, 1, 1, 1, 1)
            self.pushButton_open_dialog.signal_path.connect(self.load_data)
            number = 2
                
        self.label_7 = QtWidgets.QLabel(parent=self.frame_action)
        self.label_7.setMaximumSize(QtCore.QSize(180, 20))
        self.label_7.setText("Nhập nội dung tin nhắn:")
        self.label_7.setObjectName("label_7")
        self.gridLayout_action.addWidget(self.label_7, number, 0, 1, 1)
        
        # pushButton for open another windown for import mess
        self.pushButton_open = ButtonOpenFileDialog()
        self.pushButton_open.setupUi(self.centralwidget, "Nhom")
        self.gridLayout_action.addWidget(self.pushButton_open.pushButton_open, number, 1, 1, 1)
        self.pushButton_open.signal_path.connect(self.load_data)
        
        query = f"SELECT * FROM {group_name}"
        if os.path.isfile(f".\database\database_{group_name}.db"):
            self.load_data(group_name, query)
                
    def load_data(self, group_name, query):
        try:
            self.tableWidget.deleteLater()
        except:
            pass
        
        #Connect to database
        self.table_name = group_name
        conn = create_connection(f".\database\database_{self.table_name}.db")
        columns_name = get_columns_name(conn, self.table_name)
        if 'Nhom' in self.table_name:
            columns_name = list(map(lambda x: x.replace('member_name', 'Thành viên'), columns_name))
            columns_name = list(map(lambda x: x.replace('group_name', 'Nhóm'), columns_name))
        elif 'SDT' in self.table_name:
            columns_name = list(map(lambda x: x.replace('phone_or_url', 'Số điện thoại'), columns_name))
        columns_name = list(map(lambda x: x.replace('status', 'Tình trạng'), columns_name))
        columns_name = list(map(lambda x: x.replace('state', 'Trạng thái'), columns_name))
        # columns_name.insert(0,"Chọn")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setMinimumSize(QtCore.QSize(1050, 100))
        self.tableWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setStyleSheet("background-color:rgb(85, 255, 127)rgb(255, 255, 255)")
        self.tableWidget.setColumnCount(len(columns_name))
        self.tableWidget.setHorizontalHeaderLabels(columns_name)
        self.tableWidget.setSelectionMode(QAbstractItemView.MultiSelection)
        # self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        # self.tableWidget.horizontalHeader().setVisible(False)   
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(len(columns_name)-1, QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.gridLayout.addWidget(self.tableWidget, 8, 0, 1, 2)
        self.tableWidget.setRowCount(get_length(conn = conn,
                                                query = query.replace("*", "count(*)")))
        self.tableWidget.setSortingEnabled(True)
        self.horizontalHeader = self.tableWidget.horizontalHeader()
        
        # Connect:
        self.horizontalHeader.sectionClicked.connect(self.on_view_horizontalHeader_sectionClicked)
        self.tableWidget.clicked.connect(self.select_row)
        
        # Load data from db
        cur = conn.cursor()
        row_index = 0
        # chkBoxItem = {}
        print(query)
        rows = cur.execute(query)
        for row in rows:
            item_ID = QTableWidgetItem()
            item_ID.setData(Qt.EditRole, row[0])
            self.tableWidget.setItem(row_index, 0, item_ID) 
            # chkBoxItem = QTableWidgetItem()
            # chkBoxItem.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
            # chkBoxItem.setCheckState(Qt.Unchecked)       
            # self.tableWidget.setItem(row_index,0,chkBoxItem)
            for i in range(1,len(columns_name)):
                self.tableWidget.setItem(row_index, i, QtWidgets.QTableWidgetItem(str(row[i])))
            row_index+=1
    
    # Filter by horizontal Header
    def on_view_horizontalHeader_sectionClicked(self, logicalIndex):
        if logicalIndex == 0:
            pass
        else:
            self.logicalIndex   = logicalIndex

            valuesUnique = [self.tableWidget.item(row, self.logicalIndex).text() for row in range(self.tableWidget.rowCount()) if not self.tableWidget.isRowHidden(row)]

            # Mở cửa sổ con
            self.Menudialog = QDialog(parent=MainWindow)
            self.Menudialog.setWindowTitle('Chọn giá trị cần lọc')
            self.Menudialog.setMinimumSize(QtCore.QSize(400, 400))

            self.list_widget = QListWidget(parent=MainWindow)
            valuesUnique = sorted(list(set(valuesUnique)))
            valuesUnique.insert(0, "Tất cả")
            valuesUnique.insert(1, "Bỏ chọn tất cả")
            self.list_widget.addItems(valuesUnique)
            
            # create QScrollArea，put QListWidget in it
            scroll_area = QScrollArea(self.Menudialog)
            scroll_area.setWidgetResizable(True)
            scroll_area.setWidget(self.list_widget)

            self.list_widget.currentItemChanged.connect(self.on_list_item_clicked)
            layout = QVBoxLayout(self.Menudialog)
            layout.addWidget(scroll_area)

            headerPos = self.tableWidget.mapToGlobal(self.horizontalHeader.pos())
            posY = headerPos.y() + self.horizontalHeader.height()
            # posX = headerPos.x() + self.horizontalHeader.sectionPosition(self.logicalIndex)
            posX = headerPos.x() + self.horizontalHeader.sectionViewportPosition(self.logicalIndex)
            if posX > 1700:
                posX = 1620
            self.Menudialog.setGeometry(posX +100, posY, 200, 300)
            self.Menudialog.exec()
            
    def on_list_item_clicked(self):
        item = self.list_widget.currentItem()
        if item.text() == "Tất cả":
            query = f"SELECT * FROM {self.table_name}"
            self.load_data(group_name= self.table_name,
                            query=query)
            self.tableWidget.selectAll()
                                    
        elif item.text() == "Bỏ chọn tất cả":
            self.tableWidget.clearSelection()
            
        else:
            map_column_name = {"Thành viên": "member_name", 
                                "Nhóm": "group_name",
                                "Số điện thoại":  "phone_or_url",
                                "Tình trạng": "status",
                                "Trạng thái": "state"}
            column_name = map_column_name[self.tableWidget.horizontalHeaderItem(self.logicalIndex).text()]    
            query = f"SELECT * FROM {self.table_name} WHERE {column_name} == '{item.text()}'"
            self.tableWidget.clearSelection()
            self.load_data(group_name= self.table_name,
                            query=query)
            self.tableWidget.selectAll()
        self.Menudialog.close()
    #  Utils 
    
    def get_index_by_column_name(self, label):
        for index_column in range(self.tableWidget.columnCount()):
            if self.tableWidget.horizontalHeaderItem(index_column).text() == label:
                return index_column
        return -1

    def select_row(self, rows):
        print(rows)
        pass
        # print("rows: ",len(rows))
        # for row in rows:
        #     self.tableWidget.selectRow(row)
        #     print(row)
    
    def show_warning_messagebox(self, mess):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
    
        # setting message for Message Box
        msg.setText(mess)
        
        # setting Message box window title
        msg.setWindowTitle("Lỗi")
        
        # declaring buttons on Message Box
        msg.setStandardButtons(QMessageBox.Ok)
        
        # start the app
        retval = msg.exec_()
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tool Zalo"))
        self.pushButton_import_acc.setText(_translate("MainWindow", "Nhập acc"))
        self.pushButton_scan.setText(_translate("MainWindow", "Quét nhóm đã tham gia"))
        self.groupBox_setting.setTitle(_translate("MainWindow", "Cấu hình chung"))
        self.label_2.setText(_translate("MainWindow", "Thời gian mở (s)"))
        self.label.setText(_translate("MainWindow", "Size hình"))
        self.comboBox_typelogin.setItemText(0, _translate("MainWindow", "Mail-Pass"))
        self.comboBox_typelogin.setItemText(1, _translate("MainWindow", "UID FB-Pass-2FA"))
        self.label_4.setText(_translate("MainWindow", "Số luồng"))
        self.label_3.setText(_translate("MainWindow", "Kiểu đăng nhập"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:8pt; font-weight:600;\">X</span></p></body></html>"))
        self.pushButton_Run.setText(_translate("MainWindow", "Chạy"))
        self.pushButton_Stop.setText(_translate("MainWindow", "Dừng"))
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
