# Form helper for desktop application

# modules
from datetime import datetime
from openpyxl import *

def return_date():
    return datetime.now().strftime("%d-%m-%Y")
    
def return_new_quote():
    # FOR DESKTOP
    wb = load_workbook('C:\\Users\\franc\\Desktop\\ejemplo_cot.xlsx', data_only=True)

    # FOR NOTEBOOK
    # wb = load_workbook('C:\\Users\\franc\\OneDrive\\Escritorio\\ejemplo_cot.xlsx', data_only=True)

    ws = wb.active
    max_row = ws.max_row
    new_n_cot = int(ws.cell(max_row,1).value) + 1
    wb.close()
    return new_n_cot