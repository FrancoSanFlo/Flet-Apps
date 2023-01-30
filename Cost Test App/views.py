# file having view dictionary

# modules
from flet import *
import flet

# app-modules
from header import AppHeader
from form_quote import AppFormQuote


def views_handler(page):
    return {
        '/': View(
            route='/',
            bgcolor="#FDFDFD",
            padding = 10,
            controls=[
                # Home(page)
            ],
        ),
        '/cotizaciones': View(
            route='/cotizaciones',
            bgcolor="#FDFDFD",
            padding = 10,
            controls=[
                AppHeader(page),
                Divider(height=2, color="transparent"),
                AppFormQuote(page),
            ],
        )
    }