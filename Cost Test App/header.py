# Header for desktop application

# modules
from flet import *
import flet
from controls import add_to_control_reference, return_control_reference

control_map = return_control_reference()


class AppHeader(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

    def app_header_instance(self):
        add_to_control_reference("AppHeader", self)

    def app_header_brand(self):
        return Container(
            content=Text(
                "PERIC LTDA",
                size=15,
                weight="bold",
                italic=True
            )
        )

    def app_header_avatar(self):
        return Container(
            content=IconButton(icons.PERSON)
        )

    def build(self):
        self.app_header_instance()

        return Container(
            expand=True,
            height=70,
            bgcolor="#007C91",
            border_radius=border_radius.only(topLeft=20, topRight=20),
            padding=padding.only(left=20, right=20),
            content=Row(
                expand=True,
                alignment=MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    self.app_header_brand(),
                    self.app_header_avatar()
                ],
            ),
        )