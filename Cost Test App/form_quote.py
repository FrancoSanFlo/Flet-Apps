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
                        color='black'
                    ),
                ],
            ),
        )

    def build(self):
        return Container(
            expand=True,
            height=190,
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
                ],
            )
        )