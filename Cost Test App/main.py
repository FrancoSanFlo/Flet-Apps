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

# app-modules
from header import AppHeader
from form_quote import AppFormQuote
from database import Database
from views import views_handler
    

db = Database.ConnectToDatabse()
db.close()


def main(page: Page):
    page.title = "PERIC LTDA APP"
    page.bgcolor = "#FDFDFD"
    page.padding = 10
    
    def route_change(route):
        page.views.clear()
        page.views.append(
            views_handler(page)[page.route]
        )

    page.on_route_change = route_change
    page.go('/cotizaciones')
    page.update()


if __name__ == "__main__":
    flet.app(target=main)