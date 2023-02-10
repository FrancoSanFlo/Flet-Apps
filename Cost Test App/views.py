# file having view dictionary

# modules
from flet import *
import flet

# app-modules
from header import AppHeader
from form_quote import AppFormQuote
from form_register import AppRegisterForm
from data_table import AppDataTable



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
                # Container(
                #     offset=transform.Offset(-2,0),
                #     animate_offset=animation.Animation(1000),
                #     content=Column(
                #         expand=True,
                #         controls=[
                #             AppHeader(page),
                #             Divider(height=2, color="transparent"),
                #             AppRegisterForm(),
                #             Column(
                #                 scroll='hidden',
                #                 expand=True,
                #                 visible=False,
                #                 controls=[
                #                     AppDataTable()
                #                 ],
                #             ),

                #         ]
                #     ),
                # ),
            ],
        ),
        '/quote': View(
            route='/quote',
            bgcolor="#FDFDFD",
            padding = 10,
            controls=[
                AppHeader(page),
                Divider(height=2, color="transparent"),
                AppFormQuote(),
            ],
        )
    }