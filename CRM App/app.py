"""
    App that allows you to add and manage clients
    Some notes:
        1.- Usage data: Name, Lastname, Rut, Company, Date
        2.- Local implementation of sqlite3
"""

# modules
import flet
from flet import *
from datetime import datetime
import sqlite3


class Database:
    def ConnectToDatabse():
        try:
            db = sqlite3.connect('crm.db')
            c = db.cursor()
            c.execute("""CREATE TABLE if not exists clients (id INTEGER PRIMARY KEY,
            Name VARCHAR(255) NOT NULL, Lastname VARCHAR(255) NOT NULL, Rut VARCHAR(255) NOT NULL,
            Company VARCHAR(255), Date VARCHAR(255) NOT NULL)""")
            return db
        except Exception as e:
            print(e)

    def ReadDatabase(db):
        c = db.cursor()
        c.execute("""SELECT Rut FROM clients""")
        records = c.fetchall()
        return records

    def InsertDatabase(db, values):
        c = db.cursor()
        c.execute(
            "INSERT INTO clients (Name, Lastname, Rut, Company, Date) VALUES (?,?,?,?,?)", values)
        db.commit()

    def DeleteDatabase(db, value):
        c = db.cursor()
        c.execute("DELETE FROM clients WHERE Rut=?", value)
        db.commit()

    def UpdateDatabase(db, value):
        c = db.cursor()
        c.execute("UPDATE clients SET Rut=? WHERE Rut=?", value)
        db.commit()

    def FillDropDatabase(db, value):
        c = db.cursor()
        c.execute(
            "SELECT Name, Lastname, Rut, Company FROM clients WHERE Rut=?", value)
        record = c.fetchone()
        return record

class CrmApp(UserControl):
    def __init__(self):
        super().__init__()

    def build(self):
        self.name = TextField(
            label="Nombre",
            hint_text="Nombre",
        )

        self.last_name = TextField(
            label="Apellido",
            hint_text="Apellido",
        )

        self.rut = TextField(
            label="Rut",
            hint_text="12345678-9",
        )

        self.company = TextField(
            label="Empresa",
            hint_text="Nombre empresa",
        )

        self.menu_text = Text(
            value="Menú principal",
            style="headlineMedium",
            italic=True,
            weight="w500",
        )

        self.drop_rut = Dropdown(
            hint_text="Rut",
            on_change=self.dropdown_changed
        )

        return Column(
            width=900,
            spacing=20,
            expand=True,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            controls=[
                Row(
                    alignment=MainAxisAlignment.CENTER,
                    controls=[
                        self.menu_text,
                        Icon(name=icons.MENU)
                    ],
                ),
                self.name,
                self.last_name,
                self.rut,
                self.company,
                Row(
                    alignment=MainAxisAlignment.CENTER,
                    controls=[
                        IconButton(
                            content=Text("Ingresar"),
                            width=600,
                            icon_color='black',
                            on_click=lambda e: self.add_clicked(e),
                            style=ButtonStyle(
                                bgcolor={"": '#6d7280'},
                                shape={
                                    "": CountinuosRectangleBorder(radius=10)
                                }
                            ),
                        ),
                        IconButton(
                            content=Icon(icons.REFRESH),
                            on_click=lambda e: self.refresh_fields(e),
                            tooltip="Refrescar datos"
                        )
                    ],
                ),
                Divider(
                    height=10,
                    color="white24"
                ),
                Row(
                    alignment=MainAxisAlignment.SPACE_EVENLY,
                    vertical_alignment=CrossAxisAlignment.CENTER,
                    controls=[
                        self.drop_rut,
                        IconButton(
                            content=Text("Eliminar"),
                            width=250,
                            icon_color='black',
                            on_click=lambda e: self.delete_client(e),
                            style=ButtonStyle(
                                bgcolor={"": '#6d7280'},
                                shape={
                                    "": CountinuosRectangleBorder(radius=10)
                                }
                            )
                        )
                    ]
                )
            ],
        )

    def add_clicked(self, e):
        dateTime = datetime.now().strftime("%b %d, %Y %I:%M")

        db = Database.ConnectToDatabse()
        Database.InsertDatabase(
            db, (self.name.value, self.last_name.value, self.rut.value, self.company.value, dateTime))
        db.close()
        self.drop_rut.options.append(dropdown.Option(self.rut.value))

        self.name.value = ""
        self.last_name.value = ""
        self.rut.value = ""
        self.company.value = ""

        self.update()

    def dropdown_changed(self, e):
        db = Database.ConnectToDatabse()
        data = Database.FillDropDatabase(db, [self.drop_rut.value])
        db.close()
        self.name.value = data[0]
        self.last_name.value = data[1]
        self.rut.value = data[2]
        self.company.value = data[3]

        self.update()

    def refresh_fields(self, e):
        self.name.value = ""
        self.last_name.value = ""
        self.rut.value = ""
        self.company.value = ""

        self.update()
    
    def find_option(self, option_rut):
        for option in self.drop_rut.options:
            if option_rut == option.key:
                return option
        return None

    def delete_client(self, e):
        db = Database.ConnectToDatabse()
        option = self.find_option(self.drop_rut.value)
        Database.DeleteDatabase(db, [self.drop_rut.value])
        if option != None:
            self.drop_rut.options.remove(option)
            self.update()
        db.close()

        self.name.value = ""
        self.last_name.value = ""
        self.rut.value = ""
        self.company.value = ""

        self.update()
        

def main(page: Page):
    page.title = "CRM App By Franco Sánchez"
    page.horizontal_alignment = "center"
    page.scroll = "adaptive"
    crm = CrmApp()

    page.add(crm)

    page.update()

    db = Database.ConnectToDatabse()
    for rut in Database.ReadDatabase(db)[::-1]:
        crm.drop_rut.options.append(dropdown.Option(rut[0]))
    crm.update()

    page.update()


if __name__ == "__main__":
    flet.app(target=main)