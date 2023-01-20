# Header for desktop application

# modules
from flet import *
import flet

class AppHeader(UserControl):
    def __init__(self):
        super().__init__()

    def app_header_brand(self):
        return Container(
            content=Text(
                "Cost Test App",
                size=15
            )
        )

    def app_header_avatar(self):
        return Container(
            content=IconButton(icons.PERSON)
        )

    def build(self):
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