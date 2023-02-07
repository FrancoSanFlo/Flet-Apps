# this is the main file where we handle user input data

# modules
from flet import *
from controls import return_control_reference
from database import Database
from openpyxl import *
from form_helper import return_date, return_new_quote, Cotizacion, Categoria, FormHelper

control_map = return_control_reference()
categories_list = []

def return_cotizacion(data_quote):
    n_cotizacion = data_quote[0]
    rut = data_quote[1]
    cliente = data_quote[2]
    solicitado_por = data_quote[3]
    fecha_solicitud = data_quote[4]
    folio = ''
    factoring = ''
    fecha_factura = ''
    descripcion = data_quote[5]
    estado = 'NO ENVIADA'
    ganada = 'NO'
    entregado = 'NO'
    facturado = 'NO'
    pagado = 'NO'
    neto = 0
    iva = 0

    # TODO: VALIDAR
    for category in categories_list:
        neto += int(category.subtotal)

    iva = (int(neto) * 0.19) + int(neto)
    
    
    cotizacion = Cotizacion(
        n_cotizacion,
        rut,
        cliente,
        solicitado_por,
        fecha_solicitud,
        folio,
        factoring,
        fecha_factura,
        descripcion,
        estado,
        ganada,
        entregado,
        facturado,
        pagado,
        neto,
        iva
    )
    return cotizacion

def save_into_excel():

    # FOR DESKTOP
    wb = load_workbook('C:\\Users\\franc\\Desktop\\ejemplo_cot.xlsx', data_only=True)

    # FOR NOTEBOOK
    # wb = load_workbook('C:\\Users\\franc\\OneDrive\\Escritorio\\ejemplo_cot.xlsx', data_only=True)
    
    ws = wb.active
    max_row = int(ws.max_row) + 1
    min_column = ws.min_column

    db = Database.ConnectToDatabase()
    record = Database.LastRecord(db)
    record = list(record)
    record.pop(0)

    for i in range(len(record)):
        if i == 8:
            if record[i] == 1:
                ws.cell(max_row,min_column).value = 'ENVIADA'
            else:
                ws.cell(max_row,min_column).value = 'NO ENVIADA'
        else:
            if record[i] == 1:
                ws.cell(max_row,min_column).value = 'SI'
            elif record[i] == 0:
                ws.cell(max_row,min_column).value = 'NO'
            else:
                ws.cell(max_row,min_column).value = record[i]
            
        min_column += 1

    min_column = ws.min_column

    # FOR DESKTOP
    wb.save('C:\\Users\\franc\\Desktop\\ejemplo_cot.xlsx')
    # # FOR NOTEBOOK
    # wb.save('C:\\Users\\franc\\OneDrive\\Escritorio\\ejemplo_cot.xlsx')
    wb.close()

def update_input_data(e):
    for key, value in control_map.items():
        if key == 'AppFormQuote':
            # for user_input in value.controls[0].content.controls[0].controls[:]:
            n_cotizacion = value.controls[0].content.controls[0].controls[0].content.controls[1].value

            solicitud = value.controls[0].content.controls[0].controls[3].content.controls[1].value

            folio = value.controls[0].content.controls[1].controls[0].content.controls[1].value
            factoring = value.controls[0].content.controls[1].controls[1].content.controls[1].value
            fecha_factura = value.controls[0].content.controls[1].controls[2].content.controls[1].value

            descripcion = value.controls[0].content.controls[2].controls[0].content.controls[1].value

            estado = value.controls[0].content.controls[3].controls[0].content.controls[1].value
            ganada = value.controls[0].content.controls[3].controls[1].content.controls[1].value
            entregado = value.controls[0].content.controls[3].controls[2].content.controls[1].value
            facturado = value.controls[0].content.controls[3].controls[3].content.controls[1].value
            pagado = value.controls[0].content.controls[3].controls[4].content.controls[1].value
            db = Database.ConnectToDatabase()
            Database.UpdateDatabase(
                db, (solicitud, descripcion, estado, ganada, entregado, facturado, pagado, folio, fecha_factura, factoring, n_cotizacion)
            )
            db.close()

