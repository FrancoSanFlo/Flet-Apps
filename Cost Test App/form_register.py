# RegisterForm for desktop application

# modules
import flet 
from flet import *
from btn import return_form_button
from controls import add_to_control_reference, return_control_reference

# app-modules
from form_helper import return_date, return_new_quote, ButtonNavigation
from form_quote import AppFormQuote

ontrol_map = return_control_reference()

class AppRegisterForm(UserControl):
    def __init__(self):
        super().__init__()
    
    def app_form_input_instance(self):
        add_to_control_reference("AppRegisterForm", self)

    def build(self):
        self.app_form_input_instance()

        return Container(
            expand=True,
            height=400,
            bgcolor='white10',
            border=border.all(1, "#EBEBEB"),
            border_radius=8,
            padding=15,
            content=Column(
                expand=True,
                controls=[
                    Row(
                        controls=[
                            AppFormQuote.app_form_input_field(self, "Campo de prueba 1", 1, False, None),
                            AppFormQuote.app_form_input_field(self, "Campo de prueba 2", 2, False, None),
                            AppFormQuote.app_form_input_field(self, "Campo de prueba 3", 2, False, None),
                        ]
                    ),
                    Row(
                        controls=[
                            AppFormQuote.app_form_input_field(self, "Campo de prueba 4", 2, False, None),
                            AppFormQuote.app_form_input_field(self, "Campo de prueba 5", 2, False, None),
                            AppFormQuote.app_form_input_field(self, "Campo de prueba 6", 3, True, None),
                            AppFormQuote.app_form_input_field(self, "Campo de prueba 7", 3, True, None),
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
                                    ButtonNavigation(page, 'register', 'No hago nada', icons.PERSON_ROUNDED, False, True)
                                ],
                            ),
                        ],
                    ),
                ],
            ),
        )