# this is the form class for the desktop app
from flet import *
from controls import add_to_control_reference
from btn import return_form_button # the main button from btn.py

class AppForm(UserControl):
    def __init__(self):
        super().__init__()

    # we need to create the push instance like we did in the header
    def app_form_input_instance(self):
        add_to_control_reference("AppForm", self)

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
        self.app_form_input_instance()

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
                            self.app_form_input_field("Field *", True),
                        ],
                    ),
                    Row(
                        controls=[
                            self.app_form_input_field("Field One*", 3),
                            self.app_form_input_field("Field Two *", 1),
                            self.app_form_input_field("Field Three *", 1),
                        ],
                    ),
                    Divider(height=1, color="transparent"),
                    Row(
                        alignment=MainAxisAlignment.END,
                        controls=[
                            # We need to add a button here, but it's created in a separate file...
                            return_form_button()
                        ]
                    ),
                ],
            ),
        )