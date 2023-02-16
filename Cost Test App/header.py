# Header for desktop application

# modules
from flet import *
import flet
from controls import add_to_control_reference, return_control_reference
from form_helper import ButtonNavigation

control_map = return_control_reference()


class AppHeader(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

    def app_header_instance(self):
        add_to_control_reference("AppHeader", self)

    def app_header_brand(self):
        return Container(
            padding=padding.only(right=20),
            content=Text(
                "PERIC LTDA",
                size=16,
                weight="bold",
                italic=True
            )
        )

    def app_header_avatar(self):
        return Container(
            content=IconButton(icons.PERSON)
        )
    
    def app_header_quote_route(self):
        return Container(
            alignment=alignment.center,
            padding=padding.only(left=10, top=0, bottom=0, right=10), 
            on_click=lambda _: self.page.go('/quote'),
            on_hover=lambda e: self.animate_quote_route(e),
            content=Text(
                "Editar Cotización",
                size=13,
                weight="bold",
                text_align=TextAlign.CENTER,
            )
        )
    
    def app_header_register_route(self):
        return Container(
            alignment=alignment.center,
            padding=padding.only(left=20, top=0, bottom=0, right=10), 
            on_click=lambda _: self.page.go('/register'),
            on_hover=lambda e: self.animate_register_route(e),
            content=Text(
                "Registrar Cotización",
                size=13,
                weight="bold",
                text_align=TextAlign.CENTER,
            )
        )

    def app_header_client_route(self):
        return Container(
            alignment=alignment.center,
            padding=padding.only(left=20, top=0, bottom=0, right=10), 
            on_click=lambda _: self.page.go('/client'),
            on_hover=lambda e: self.animate_client_route(e),
            content=Text(
                "Registrar Cliente",
                size=13,
                weight="bold",
                text_align=TextAlign.CENTER,
            )
        )


    def animate_register_route(self, e):
        if e.data == 'true':
            self.controls[0].content.controls[1].controls[0].bgcolor = "white"
            self.controls[0].content.controls[1].controls[0].content.color = "#007C91"
            self.controls[0].content.controls[1].controls[0].update()
            self.controls[0].content.controls[1].controls[0].content.update()
        else:
            self.controls[0].content.controls[1].controls[0].bgcolor = "#007C91"
            self.controls[0].content.controls[1].controls[0].content.color = "white"
            self.controls[0].content.controls[1].controls[0].update()
            self.controls[0].content.controls[1].controls[0].content.update()

    def animate_quote_route(self, e):
        if e.data == 'true':
            self.controls[0].content.controls[1].controls[1].bgcolor = "white"
            self.controls[0].content.controls[1].controls[1].content.color = "#007C91"
            self.controls[0].content.controls[1].controls[1].update()
            self.controls[0].content.controls[1].controls[1].content.update()
        else:
            self.controls[0].content.controls[1].controls[1].bgcolor = "#007C91"
            self.controls[0].content.controls[1].controls[1].content.color = "white"
            self.controls[0].content.controls[1].controls[1].update()
            self.controls[0].content.controls[1].controls[1].content.update()

    def animate_client_route(self, e):
        if e.data == 'true':
            self.controls[0].content.controls[1].controls[2].bgcolor = "white"
            self.controls[0].content.controls[1].controls[2].content.color = "#007C91"
            self.controls[0].content.controls[1].controls[2].update()
            self.controls[0].content.controls[1].controls[2].content.update()
        else:
            self.controls[0].content.controls[1].controls[2].bgcolor = "#007C91"
            self.controls[0].content.controls[1].controls[2].content.color = "white"
            self.controls[0].content.controls[1].controls[2].update()
            self.controls[0].content.controls[1].controls[2].content.update()

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
                    Row(
                        expand=True,
                        alignment=MainAxisAlignment.START,
                        controls=[
                            self.app_header_register_route(),
                            self.app_header_quote_route(),
                            self.app_header_client_route(),
                        ],
                    ),
                    self.app_header_avatar()

                ],
            ),
        )