from PyQt5 import QtCore
from typing import List, Dict
import os
import sys
sys.path.append(os.getcwd())
from ZaloController.ZaloController import AutoZalo
from utils import *
import time

PATH = os.getcwd()

class ThreadScan(QtCore.QThread):
    signal_state = QtCore.pyqtSignal(object, object)

    def __init__(self, time_open = int, type_login = str):
        super(ThreadScan, self).__init__()
        self.time_open = time_open
        self.type_login = type_login
        self.is_running = True
        self.table_name = "Nhom"
        self.query = f"SELECT * FROM Nhom"

    def run(self):
        self.auto = AutoZalo(self.time_open)
        self.auto.open_profile()
        if self.type_login == 'Quét QR':
            self.auto.login_QR()
        else:
            acc, password = open_txt(PATH + "/settings/ListAcc.txt")[0].split("|")
            self.auto.login_cookies(phone_number=acc,
                                    password=password)
        self.auto.scan_member()
        self.signal_state.emit(self.table_name, self.query)
        self.auto.driver.close()
    
    def stop(self):
        self.signal_state.emit(self.table_name, self.query)
        self.auto.driver.close()
        self.terminate()
        
class ThreadsZalo(QtCore.QThread):
    signal_state = QtCore.pyqtSignal(object, object)

    def __init__(self, IDs = List, type_login = str, action = str, time_distance = List , time_open = int):
        super(ThreadsZalo, self).__init__()
        self.IDs = IDs
        self.type_login = type_login
        self.action = action
        self.time_distance = time_distance
        self.time_open = time_open
        self.is_running = True
        
                
    def run(self):
        self.auto = AutoZalo(time_open=self.time_open)
        self.auto.open_profile()
        time.sleep(self.time_open)
        if self.type_login == 'Quét QR':
            self.auto.login_QR()
        else:
            acc, password = open_txt(PATH + "/settings/ListAcc.txt")[0].split("|")
            self.auto.login_cookies(phone_number=acc,
                                    password=password)
        for ID in self.IDs:
            output = getattr(self.auto, self.action)(ID)
            self.signal_state.emit(ID, output)
            try:
                time.sleep(random.choice(range(self.time_distance[0], 
                                                self.time_distance[1])))
            except:
                pass
            if (output == "Bị chặn spam tạm thời!") | (output == "Quá số lần tìm kiếm"):
                break
        self.auto.driver.close()
    
    def stop(self):
        self.auto.driver.close()
        self.terminate()

