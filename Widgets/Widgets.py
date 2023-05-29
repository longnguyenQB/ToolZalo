from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import unidecode
import os
import sys
sys.path.append(os.getcwd())
from SqliteHelper.SqliteHelper import *
from utils import *

PATH = os.getcwd()

class ButtonOpenFileDialog(QWidget):
    signal_path = QtCore.pyqtSignal(object, object)
    
    def setupUi(self, parent, group_name):
        self.table_name = group_name
        self.pushButton_open = QtWidgets.QPushButton(parent=parent)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_open.setFont(font)
        self.pushButton_open.setText(("Nhập"))
        self.pushButton_open.setStyleSheet("background-color:rgb(0, 170, 127)")
        self.pushButton_open.setObjectName("pushButton_open")
        self.pushButton_open.clicked.connect(self.click)
    
    def click(self):
        query = f"SELECT * FROM {self.table_name}"
        if "Nhom" in self.table_name:
            # Open another windown for import
            self.ui_run = Ui_ImportWindown()
            self.ui_run.setupUi("ImportMessSpam")
            self.ui_run.ImportAcc.show()
            self.signal_path.emit(self.table_name, query)
        elif "SDT" in self.table_name:
            # Open file dialog
            fname = QFileDialog.getOpenFileName(self, caption= "Open File", directory = "", filter = "All Files (*);; txt file (*.txt)")
            if fname:
                path = fname[0]
                if ".txt" in path:
                    contents = open_txt(path=path)
                    conn = create_connection(PATH + f"/database/database_{self.table_name}.db")
                    delete_table(conn=conn, table=self.table_name)
                    query_create_table = f"""CREATE TABLE IF NOT EXISTS {self.table_name} (
                                        id integer PRIMARY KEY AUTOINCREMENT,
                                        phone_or_url text NOT NULL,
                                        status text,
                                        state text
                                    );"""
                    create_table(conn=conn, query=query_create_table)
                    for content in contents:
                        insert_table(conn=conn, table=self.table_name,
                                    columns=['phone_or_url'],
                                    values=[content],
                                    realtime = False)
                    conn.commit()
                self.signal_path.emit(self.table_name, query)

            
class Ui_ImportWindown(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
    def setupUi(self, type):
        self.type = type
        # ImportAcc.setObjectName("ImportAcc")
        # ImportAcc.resize(780, 518)
        self.ImportAcc = QtWidgets.QMainWindow()
        self.ImportAcc.setObjectName("ImportAcc")
        self.ImportAcc.setWindowTitle("Nhập nội dung")
        self.ImportAcc.setMinimumSize(QtCore.QSize(780, 520))
        self.ImportAcc.setMaximumSize(QtCore.QSize(780, 520))
        self.centralwidget = QtWidgets.QWidget(parent=self.ImportAcc)
        self.centralwidget.setObjectName("centralwidget")
        self.btnSave = QtWidgets.QPushButton(self.centralwidget)
        self.btnSave.setGeometry(QtCore.QRect(290, 440, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnSave.setFont(font)
        self.btnSave.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btnSave.setStyleSheet("background-color: rgb(170, 255, 127)")
        self.btnSave.setObjectName("btnSave")
        self.btnSave.setText( "Lưu")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(30, 10, 721, 416))
        self.plainTextEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.plainTextEdit.setMaximumSize(QtCore.QSize(721, 416))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.ImportAcc.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self.ImportAcc)
        self.statusbar.setObjectName("statusbar")
        self.ImportAcc.setStatusBar(self.statusbar)
        # Connect
        if self.type == "ImportAcc":
            self.path=PATH + "/settings/ListAcc.txt"
        elif self.type == "ImportMessSpam":
            self.path=PATH + "/settings/ListMessSpam.txt"
            
        pre_content = open_txt(self.path)
        pre_content = '\n'.join(pre_content)
        self.plainTextEdit.setPlainText(pre_content)
        self.btnSave.clicked.connect(self.btnSaveClick)
    
    def btnSaveClick(self):
        data = self.plainTextEdit.toPlainText().splitlines()
        if self.type == "ImportAcc":
            write_txt(path=self.path,
                      content=data)
        elif self.type == "ImportMessSpam":
            write_txt(path=self.path,
                      content=data)
            
        self.ImportAcc.close()

class MyBar(QWidget):
    clickPos = None
    def __init__(self, parent):
        super(MyBar, self).__init__(parent)
        self.setAutoFillBackground(True)
        
        self.setBackgroundRole(QPalette.Shadow)
        # alternatively:
        # palette = self.palette()
        # palette.setColor(palette.Window, Qt.black)
        # palette.setColor(palette.WindowText, Qt.white)
        # self.setPalette(palette)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(1, 1, 1, 1)
        layout.addStretch()

        self.title = QLabel("My Own Bar", self, alignment=Qt.AlignCenter)
        # if setPalette() was used above, this is not required
        self.title.setForegroundRole(QPalette.Light)

        style = self.style()
        ref_size = self.fontMetrics().height()
        ref_size += style.pixelMetric(style.PM_ButtonMargin) * 2
        self.setMaximumHeight(ref_size + 2)

        btn_size = QSize(ref_size, ref_size)
        for target in ('min', 'normal', 'max', 'close'):
            btn = QToolButton(self, focusPolicy=Qt.NoFocus)
            layout.addWidget(btn)
            btn.setFixedSize(btn_size)

            iconType = getattr(style, 
                'SP_TitleBar{}Button'.format(target.capitalize()))
            btn.setIcon(style.standardIcon(iconType))

            if target == 'close':
                colorNormal = 'red'
                colorHover = 'orangered'
            else:
                colorNormal = 'palette(mid)'
                colorHover = 'palette(light)'
            btn.setStyleSheet('''
                QToolButton {{
                    background-color: {};
                }}
                QToolButton:hover {{
                    background-color: {}
                }}
            '''.format(colorNormal, colorHover))

            signal = getattr(self, target + 'Clicked')
            btn.clicked.connect(signal)

            setattr(self, target + 'Button', btn)

        self.normalButton.hide()

        self.updateTitle(parent.windowTitle())
        parent.windowTitleChanged.connect(self.updateTitle)

    def updateTitle(self, title=None):
        if title is None:
            title = self.window().windowTitle()
        width = self.title.width()
        width -= self.style().pixelMetric(QStyle.PM_LayoutHorizontalSpacing) * 2
        self.title.setText(self.fontMetrics().elidedText(
            title, Qt.ElideRight, width))

    def windowStateChanged(self, state):
        self.normalButton.setVisible(state == Qt.WindowMaximized)
        self.maxButton.setVisible(state != Qt.WindowMaximized)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.clickPos = event.windowPos().toPoint()

    def mouseMoveEvent(self, event):
        if self.clickPos is not None:
            self.window().move(event.globalPos() - self.clickPos)

    def mouseReleaseEvent(self, QMouseEvent):
        self.clickPos = None

    def closeClicked(self):
        self.window().close()

    def maxClicked(self):
        self.window().showMaximized()

    def normalClicked(self):
        self.window().showNormal()

    def minClicked(self):
        self.window().showMinimized()

    def resizeEvent(self, event):
        self.title.resize(self.minButton.x(), self.height())
        self.updateTitle()