# Client Register Form for desktop application

#modules
import flet 
from flet import *
from controls import add_to_control_reference, return_control_reference

# app_modules
from form_quote import AppFormQuote
from form_register import AppRegisterForm
from form_client import AppClientForm
from form_helper import return_new_client_code
from btn import return_edit_clients_button, update_client_input_data
from database import *

control_map = return_control_reference()

class AppEditClientForm(UserControl):
    def __init__(self):
        super().__init__()

    def app_form_input_instance(self):
        add_to_control_reference("AppEditClientForm", self)
    
    def dropdown_client_changed(self, e):
        db = Database.ConnectToDatabase()
        for key, value in control_map.items():
            if key == 'AppEditClientForm':
                record = Database.SearchByCode(db , [value.controls[0].content.controls[0].controls[0].content.controls[1].value])
                record = list(record)

                rut = str(record[1])
                rut = rut.replace('.', '')
                rut = rut.replace('-', '')
                phone = str(record[3])
                
                value.controls[0].content.controls[0].controls[1].content.controls[1].value = rut
                value.controls[0].content.controls[0].controls[1].content.controls[1].update()
                value.controls[0].content.controls[0].controls[2].content.controls[1].value = record[2]
                value.controls[0].content.controls[0].controls[2].content.controls[1].update()
                value.controls[0].content.controls[0].controls[3].content.controls[1].value = phone[1:]
                value.controls[0].content.controls[0].controls[3].content.controls[1].update()
                value.controls[0].content.controls[0].controls[4].content.controls[1].value = record[4]
                value.controls[0].content.controls[0].controls[4].content.controls[1].update()

    def app_form_dropdown_field_client_code(self, name:str, expand:int):
        return Container(
            expand=expand,
            height=45,
            width=150,
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
                        color=colors.WHITE,
                        alignment=Alignment(0, 0),
                        on_change=lambda e: self.dropdown_client_changed(e),
                        focused_border_color="#007C91",
                        filled=True,
                        bgcolor=colors.BLACK38
                    ),
                    
                ],
            ),
        )

    def OpenAlert(e, value, icon_name, color):
        return AlertDialog(
                title_padding=0,
                content_padding=0,
                actions_padding=0,
                content=Container(
                    expand=True,
                    height=45,
                    border_radius=20,
                    bgcolor="white",
                    content=Row(
                        vertical_alignment=CrossAxisAlignment.CENTER,
                        alignment=MainAxisAlignment.SPACE_EVENLY,
                        controls=[
                            Icon(
                                name=icon_name,
                                size=24,
                                color=color,
                            ),
                            Text(
                                value=value,
                                size=20,
                                weight='bold',
                                italic=True,
                                color="#383838"
                            ),
                        ]
                    )
                )
            )

    def update_client(self, e):
        boolean_value, value, icon_name = update_client_input_data()
        if boolean_value:
            open_alert = self.OpenAlert(value, icon_name, "#42AB49")
            self.page.dialog = open_alert
            open_alert.open = True
            self.page.update()
        else:
            open_alert = self.OpenAlert(value, icon_name, "#FF6961")
            self.page.dialog = open_alert
            open_alert.open = True
            self.page.update()

    def return_edit_form_button(self):
        return Container(
            alignment=alignment.center,
            content=ElevatedButton(
                on_click=self.update_client,
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
                            self.app_form_dropdown_field_client_code("Código cliente", 1),
                            AppClientForm.app_rut_input_field(self, "Rut", 1, False, None),
                            AppFormQuote.app_form_input_field(self, "Cliente", 2, False, None),
                            AppClientForm.app_phone_input_field(self, "Teléfono", 1, False, None),
                            AppFormQuote.app_form_input_field(self, "Dirección", 2, False, None),
                          ]  
                        ),
                        Divider(height=2, color="transparent"),
                        Row(
                            alignment=MainAxisAlignment.END,
                            controls=[
                                return_edit_clients_button(),
                                self.return_edit_form_button()
                            ],
                        ),
                    ],
            ),
        )