# Form for desktop application

# modules
import flet 
from flet import *

class AppFormQuote(UserControl):
    def __init__(self):
        super().__init__()
    
    # some re=usable UI
    def app_form_input_field(self, name:str, expand:int): 
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
                        text_size=13,
                        content_padding=0,
                        color='black',
                        options=[
                            dropdown.Option("ENVIADA"),
                            dropdown.Option("NO ENVIADA"),
                        ],
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
                        text_size=13,
                        content_padding=0,
                        color='black',
                        options=[
                            dropdown.Option("SI"),
                            dropdown.Option("NO"),
                        ],
                    ),
                ],
            ),
        )
        pass

    def build(self):
        return Container(
            expand=True,
            height=250,
            bgcolor='white10',
            border=border.all(1, "#EBEBEB"),
            border_radius=8,
            padding=15,
            content=Column(
                expand=True,
                controls=[
                    Row(
                        controls=[
                            self.app_form_input_field("Número Cotización", 1),
                            self.app_form_input_field("Rut", 1),
                            self.app_form_input_field("Cliente", 2),
                            self.app_form_input_field("Solicitado por", 2),
                            self.app_form_input_field("Fecha solicitud", 1),
                        ],
                    ),
                    Row(
                        controls=[
                            self.app_form_input_field("Folio", 1),
                            self.app_form_input_field("Factoring", 3),
                            self.app_form_input_field("Fecha factura", 1),
                        ],
                    ),
                    Row(
                        controls=[
                            self.app_form_input_field("Descripción breve", True),
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
                ],
            )
        )