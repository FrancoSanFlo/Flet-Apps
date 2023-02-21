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
                        on_change=lambda e: self.on_change_rut_input(e),
                        max_length=10,
                        counter_style=TextStyle(
                            color='black', 
                            size=10,
                            weight='bold'
                        ),

                    ),
                ],
            ),
        )

    def on_change_rut_input(self, e):
        for key, value in control_map.items():
            if key == 'AppClientForm':
                rut_aux = ''
                rut = str(value.controls[0].content.controls[0].controls[1].content.controls[1].value)
                # try:
                #     int(rut)
                # except ValueError as ve:
                #     value.controls[0].content.controls[0].controls[1].content.controls[1].error_text = ve
                
                #123456789
                if len(rut) == 8:
                    rut = f'{rut[0:7]}-{rut[-1]}'
                    rut_aux = rut.replace('-', '')
                    value.controls[0].content.controls[0].controls[1].content.controls[1].value = rut
                    value.controls[0].content.controls[0].controls[1].content.controls[1].update()
                    print(rut_aux)


                if len(rut) == 9:
                    # if '-' in rut:
                    #     rut = rut.replace('-', '')
                        
                    rut = f'{rut[0:8]}-{rut[-1]}'
                    value.controls[0].content.controls[0].controls[1].content.controls[1].value = rut
                    value.controls[0].content.controls[0].controls[1].content.controls[1].update()
                value.controls[0].content.controls[0].controls[1].content.controls[1].update()
                
                


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
                            AppFormQuote.app_form_input_field(self, "Teléfono", 1, False, None),
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