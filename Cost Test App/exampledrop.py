from openpyxl import *
from openpyxl.drawing.image import Image
from database import *
from form_helper import return_new_client_code, return_new_quote, return_existence

# wb = load_workbook('C:\\Users\\franc\\Desktop\\FORMATO CTZ PERICLTDA.xlsx', data_only=True)
# ws = wb.active

# # print(len(ws.cell(row=28, column=7).value))

# for row in ws.iter_rows(min_row=18, max_col=9, max_row=ws.max_row):
#     for cell in row:
#         if cell.value == "TOTAL NETO (CLP)":
#             print("ENCONTRADO NETO", cell.row, cell.column)
#         if cell.value == "PRECIO UNITARIO NETO DE LA PARTIDA CON GASTOS GENERALES Y UTILIDADES (CLP)":
#             print("ENCONTRADO EL VALOR TOTAL", cell.row, cell.column)

# ws['A18'] = 'HOLA'
# ws['B18'] = "HOLA"
# ws['F18'] = "HOLA"
# ws['G18'] = "HOLA"
# ws['H18'] = "HOLA"
# ws['I18'] = "HOLA"
# ws.cell(row=18, column=1).value = 'DESDE COORDENADA'

# ws['A19'] = 'HOLANDA'
# ws['B19'] = "HOLANDA"
# ws['F19'] = "HOLANDA"
# ws['G19'] = "HOLANDA"
# ws['H19'] = "HOLANDA"
# ws['I19'] = "HOLANDA"

# cotizacion = 1234

# img = Image('images/peric.png')
# ws.add_image(img, 'A1')

# # wb.save('C:\\Users\\franc\\Desktop\\FORMATO CTZ PERICLTDA EDITADO.xlsx')
# wb.save(f'C:\\Users\\franc\\Desktop\\Cotizacion_{cotizacion}.xlsx')
# wb.close()

# db = Database.ConnectToDatabase()
# Database.InsertDatabaseClientes(db, ('001', '2300230K','EMIRATES AIRLINES', '987216543', 'SENDERO DEL ALERCE'))

code = return_new_client_code()
# print(code)

quote = return_new_quote()
# print(quote)

# db = Database.ConnectToDatabase()
# repetido = Database.SearchRutExists(db, ['2300230K'])
# if repetido == None:
#     print(False)
# else:
#     print(repetido[0])

booleano = return_existence('2300230K')
print(booleano)