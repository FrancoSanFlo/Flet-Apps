# file having view dictionary

# modules
from flet import *
import flet

# app-modules
from header import AppHeader
from form_quote import AppFormQuote
from form_register import AppRegisterForm
from data_table import AppDataTable
from form_client import AppClientForm
from form_edit_client import AppEditClientForm



def views_handler(page):
    return {
        '/register': View(
            route='/register',
            bgcolor="#FDFDFD",
            padding = 10,
            controls=[
                AppHeader(page),
                Divider(height=2, color="transparent"),
                AppRegisterForm(),
                Column(
                    scroll='hidden',
                    expand=True,
                    controls=[
                        AppDataTable()
                    ],
                ),
            ],
        ),
        '/quote': View(
            route='/quote',
            bgcolor="#FDFDFD",
            controls=[
                AppHeader(page),
                Divider(height=2, color="transparent"),
                AppFormQuote(),
            ],
        ),
        '/client': View(
            route='/client',
            bgcolor="#FDFDFD",
            padding = 10,
            controls=[
                AppHeader(page),
                Divider(height=2, color="transparent"),
                AppClientForm()
            ],
        ),
        '/edit-client': View(
            route='/edit-client',
            bgcolor="#FDFDFD",
            padding = 10,
            controls=[
                AppHeader(page),
                Divider(height=2, color="transparent"),
                AppEditClientForm()
            ],
        )
    }