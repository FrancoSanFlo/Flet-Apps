# Form helper for desktop application

# modules
from datetime import datetime
from openpyxl import *
from database import *
from flet import *
from controls import return_control_reference

control_map = return_control_reference()


def return_date():
    return datetime.now().strftime("%d-%m-%Y")
    
# NOTE: ÚLTIMO REGISTRO VALIDADO
def return_new_quote():
    db = Database.ConnectToDatabase()
    new_quote = 0
    quote = Database.LastRecord(db)
    if quote == None:
        new_quote = 1
        return new_quote
    else:
        new_quote = int(quote[1]) + 1
        return new_quote

# NOTE: VALIDATION FOR LAST RECORD IN CLIENTES TABLE
def return_new_client_code():
    new_client_code = ''
    db = Database.ConnectToDatabase()
    last_client_code = Database.LastReadCode(db) 
    if last_client_code[0] == None:
        new_client_code = '001'
        return new_client_code
    else:
        int_client = int(last_client_code[0]) + 1
        if len(str(int_client)) == 1:
            new_client_code = '00' + str(int_client)
        elif len(str(int_client)) == 2:
            new_client_code = '0' + str(int_client)
        else:
            new_client_code = str(int_client)
        return new_client_code

def return_existence(rut):
    db = Database.ConnectToDatabase()
    repetido = Database.SearchRutExists(db, [rut])
    return True if repetido != None else False

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


class Categoria:
    def __init__(self,
        nombre_categoria,
        tipo_unidad,
        cantidad,
        valor_unitario,
        subtotal
    ):
        self.nombre_categoria = nombre_categoria
        self.tipo_unidad = tipo_unidad
        self.cantidad = cantidad
        self.valor_unitario = valor_unitario
        self.subtotal = subtotal


class Cliente:
    def __init__(self,
        codigo_cliente,
        rut,
        cliente,
        fono,
        direccion
    ):
        self.codigo_cliente = codigo_cliente
        self.rut = rut
        self.cliente = cliente
        self.fono = fono
        self.direccion = direccion

    


# TODO: VERIFICAR FUNCIONALIDAD DE ESTE BOTÓN
class ButtonNavigation(UserControl):
    def __init__(self, page, rout:str, txt_value:str, icon, icon_state1:bool, icon_state2:bool):
        super().__init__()
        self.page = page
        self.rout = rout
        self.txt_value = txt_value
        self.icon = icon
        self.icon_state1 = icon_state1
        self.icon_state2 = icon_state2

    #re=usable UI Button Navigation
    def build(self):
        return Container(
        alignment=alignment.center,
        content=ElevatedButton(
            on_click=lambda _: self.page.go(f'/{self.rout}'),
            bgcolor='#007C91',
            color="white",
            content=Row(
                alignment=MainAxisAlignment.CENTER,
                vertical_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    Icon(
                        visible=self.icon_state1,
                        name=self.icon,
                        size=12
                    ),
                    Text(
                        value=self.txt_value,
                        size=12,
                        weight="bold",
                    ),
                    Icon(
                        visible=self.icon_state2,
                        name=self.icon,
                        size=12
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


class FormHelper(UserControl):
    def __init__(self, user_input):
        self.user_input = user_input
        super().__init__()

    # whe we update, it works, but we need to set the read only back to True after we leave the text field
    def save_value(self, e):
        self.controls[0].read_only = True
        self.controls[0].update()

    def build(self):
        return TextField(
            value=self.user_input, # we pass the form field values into here
            border_color="transparent",
            height=20,
            text_size=13,
            content_padding=0,
            cursor_color="black",
            cursor_width=1,
            color='black',
            # important changes
            read_only=True,
            # on_blur=lambda e: self.save_value(e)
        )