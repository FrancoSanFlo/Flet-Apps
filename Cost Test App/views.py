# file having view dictionary

# modules
from flet import *
import flet

# app-modules
from header import AppHeader
from form_quote import AppFormQuote
from form_register import AppRegisterForm


def views_handler(page):
    return {
        '/register': View(
            route='/register',
            bgcolor="#FDFDFD",
            padding = 10,
            controls=[
                AppHeader(),
                Divider(height=2, color="transparent"),
                AppRegisterForm(),
                
            ],
        ),
        '/quote': View(
            route='/quote',
            bgcolor="#FDFDFD",
            padding = 10,
            controls=[
                AppHeader(),
                Divider(height=2, color="transparent"),
                AppFormQuote(),
            ],
        )
    }