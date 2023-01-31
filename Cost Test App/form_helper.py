# Form helper for desktop application

# modules
from datetime import datetime
from openpyxl import *
from database import *
from flet import *

def return_date():
    return datetime.now().strftime("%d-%m-%Y")
    
def return_new_quote():
    db = Database.ConnectToDatabase()
    new_quote = Database.LastRecord(db)
    return int(new_quote[1])+1


class ButtonNavigation(UserControl):
    def __init__(self, page, rout:str, txt_value:str, icon, icon_state1:bool, icon_state2:bool):
        super().__init__()
        self.page = page
        self.rout = rout
        self.txt_value = txt_value
        self.icon = icon
        self.icon_state1 = icon_state1
        self.icon_state2 = icon_state2

    #re=usable UI Button Navigation
    def build(self):
        return Container(
        alignment=alignment.center,
        content=ElevatedButton(
            on_click=lambda _: self.page.go(f'/{self.rout}'),
            bgcolor='#007C91',
            color="white",
            content=Row(
                alignment=MainAxisAlignment.CENTER,
                controls=[
                    Icon(
                        visible=self.icon_state1,
                        name=self.icon,
                        size=12
                    ),
                    Text(
                        value=self.txt_value,
                        size=12,
                        weight="bold",
                    ),
                    Icon(
                        visible=self.icon_state2,
                        name=self.icon,
                        size=12
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