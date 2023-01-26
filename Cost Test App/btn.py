# this is the main file where we handle user input data

# modules
from flet import *
from controls import return_control_reference
from database import Database
from openpyxl import *
# from form_helper import FormHelper

control_map = return_control_reference()

class Cotizacion:
    def __init__(self, 
        n_cotizacion, 
        rut, 
        cliente, 
        solicitado_por,
        fecha_solicitud,
        folio,
        factoring,
        fecha_factura,
        descripcion,
        estado: int,
        ganada: int,
        entregado: int,
        facturado: int,
        pagado: int,
        neto,
        iva
    ):
        self.n_cotizacion = n_cotizacion
        self.rut = rut
        self.cliente = cliente
        self.solicitado_por = solicitado_por
        self.fecha_solicitud = fecha_solicitud
        self.folio = folio
        self.factoring = factoring
        self.fecha_factura = fecha_factura
        self.descripcion = descripcion
        self.estado = estado
        self.ganada = ganada
        self.entregado = entregado
        self.facturado = facturado
        self.pagado = pagado
        self.neto = neto
        self.iva = iva


def return_cotizacion(data_quote):
    n_cotizacion = data_quote[0]
    rut = data_quote[1]
    cliente = data_quote[2]
    solicitado_por = data_quote[3]
    fecha_solicitud = data_quote[4]
    folio = data_quote[5]
    factoring = data_quote[6]
    fecha_factura = data_quote[7]
    descripcion = data_quote[8]
    estado = data_quote[9]
    ganada = data_quote[10]
    entregado = data_quote[11]
    facturado = data_quote[12]
    pagado = data_quote[13]
    neto = data_quote[14]
    iva = data_quote[15]
    
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

    new_estado = ''
    if cotizacion.estado == 1:
        new_estado = 'ENVIADA'
    else:
        new_estado = 'NO ENVIADA'

    ordered_data_quote = [
        cotizacion.n_cotizacion,
        cotizacion.cliente,
        cotizacion.rut,
        cotizacion.solicitado_por,
        cotizacion.descripcion,
        cotizacion.fecha_solicitud,
        cotizacion.neto,
        cotizacion.iva,
        new_estado,
        cotizacion.ganada,
        cotizacion.entregado,
        cotizacion.facturado,
        cotizacion.pagado,
        cotizacion.folio,
        cotizacion.fecha_factura,
        cotizacion.factoring
    ]

    return cotizacion, ordered_data_quote

def get_input_data(e):
    data_cotizacion = []
    wb = load_workbook('C:\\Users\\franc\\Desktop\\ejemplo_cot.xlsx', data_only=True)
    ws = wb.active
    # min_row = ws.min_row
    max_row = int(ws.max_row) + 1
    min_column = ws.min_column
    # max_column = ws.max_column

    for key, value in control_map.items():
        if key == 'AppFormQuote':
            for user_input in value.controls[0].content.controls[0].controls[:]:
                data_cotizacion.append(user_input.content.controls[1].value)

            for user_input in value.controls[0].content.controls[1].controls[:]:
                data_cotizacion.append(user_input.content.controls[1].value)

            for user_input in value.controls[0].content.controls[2].controls[:]:
                data_cotizacion.append(user_input.content.controls[1].value)

            for user_input in value.controls[0].content.controls[3].controls[:]:
                if user_input.content.controls[1].value == 'SI' or  user_input.content.controls[1].value == 'ENVIADA':
                    data_cotizacion.append(1)
                elif user_input.content.controls[1].value == 'NO' or  user_input.content.controls[1].value == 'NO ENVIADA':
                    data_cotizacion.append(0)
                else:
                    data_cotizacion.append(user_input.content.controls[1].value)
            
            for user_input in value.controls[0].content.controls[4].controls[:]:
                data_cotizacion.append(str(user_input.content.controls[1].value))

    ctz, ordered_data_quote = return_cotizacion(data_cotizacion)

    # Calling to the DB Class
    db = Database.ConnectToDatabse()
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

    for i in ordered_data_quote:
        if i == 1:
            ws.cell(max_row,min_column).value = 'SI'
        elif i == 0:
            ws.cell(max_row,min_column).value = 'NO'
        else:
            ws.cell(max_row,min_column).value = i
            
        min_column += 1


    min_column = ws.min_column
    wb.save('C:\\Users\\franc\\Desktop\\ejemplo_cot.xlsx')
    wb.close()

def return_form_button():
    return Container(
        alignment=alignment.center,
        content=ElevatedButton(
            on_click=lambda e: get_input_data(e),
            bgcolor='#007C91',
            color="white",
            content=Row(
                controls=[
                    Icon(
                        name=icons.ADD_ROUNDED,
                        size=12
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
            width=220,
        ),
    )