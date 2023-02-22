# Client Register Form for desktop application

#modules
import flet 
from flet import *
from controls import add_to_control_reference, return_control_reference

# app_modules
from form_quote import AppFormQuote
from form_helper import return_new_client_code
from btn import return_client_form_button

control_map = return_control_reference()

class AppClientForm(UserControl):
    def __init__(self):
        super().__init__()

    def app_form_input_instance(self):
        add_to_control_reference("AppClientForm", self)

    def app_rut_input_field(self, name:str, expand:int, txt_state:bool, txt_value:str): 
        return Container(
            expand=expand,
            height=45,
            bgcolor='#EBEBEB',
            border_radius=6,
            padding=8,
            tooltip="Sin puntos, ni guión",
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
                        max_length=9,
                        counter_style=TextStyle(
                            color='black', 
                            size=10,
                            weight='bold'
                        ),

                    ),
                ],
            ),
        )

    def app_phone_input_field(self, name:str, expand:int, txt_state:bool, txt_value:str): 
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
                        max_length=8,
                        prefix_text="9 ",
                        prefix_style=TextStyle(
                            color='black',
                            weight='bold',
                            size=12,
                        ),
                        counter_style=TextStyle(
                            color='black', 
                            size=10,
                            weight='bold'
                        ),

                    ),
                ],
            ),
        )

    def build(self):
        self.app_form_input_instance()

        return Container(
            expand=True,
            height=150,
            bgcolor='white10',
            border=border.all(1, "#EBEBEB"),
            border_radius=8,
            padding=15,
            content=Column(
                expand=True,
                    controls=[
                        Row(
                          controls=[
                            AppFormQuote.app_form_input_field(self, "Código cliente", 1, True, return_new_client_code()),
                            self.app_rut_input_field("Rut", 1, False, None),
                            AppFormQuote.app_form_input_field(self, "Cliente", 2, False, None),
                            self.app_phone_input_field("Teléfono", 1, False, None),
                            AppFormQuote.app_form_input_field(self, "Dirección", 2, False, None),
                          ]  
                        ),
                        Divider(height=2, color="transparent"),
                        Row(
                            alignment=MainAxisAlignment.END,
                            controls=[
                                return_client_form_button()
                            ],
                        ),
                    ],
            ),
        )