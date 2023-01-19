""" Flet Data Table Desktop App """

# modules
import flet
from flet import *
from header import AppHeader # application header

def main(page : Page):
    page.bgcolor = "#FDFDFD"
    page.padding = 10
    page.add(
        # main column where each app component will be placed
        Column(
            expand=True,
            controls=[
                # class instances go here
                AppHeader()
            ],
        )
    )
    page.update()
    pass

if __name__ == "__main__":
    flet.app(target=main)