def clean_data_fields():
    for key, value in control_map.items():
        if key == 'AppFormQuote':
            for user_input in value.controls[0].content.controls[0].controls[:]:
                if user_input.content.controls[0].value == 'Número Cotización':
                    user_input.content.controls[1].value = return_new_quote()
                    user_input.content.controls[1].update()
                elif user_input.content.controls[0].value == 'Fecha solicitud':
                    user_input.content.controls[1].value = return_date()
                    user_input.content.controls[1].update()
                else:
                    user_input.content.controls[1].value = ''
                    user_input.content.controls[1].update()

            for user_input in value.controls[0].content.controls[1].controls[:]:
                user_input.content.controls[1].value = ''
                user_input.content.controls[1].update()

            for user_input in value.controls[0].content.controls[2].controls[:]:
                user_input.content.controls[1].value = ''
                user_input.content.controls[1].update()

            for user_input in value.controls[0].content.controls[3].controls[:]:
                user_input.content.controls[1].value = ''
                user_input.content.controls[1].update()
            
            for user_input in value.controls[0].content.controls[4].controls[:]:
                if  user_input.content.controls[0].value == 'Neto':
                    user_input.content.controls[1].value = ''
                    user_input.content.controls[1].update()
                else:
                    user_input.content.controls[1].value = ''
                    user_input.content.controls[1].update()

def get_input_data(e):
    data_cotizacion = []
    
    for key, value in control_map.items():
        if key == 'AppRegisterForm':
            for user_input in value.controls[0].content.controls[0].controls[:]:
                data_cotizacion.append(user_input.content.controls[1].value)

            user_description = value.controls[0].content.controls[1].controls[0].content.controls[1].value
            data_cotizacion.append(user_description)

            for user_input in value.controls[0].content.controls[2].controls[:]:
                user_input.content.controls[1].value = ''
                user_input.content.controls[1].update()

    ctz = return_cotizacion(data_cotizacion)

    # Calling to the DB Class
    db = Database.ConnectToDatabase()
    Database.InsertDatabase(
        db, 
        (
            ctz.n_cotizacion, 
            ctz.cliente, 
            ctz.rut, 
            ctz.solicitado_por,
            ctz.descripcion,
            ctz.fecha_solicitud,
            int(ctz.neto),
            int(ctz.iva),
            ctz.estado,
            ctz.ganada,
            ctz.entregado,
            ctz.facturado,
            ctz.pagado,
            ctz.folio,
            ctz.fecha_factura,
            ctz.factoring
        )
    )
    db.close()

    save_into_excel()
    # clean_data_fields()
    categories_list = []

def fill_quotes(e):
    db = Database.ConnectToDatabase()
    for key, value in control_map.items():
        if key == 'AppFormQuote':
            for user_input in value.controls[0].content.controls[0].controls[:]:
                if user_input.content.controls[0].value == 'Número Cotización':
                    user_input.content.controls[1].options.clear()
                    for quote in Database.ReadDatabase(db)[::-1]:
                        user_input.content.controls[1].options.append(dropdown.Option(quote[0]))
                    user_input.content.controls[1].update()
            
            value.controls[0].content.controls[6].controls[1].controls[1].content.visible = False

