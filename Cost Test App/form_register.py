# RegisterForm for desktop application

# modules
import flet 
from flet import *
from btn import return_form_button, return_category_register_button, return_register_form_button
from controls import add_to_control_reference, return_control_reference

# app-modules
from form_helper import return_date, return_new_quote, ButtonNavigation
from form_quote import AppFormQuote

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
                    #TODO: ARREGLAR ERROR STYLE TEXT
                    # price_txt.content.controls[1].error_text = "Ingresar sólo números"
                    # price_txt.content.controls[1].update()
                    print(v)



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
                            AppFormQuote.app_form_input_field(self, "Rut", 1, False, None),
                            AppFormQuote.app_form_input_field(self, "Cliente", 2, False, None),
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
                            self.app_register_form_total_price("Total", 0, True, None)
                        ]
                    ),
                    Divider(height=2, color="transparent"),
                    Row(
                        alignment=MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            Row(
                                alignment=MainAxisAlignment.START,
                                controls=[
                                    ButtonNavigation(page, 'quote', 'Editar cotización', icons.ARROW_FORWARD_ROUNDED, False, True),
                                ],
                            ),
                            Row(
                                alignment=MainAxisAlignment.END,
                                controls=[
                                    # ButtonNavigation(page, 'register', 'Registrar categoría', icons.CATEGORY_ROUNDED, False, True),
                                    return_register_form_button(),
                                    return_category_register_button(),
                                    # ButtonNavigation(page, 'register', 'Registrar categoría', icons.PERSON_ROUNDED, False, True),
                                ],
                            ),
                        ],
                    ),
                ],
            ),
        )