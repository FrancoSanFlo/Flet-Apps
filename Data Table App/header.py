# This is the header of the desktop application

# modules
from flet import *
from controls import add_to_control_reference, return_control_reference
# these are the function we just created in the control.py

# we can set the returned dict as a variable at the top of the class
control_map = return_control_reference()

# main class
class AppHeader(UserControl):
    def __init__(self):
        super().__init__()
    
    def app_header_instance(self):
        # this function sets the class instance as a key:value pair in the global dict
        add_to_control_reference("AppHeader", self)
        # so the key => "AppHeader"
        # and the value => self (which is the instance, e.g. the object location in memory)

    # create header inner components
    def app_header_brand(self):
        return Container(
            content=Text(
                "Franco Sánchez",
                size=15
            )
        )

    def app_header_search(self):
        return Container(
            width=320,
            bgcolor="white10",
            border_radius=6,
            opacity=0,
            animate_opacity=320,
            padding=8,
            content=Row(
                spacing=10,
                vertical_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    Icon(
                        name=icons.SEARCH_ROUNDED,
                        size=17,
                        opacity=0.85
                    ),
                    TextField(
                        # some basic UI from my end
                        border_color="transparent",
                        height=20,
                        text_size=14,
                        content_padding=0,
                        cursor_color="white",
                        cursor_width=1,
                        color="white",
                        hint_text="Search",
                        # on_change=lambda e: self.filter_data_table(e)
                    ),
                ],
            )
        )

    def app_header_avatar(self):
        return Container(
            content=IconButton(icons.PERSON)
        )

    # we want to show the search bar whenever the user hovers over the header
    def show_search_bar(self, e):
        if e.data == 'true':
            self.controls[0].content.controls[1].opacity = 1
            self.controls[0].content.controls[1].update()
        else:
            # we want to remove the text when we make the search bar disappear
            self.controls[0].content.controls[1].opacity = 0
            self.controls[0].content.controls[1].update()

    def build(self):
        self.app_header_instance()

        return Container(
            expand=True,
            on_hover=lambda e: self.show_search_bar(e),
            height=60,
            bgcolor='#081D33',
            border_radius=border_radius.only(topLeft=15, topRight=15),
            padding=padding.only(left=15, right=15),
            content=Row(
                expand=True,
                alignment=MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    self.app_header_brand(),
                    self.app_header_search(),
                    self.app_header_avatar(),
                ],
            ),
        )