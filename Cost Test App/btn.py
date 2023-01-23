# this is the main file where we handle user input data

# modules
from flet import *
from controls import return_control_reference
import sqlite3
# from form_helper import FormHelper

control_map = return_control_reference()


class Database:
    def ConnectToDatabse():
        try:
            db = sqlite3.connect('cotizaciones.db')
            c = db.cursor()
            c.execute("""CREATE TABLE if not exists cotizaciones (id INTEGER PRIMARY KEY,
            Cliente VARCHAR(255) NOT NULL, Rut VARCHAR(255) NOT NULL, Solicitud VARCHAR(255) NOT NULL, Descripcion VARCHAR(255),
            Fecha_creacion VARCHAR(255) NOT NULL, Neto VARCHAR(255) NOT NULL, Iva VARCHAR(255) NOT NULL, Estado BIT NOT NULL,
            Ganada BIT NOT NULL, Entregada BIT NOT NULL, Facturada BIT NOT NULL, Pagado BIT NOT NULL,
            Folio VARCHAR(255) NOT NULL, Fecha_factura VARCHAR(255) NOT NULL, Factoring VARCHAR(255))""")
            return db
        except Exception as e:
            print(e)


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
        pagado: int
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


def get_input_data(e):
    data_cotizacion = []

    for key, value in control_map.items():
        if key == 'AppFormQuote':
            for user_input in value.controls[0].content.controls[0].controls[:]:
                # print(user_input.content.controls[1].value)
                data_cotizacion.append(user_input.content.controls[1].value)

            for user_input in value.controls[0].content.controls[1].controls[:]:
                # print(user_input.content.controls[1].value)
                data_cotizacion.append(user_input.content.controls[1].value)

            for user_input in value.controls[0].content.controls[2].controls[:]:
                # print(user_input.content.controls[1].value)
                data_cotizacion.append(user_input.content.controls[1].value)

            for user_input in value.controls[0].content.controls[3].controls[:]:
                # print(user_input.content.controls[1].value)
                if user_input.content.controls[1].value == 'SI' or  user_input.content.controls[1].value == 'ENVIADA':
                    data_cotizacion.append(1)
                elif user_input.content.controls[1].value == 'NO' or  user_input.content.controls[1].value == 'NO ENVIADA':
                    data_cotizacion.append(0)
                else:
                    data_cotizacion.append(user_input.content.controls[1].value)



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