import gspread
import pandas as pd
from gspread_dataframe import set_with_dataframe
import machineid
import os
import sys
sys.path.append(os.getcwd())

PATH = os.getcwd()

def append_row(gsheet_name, tab_name, row_value):
    gc = gspread.service_account(filename=PATH + "/Auth/controll-keys-84681da521e3.json")
    sh = gc.open(gsheet_name)
    worksheet = sh.worksheet(tab_name)
    worksheet.append_row(row_value, table_range= "A1:C1")
    
def get_sheet_data(gsheet_name, tab_name):
    gc = gspread.service_account(filename=PATH + "/Auth/controll-keys-84681da521e3.json")
    sh = gc.open(gsheet_name)
    worksheet = sh.worksheet(tab_name)
    df = pd.DataFrame(worksheet.get_all_records())
    return df

def write_sheet_data(gsheet_name, tab_name, df):
    gc = gspread.service_account(filename=PATH + "/Auth/controll-keys-84681da521e3.json")
    sh = gc.open(gsheet_name)
    worksheet = sh.worksheet(tab_name)
    set_with_dataframe(worksheet, df)
