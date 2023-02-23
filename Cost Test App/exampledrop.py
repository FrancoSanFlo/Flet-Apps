import flet 
from flet import *

class AlertDialog_(UserControl):
    def __init__(self, value:str, icon_name):
        self.value = value
        self.icon_name = icon_name
        super().__init__()

    def OpenAlert(e, value, icon_name):
        return AlertDialog(
                title_padding=0,
                content_padding=0,
                actions_padding=0,
                content=Container(
                    width=350,
                    height=50,
                    border_radius=20,
                    bgcolor="transparent",
                    content=Row(
                        vertical_alignment=CrossAxisAlignment.CENTER,
                        alignment=MainAxisAlignment.SPACE_EVENLY,
                        controls=[
                            Icon(
                                name=icon_name,
                                size=20,
                                color="#42AB49",
                            ),
                            Text(
                                value=value,
                                size=20,
                                weight='bold',
                                italic=True,
                                color="white"
                            ),
                        ]
                    )
                )
            )
    
    def Show(self, e):
        open_alert = self.OpenAlert(self.value, self.icon_name)
        self.page.dialog = open_alert
        open_alert.open = True
        self.page.update()
    
    def build(self):
        return ElevatedButton("Open dialog", on_click=self.Show)
        

def main(page: Page):

    page.add(
    AlertDialog_("Ingresado satisfactoriamente", icons.CHECK_CIRCLE_OUTLINE_ROUNDED)
)

app(target=main)