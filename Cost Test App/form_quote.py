# Form for desktop application

# modules
import flet 
from flet import *
from btn import return_form_button, return_quotes_button
from controls import add_to_control_reference, return_control_reference

# app-modules
from form_helper import ButtonNavigation
from database import *

control_map = return_control_reference()

class AppFormQuote(UserControl):
    def __init__(self):
        super().__init__()
    
    def app_form_input_instance(self):
        add_to_control_reference("AppFormQuote", self)
    
    # some re=usable UI
    def app_form_input_field(self, name:str, expand:int, txt_state:bool, txt_value:str): 
        return Container(
            expand=expand,
            height=45,
            bgcolor='#EBEBEB',
            border_radius=6,
            padding=8,
            content=Column(
                spacing=1,
                controls=[
                    Text(
                        value=name,
                        size=9,
                        color='black',
                        weight='bold'
                    ),
                    TextField(
                        border_color="transparent",
                        height=20,
                        value=txt_value,
                        disabled=txt_state,
                        text_size=13,
                        content_padding=0,
                        cursor_color="black",
                        cursor_width=1,
                        cursor_height=18,
                        color='black',
                    ),
                ],
            ),
        )

    def app_form_input_field_price(self, name:str, expand:int, txt_state:bool): 
            return Container(
                expand=expand,
                height=45,
                bgcolor='#EBEBEB',
                border_radius=6,
                padding=8,
                content=Column(
                    spacing=1,
                    controls=[
                        Text(
                            value=name,
                            size=9,
                            color='black',
                            weight='bold'
                        ),
                        TextField(
                            border_color="transparent",
                            # on_change= lambda e: self.on_change_input(e),
                            height=20,
                            disabled=txt_state,
                            text_size=13,
                            prefix_text="$ ",
                            prefix_style=TextStyle(
                                color='black',
                                weight='bold',
                                size=12,
                            ),
                            content_padding=0,
                            cursor_color="black",
                            cursor_width=1,
                            cursor_height=18,
                            color='black',
                        ),
                    ],
                ),
            )

    def app_form_dropdown_field_status(self, name:str, expand:int):
        return Container(
            expand=expand,
            height=45,
            bgcolor='#EBEBEB',
            border_radius=6,
            padding=8,
            content=Column(
                spacing=1,
                controls=[
                    Text(
                        value=name,
                        size=9,
                        color='black',
                        weight='bold'
                    ),
                    Dropdown(
                        height=20,
                        text_size=10,
                        content_padding=0,
                        text_style=TextStyle(weight="bold"),
                        color='black',
                        alignment=Alignment(0, 0),
                        options=[
                            dropdown.Option("ENVIADA"),
                            dropdown.Option("NO ENVIADA"),
                        ],
                    ),
                ],
            ),
        )

    def app_form_dropdown_field_quote(self, name:str, expand:int):
        return Container(
            expand=expand,
            height=45,
            bgcolor='#EBEBEB',
            border_radius=6,
            padding=8,
            content=Column(
                spacing=1,
                controls=[
                    Text(
                        value=name,
                        size=9,
                        color='black',
                        weight='bold'
                    ),
                    Dropdown(
                        height=20,
                        text_size=10,
                        content_padding=0,
                        text_style=TextStyle(weight="bold"),
                        color='black',
                        alignment=Alignment(0, 0),
                        on_change=lambda e: self.dropdown_quote_changed(e)
                    ),
                ],
            ),
        )

    def app_form_dropdown_field_yesno(self, name:str, expand:int):
        return Container(
            expand=expand,
            height=45,
            bgcolor='#EBEBEB',
            border_radius=6,
            padding=8,
            content=Column(
                spacing=1,
                controls=[
                    Text(
                        value=name,
                        size=9,
                        color='black',
                        weight='bold'
                    ),
                    Dropdown(
                        height=20,
                        text_size=10,
                        content_padding=0,
                        color='black',
                        text_style=TextStyle(weight="bold"),
                        alignment=Alignment(0, 0),
                        options=[
                            dropdown.Option("SI"),
                            dropdown.Option("NO"),
                        ],
                    ),
                ],
            ),
        )

   
    # Function that returns the price with IVA at the moment a change is made in the textfield
    def on_change_input(self, e):
        for key, value in control_map.items():
            if key == 'AppFormQuote':
                # 5TH Row in FormQuote
                price_txt = value.controls[0].content.controls[4].controls[0]
                iva_txt = value.controls[0].content.controls[4].controls[1]
                declared_price = price_txt.content.controls[1].value
                try:
                    if declared_price == '':
                        iva_txt.content.controls[1].value = ''
                        iva_txt.content.controls[1].update()
                    else:
                        con_iva = (int(declared_price) * 0.19) + int(declared_price)
                        iva_txt.content.controls[1].value = int(con_iva)
                        iva_txt.content.controls[1].update()
                except ValueError as v:
                    #TODO: ARREGLAR ERROR STYLE TEXT
                    # price_txt.content.controls[1].error_text = "Ingresar sólo números"
                    # price_txt.content.controls[1].update()
                    print(v)

    def dropdown_quote_changed(self, e):
        db = Database.ConnectToDatabase()
        for key, value in control_map.items():
            if key == 'AppFormQuote':
                record = Database.SearchByQuote(db , [value.controls[0].content.controls[0].controls[0].content.controls[1].value])
                record = list(record)
                for i in range(9, 13):
                    if record[i] == 1:
                        record[i] = 'SI'
                    else:
                        record[i] = 'NO'
                """"NOTE: PARA VER DONDE ESTOY"""
                print(record)

                # First Row From AppFormQuote
                value.controls[0].content.controls[0].controls[1].content.controls[1].value = record[2]
                value.controls[0].content.controls[0].controls[1].content.controls[1].update()

                value.controls[0].content.controls[0].controls[2].content.controls[1].value = record[1]
                value.controls[0].content.controls[0].controls[2].content.controls[1].update()

                value.controls[0].content.controls[0].controls[3].content.controls[1].value = record[3]
                value.controls[0].content.controls[0].controls[3].content.controls[1].update()

                value.controls[0].content.controls[0].controls[4].content.controls[1].value = record[5]
                value.controls[0].content.controls[0].controls[4].content.controls[1].update()

                # Second Row From AppFormQuote
                value.controls[0].content.controls[1].controls[0].content.controls[1].value = record[13]
                value.controls[0].content.controls[1].controls[0].content.controls[1].update()

                value.controls[0].content.controls[1].controls[1].content.controls[1].value = record[15]
                value.controls[0].content.controls[1].controls[1].content.controls[1].update()

                value.controls[0].content.controls[1].controls[2].content.controls[1].value = record[14]
                value.controls[0].content.controls[1].controls[2].content.controls[1].update()

                # Third Row From AppFormQuote
                value.controls[0].content.controls[2].controls[0].content.controls[1].value = record[4]
                value.controls[0].content.controls[2].controls[0].content.controls[1].update()

                # Fourth Row From AppFormQuote
                for db_output in value.controls[0].content.controls[3].controls[:]:
                    if db_output.content.controls[0].value == 'Estado':
                        if record[8] == 1:
                            db_output.content.controls[1].value = 'ENVIADA'
                            db_output.content.controls[1].update()
                        else:
                            db_output.content.controls[1].value = 'NO ENVIADA'
                            db_output.content.controls[1].update()
                count = 9
                for i in range(1, 5):
                    db_output = value.controls[0].content.controls[3].controls[i]
                    db_output.content.controls[1].value = record[count]
                    db_output.content.controls[1].update()
                    count += 1
                db.close()

                # Fifth Row From AppFormQuote 6 y 7
                value.controls[0].content.controls[4].controls[0].content.controls[1].value = record[6]
                value.controls[0].content.controls[4].controls[0].content.controls[1].update()

                value.controls[0].content.controls[4].controls[1].content.controls[1].value = record[7]
                value.controls[0].content.controls[4].controls[1].content.controls[1].update()

    def build(self):
        self.app_form_input_instance()

        return Container(
            expand=True,
            height=500,
            bgcolor='white10',
            border=border.all(1, "#EBEBEB"),
            border_radius=8,
            padding=15,
            content=Column(
                expand=True,
                controls=[
                    Row(
                        controls=[
                            # self.app_form_input_field("Número Cotización", 1, True, return_new_quote()),
                            self.app_form_dropdown_field_quote("Número Cotización", 1),
                            self.app_form_input_field("Rut", 1, False, None),
                            self.app_form_input_field("Cliente", 2, False, None),
                            self.app_form_input_field("Solicitado por", 2, False, None),
                            self.app_form_input_field("Fecha solicitud", 1, True, None),
                        ],
                    ),
                    Row(
                        controls=[
                            self.app_form_input_field("Folio", 1, False, None),
                            self.app_form_input_field("Factoring", 3, False, None),
                            self.app_form_input_field("Fecha factura", 1, False, None),
                        ],
                    ),
                    Row(
                        controls=[
                            self.app_form_input_field("Descripción breve", True, False, None),
                        ],
                    ),
                    Row(
                        controls=[
                            self.app_form_dropdown_field_status("Estado", 1),
                            self.app_form_dropdown_field_yesno("Ganada", 1),
                            self.app_form_dropdown_field_yesno("Entregado", 1),
                            self.app_form_dropdown_field_yesno("Facturado", 1),
                            self.app_form_dropdown_field_yesno("Pagado", 1),
                        ],
                    ),
                    Row(
                        controls=[
                            self.app_form_input_field_price("Neto", 1, False),
                            self.app_form_input_field_price("IVA", 1, True),
                        ],
                    ),
                    Divider(height=2, color="transparent"),
                    Row(
                        alignment=MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            Row(
                                alignment=MainAxisAlignment.START,
                                controls=[
                                    ButtonNavigation(page, 'register', 'Volver atrás', icons.ARROW_BACK_ROUNDED, True, False),
                                ]
                            ),
                            Row(
                                alignment=MainAxisAlignment.END,
                                controls=[
                                # We need to add a button here, but it's created in a separate file...
                                    return_quotes_button(),
                                    return_form_button(),
                                ],
                            ),
                        ],
                    ),
                ],
            )
        )