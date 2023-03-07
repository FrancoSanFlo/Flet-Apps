# RegisterForm for desktop application

# modules
import flet 
from flet import *
from btn import return_category_register_button, return_clients_button
from controls import add_to_control_reference, return_control_reference
from database import *

# app-modules
from form_helper import return_date, return_new_quote, ButtonNavigation
from form_quote import AppFormQuote
from btn import get_input_data

control_map = return_control_reference()

class AppRegisterForm(UserControl):
    def __init__(self):
        super().__init__()
    
    def app_form_input_instance(self):
        add_to_control_reference("AppRegisterForm", self)

    # Duplicated code TODO: try to refactor this code fragment
    def app_register_form_field_price(self, name:str, expand:int, txt_state:bool): 
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
                            on_change= lambda e: self.on_change_input(e),
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

    def app_register_form_total_price(self, name:str, expand:int, txt_state:bool, txt_value:str): 
        return Container(
            expand=expand,
            height=45,
            width=222,
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

    def app_form_dropdown_field_client_code(self, name:str, expand:int):
        return Container(
            expand=expand,
            height=45,
            width=180,
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

    def return_register_form_button(self):
        return Container(
            alignment=alignment.center,
            content=ElevatedButton(
                on_click=self.get_data,
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

    def get_data(self, e):
        boolean_value, value, icon_name = get_input_data()
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

    # Operations
    def on_change_input(self, e):
        for key, value in control_map.items():
            if key == 'AppRegisterForm':
                # 3RD Row in FormQuote
                amount = value.controls[0].content.controls[2].controls[2] # Accesing to CONTROL
                amount_value = amount.content.controls[1].value
                unit = value.controls[0].content.controls[2].controls[3] # Accesing to CONTROL
                unit_value = unit.content.controls[1].value
                subtotal = value.controls[0].content.controls[2].controls[4] # Accesing to CONTROL
                try:
                    if unit_value == '':
                        subtotal.content.controls[1].value = ''
                        subtotal.content.controls[1].update()
                        amount.content.controls[1].value = ''
                        amount.content.controls[1].update()
                    else:
                        total_of_subtotal = (int(amount_value)) * int(unit_value)
                        subtotal.content.controls[1].value = int(total_of_subtotal)
                        subtotal.content.controls[1].update()
                except ValueError as v:
                    print(v)

    def dropdown_client_changed(self, e):
        db = Database.ConnectToDatabase()
        for key, value in control_map.items():
            if key == 'AppRegisterForm':
                record = Database.SearchByCode(db , [value.controls[0].content.controls[5].controls[0].controls[1].content.controls[1].value])
                record = list(record)

                value.controls[0].content.controls[0].controls[1].content.controls[1].value = record[1]
                value.controls[0].content.controls[0].controls[1].content.controls[1].update()
                value.controls[0].content.controls[0].controls[2].content.controls[1].value = record[2]
                value.controls[0].content.controls[0].controls[2].content.controls[1].update()

    def build(self):
        self.app_form_input_instance()

        return Container(
            expand=True,
            height=300,
            bgcolor='white10',
            border=border.all(1, "#EBEBEB"),
            border_radius=8,
            padding=15,
            content=Column(
                expand=True,
                controls=[
                    Row(
                        controls=[
                            AppFormQuote.app_form_input_field(self, "Número Cotización", 1, True, return_new_quote()),
                            AppFormQuote.app_form_input_field(self, "Rut", 1, True, None),
                            AppFormQuote.app_form_input_field(self, "Cliente", 2, True, None),
                            AppFormQuote.app_form_input_field(self, "Solicitado por", 2, False, None),
                            AppFormQuote.app_form_input_field(self, "Fecha", 1, True, return_date()),
                        ]
                    ),
                    Row(
                        controls=[
                            AppFormQuote.app_form_input_field(self, "Descripción", 2, False, None),
                            AppFormQuote.app_form_input_field(self, "Gestor", 1, True, "DRAGO PERIC"),
                        ]
                    ),
                    Row(
                        controls=[
                            AppFormQuote.app_form_input_field(self, "Categoría", 7, False, None),
                            AppFormQuote.app_form_input_field(self, "Tipo Unidad", 1, True, "GL"),
                            AppFormQuote.app_form_input_field(self, "Cantidad", 1, False, None),
                            self.app_register_form_field_price("Valor unitario", 1, False),
                            self.app_register_form_field_price("Subtotal", 1, True),
                        ]
                    ),
                    Row(
                        alignment=MainAxisAlignment.END,
                        controls=[
                            self.app_register_form_total_price("Neto", 0, True, None)
                        ]
                    ),
                    Divider(height=2, color="transparent"),
                    Row(
                        alignment=MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            Row(
                                alignment=MainAxisAlignment.START,
                                controls=[
                                    return_clients_button(),
                                    self.app_form_dropdown_field_client_code("Código cliente", 0)
                                ],
                            ),
                            Row(
                                alignment=MainAxisAlignment.END,
                                controls=[
                                    self.return_register_form_button(),
                                    return_category_register_button(),
                                ],
                            ),
                        ],
                    ),
                ],
            ),
        )