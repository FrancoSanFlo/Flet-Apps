import flet
from flet import *
from controls import add_to_control_reference, return_control_reference, add_url_control_reference, return_url_control_reference
from btn import add_url_data

control_map = return_control_reference()

class AppSettingsForm(UserControl):
    def __init__(self):
        super().__init__()
    
    def app_form_input_instance(self):
        add_to_control_reference("AppSettingsForm", self)

    def app_form_input_field(self, name:str, expand:int, txt_state:bool, txt_value:str): 
        return Container(
            expand=expand,
            height=70,
            bgcolor='#EBEBEB',
            border_radius=6,
            padding=10,
            content=Column(
                spacing=1,
                controls=[
                    Text(
                        value=name,
                        size=10,
                        color='black',
                        weight='bold',
                    ),
                    TextField(
                        border_color="black",
                        height=35,
                        value=txt_value,
                        disabled=txt_state,
                        text_size=15,
                        content_padding=0,
                        cursor_color="black",
                        cursor_width=1,
                        cursor_height=18,
                        color='black',
                    ),
                ],
            ),
        )

    def return_settings_form_button(self):
        return Container(
            alignment=alignment.center,
            content=ElevatedButton(
                on_click=self.get_url_data,
                bgcolor='#007C91',
                color="white",
                content=Row(
                    alignment=MainAxisAlignment.CENTER,
                    controls=[
                        Icon(
                            name=icons.SAVE_ROUNDED,
                            size=16
                        ),
                        Text(
                            "Guardar direcciones",
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

    def get_url_data(self, e):
        add_url_data()


    def build(self):
        self.app_form_input_instance()

        return Container(
            width=750,
            height=350,
            bgcolor='white10',
            border=border.all(1, "#EBEBEB"),
            border_radius=8,
            padding=15,
            content=Column(
                expand=True,
                controls=[
                    Column(
                        controls=[
                            self.app_form_input_field("URL archivo cotización*", False, False, None),
                            self.app_form_input_field("URL archivo plantilla*", False, False, None),
                            self.app_form_input_field("URL archivo cotización para empresa*", False, False, None),
                        ],
                    ),
                    Divider(height=2, color="transparent"),
                    Row(
                        alignment=MainAxisAlignment.END,
                        controls=[
                            self.return_settings_form_button()
                        ],
                    ),
                ],
            ),
        )