
from openpyxl import *
from btn import update_into_excel

# wb = load_workbook('C:\\Users\\franc\\OneDrive\\Escritorio\\ejemplo_cot.xlsx', data_only=True)
    
# ws = wb.active

# # max_row = int(ws.max_row) + 1
# # min_column = ws.min_column
# def UpdateExcel():
#     for row in ws.iter_rows(min_row=ws.min_row, max_col=ws.max_column, max_row=ws.max_row):
#         for cell in row:
#             # print(cell)
#             if cell.value == 1557:
#                 return cell.row
#                 print("hola", cell.row, cell.column, cell.index)
#             # print(cell.value, end=' ')
#         # print()

# row = UpdateExcel()
# for i in range(ws.min_column, ws.max_column+1):
#     print(ws.cell(row=row, column=i).value, end=' ')

update_into_excel(7)

# print(row)

# print(ws.min_column, ws.max_column)
# ws.cell(row=2, column=2).value = 5  
# print(ws.cell(row=2, column=2).value)



# for row in ws.values:
#    for value in row:
#      print(value)