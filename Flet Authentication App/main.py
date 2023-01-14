"""Flet with Firebase"""

# Modules
import pyrebase
import flet
from flet import *
import datetime
from functools import partial


# Config File 
# Your web app's Firebase configuration
config  = {
    "apiKey": "AIzaSyBZhdPg5sqr-LBcJ-fz2yIyYtJNfvAClxI",
    "authDomain": "flet-fbase.firebaseapp.com",
    "projectId": "flet-fbase",
    "storageBucket": "flet-fbase.appspot.com",
    "messagingSenderId": "459421754908",
    "appId": "1:459421754908:web:a146523924bfbfbaaa21d9",
    # set database to None
    "databaseURL" : "",
}

# initialize firebase
firebase = pyrebase.initialize_app(config)

# set up authentication manager
auth = firebase.auth()

# UI class
class UserWidget(UserControl):
    def __init__(self, title:str):
        self.title = title
        super().__init__()

    def build(self):
        # is this UI class wiill allow us to create a sign in +
        # registration form at the same time with minimal code

        # the title of the page
        self._title = Container(
            alignment=alignment.center,
            content=Text(
                self.title, # we will pass in the args when we call this class in the main function
                size=15,
                text_align="center",
                weight="bold",
                color="black"
            ),
        )
        
        # the UI that is returned from this class
        return Column(
            horizontal_alignment="center",
            controls=[
                Container(padding=10),
                self._title,
            ],
        )

def main(page: Page):
    # add some basic setup info
    page.title =  "Flet with Firebase"
    page.bgcolor = "#F0F3F6"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    # we can make the forms re-usable by returning the UI once
    def _main_column_():
        return Container(
            width=280,
            height=600,
            bgcolor="#FFFFFF",
            padding=12,
            border_radius=25,
            content=Column(
                spacing=20,
                horizontal_alignment='center'
            )
        )

    # call the class twice, one for sign in the other for registration
    _sign_in_ = UserWidget(
        "Welcome Back!",
    )

    _register_ = UserWidget(
        "Registration",
    )

    # now we create a two column container from _main_column_ 
    # so we can pass in the UserWidget classUI
    _sign_in_main = _main_column_()
    _sign_in_main.content.controls.append(Container(padding=15))
    # passing in the instantized class into this column, so
    # all that's happening is I'm passing the UI generated 
    # by the class into the container returned by _main_column()
    _sign_in_main.content.controls.append(_sign_in_)

    _reg_main = _main_column_()
    _reg_main.content.controls.append(Container(padding=15))
    _reg_main.content.controls.append(_register_)


    # finally, add the UI to the page side-by-side
    page.add(
        Row(
            alignment='center',
            spacing=25,
            controls=[
                _sign_in_main,
                _reg_main,
            ],
        )
    )

if __name__ == "__main__":
    flet.app(target=main, assets_dir="assets")