""" Flet Data Table Desktop App """

# modules
import flet
from flet import *
from header import AppHeader # application header
from form import AppForm # application input form
from data_table import AppDataTable # application data table

def main(page : Page):
    page.bgcolor = "#FDFDFD"
    page.padding = 10
    page.add(
        # main column where each app component will be placed
        Column(
            expand=True,
            controls=[
                # class instances go here
                AppHeader(),
                Divider(height=2, color="transparent"),
                AppForm(),
                # we call the data table class inside this column
                Column(
                    scroll='hidden',
                    expand=True,
                    controls=[
                        AppDataTable()
                    ]
                )
            ],
        )
    )
    page.update()
    pass

if __name__ == "__main__":
    flet.app(target=main)