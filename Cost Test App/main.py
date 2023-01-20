"""
    Cost Test App
    Test for professional practice, DPERIC-LTDA
    Some notes: 
        1.- UI Design 
        2.- CRUD for clients and quotes
        3.- First menu
"""

# modules
from flet import *
import flet
from datetime import datetime

# app/modules
from header import AppHeader
from form_quote import AppFormQuote


class QuoteApp(UserControl):
    def __init__(self):
        super().__init__()

    

def main(page: Page):
    page.title = "Cost Test App"
    page.bgcolor = "#FDFDFD"
    page.padding = 10
    page.add(
        Column(
            expand=True,
            controls=[
                AppHeader(),
                Divider(height=2, color="transparent"),
                AppFormQuote()
            ],
        )
    )
    page.update()


if __name__ == "__main__":
    flet.app(target=main)