def register_category(e):
    for key, value in control_map.items():
        if key == 'AppRegisterForm':
            data = DataRow(cells=[])

            name_category_value = value.controls[0].content.controls[2].controls[0].content.controls[1].value
            type_unit_value = value.controls[0].content.controls[2].controls[1].content.controls[1].value
            amount_value = value.controls[0].content.controls[2].controls[2].content.controls[1].value
            unit_value = value.controls[0].content.controls[2].controls[3].content.controls[1].value
            subtotal_value = value.controls[0].content.controls[2].controls[4].content.controls[1].value

            if name_category_value == '' or type_unit_value == '' or amount_value == '' or unit_value == '' or subtotal_value == '':
                print('SOME FIELD IS EMPTY')
            else:
                categoria = Categoria(name_category_value, type_unit_value, int(amount_value), int(unit_value), int(subtotal_value))
                categories_list.append(categoria)
                for i in categories_list:
                    print(i.subtotal)

                for i in range(0, 5):
                    data.cells.append(
                        DataCell(
                            FormHelper(value.controls[0].content.controls[2].controls[i].content.controls[1].value)
                        )
                    )
                    if value.controls[0].content.controls[2].controls[i].content.controls[1].value == 'GL':
                        pass
                    else:
                        value.controls[0].content.controls[2].controls[i].content.controls[1].value = ''
                        value.controls[0].content.controls[2].controls[i].content.controls[1].update()

        if key == "AppDataTable":
            if len(data.cells) == 0:
                pass
            else:
                value.controls[0].controls[0].rows.append(data)
                value.controls[0].controls[0].update()


# Buttons
def return_form_button():
    return Container(
        alignment=alignment.center,
        content=ElevatedButton(
            on_click=lambda e: update_input_data(e),
            bgcolor='#007C91',
            color="white",
            content=Row(
                alignment=MainAxisAlignment.CENTER,
                controls=[
                    Icon(
                        name=icons.ADD_ROUNDED,
                        size=16
                    ),
                    Text(
                        "Enviar cambios",
                        size=12,
                        weight="bold",
                    ),
                ],
            ),
            style=ButtonStyle(
                shape={
                    "": RoundedRectangleBorder(radius=6),
                },
                color={
                    "": "white",
                },
            ),
            height=42,
            width=170,
        ),
    )

def return_quotes_button():
    return Container(
        alignment=alignment.center,
        content=ElevatedButton(
            on_click=lambda e: fill_quotes(e),
            bgcolor='#007C91',
            color="white",
            content=Row(
                alignment=MainAxisAlignment.CENTER,
                controls=[
                    Icon(
                        name=icons.REFRESH_ROUNDED,
                        size=16
                    ),
                    Text(
                        "Cargar cotizaciones",
                        size=12,
                        weight="bold",
                    ),
                ],
            ),
            style=ButtonStyle(
                shape={
                    "": RoundedRectangleBorder(radius=6),
                },
                color={
                    "": "white",
                },
            ),
            height=42,
            width=170,
        ),
    )

def return_category_register_button():
    return Container(
        alignment=alignment.center,
        content=ElevatedButton(
            on_click=lambda e: register_category(e),
            bgcolor='#007C91',
            color="white",
            content=Row(
                alignment=MainAxisAlignment.CENTER,
                controls=[
                    Icon(
                        name=icons.CATEGORY_ROUNDED,
                        size=16
                    ),
                    Text(
                        "Registar categoría",
                        size=12,
                        weight="bold",
                    ),
                ],
            ),
            style=ButtonStyle(
                shape={
                    "": RoundedRectangleBorder(radius=6),
                },
                color={
                    "": "white",
                },
            ),
            height=42,
            width=170,
        ),
    )

def return_register_form_button():
    return Container(
        alignment=alignment.center,
        content=ElevatedButton(
            on_click=lambda e: get_input_data(e),
            bgcolor='#007C91',
            color="white",
            content=Row(
                alignment=MainAxisAlignment.CENTER,
                controls=[
                    Icon(
                        name=icons.CHECK_CIRCLE_ROUNDED,
                        size=16
                    ),
                    Text(
                        "Registar cotización",
                        size=12,
                        weight="bold",
                    ),
                ],
            ),
            style=ButtonStyle(
                shape={
                    "": RoundedRectangleBorder(radius=6),
                },
                color={
                    "": "white",
                },
            ),
            height=42,
            width=170,
        ),
    )

