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
    "apiKey": "",
    "authDomain": "",
    "projectId": "",
    "storageBucket": "",
    "messagingSenderId": "",
    "appId": "",
    # set database to None
    "databaseURL" : "",
}

# initialize firebase
firebase = pyrebase.initialize_app(config)

# set up authentication manager
auth = firebase.auth()

# UI class
class UserWidget(UserControl):
    def __init__(self, title:str, sub_title:str, btn_name:str, func):
        self.title = title
        self.sub_title = sub_title
        self.btn_name = btn_name
        self.func = func
        super().__init__()

    # for the text fields, we need to create a separate function
    def InputTextField(self, text:str, hide:bool):
        return Container(
            alignment=alignment.center,
            content=TextField(
                # the following are some basic UI designs that can be changed as needed.
                height=48,
                width=255,
                bgcolor="#F0F3F6",
                text_size=12,
                color="black",
                border_color="transparent",
                hint_text=text, # we pass this in during the build
                filled=True,
                cursor_color="black",
                hint_style=TextStyle(
                    size=11,
                    color="black"
                ),
                password=hide, # set to true or false to show/hide password input
            ),
        )

    # Now we need the sig in/register button => this is alternative sign-in i.e., google, facebook, etc...
    def SignInOption(self, path:str, name:str):
        return Container(
            content=ElevatedButton(
                content=Row(
                    alignment="center",
                    spacing=4,
                    controls=[
                        Image(
                            src=path, # path to image
                            width=30,
                            height=30,
                        ),
                        Text(
                            name, # name of sign in option
                            color="black",
                            size=11,
                            weight='bold'
                        )
                    ],
                ),
                style=ButtonStyle(
                    shape={
                        "": RoundedRectangleBorder(radius=8)
                    },
                    bgcolor={
                        "": "#F0F3F6"
                    }
                ),
            )
        )


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

        # Now that the basic set up is donde, we can start adding more UI easily

        # sub title fot the title
        self._sub_title = Container(
            alignment=alignment.center,
            content=Text(
                self.sub_title,
                size=12,
                text_align="center",
                color="black",
            )
        )

        # main sign-in UI here
        self._sign_in = Container(
            content=ElevatedButton(
                on_click=partial(self.func),
                content=Text(
                    self.btn_name, # name of button
                    size=11,
                    weight="bold"
                ),
                style=ButtonStyle(
                    shape={
                        "": RoundedRectangleBorder(radius=8)
                    },
                    color={
                        "": "White",
                    },
                ),
                height=48,
                width=255,
            )
        )
        
        # the UI that is returned from this class
        return Column(
            horizontal_alignment="center",
            controls=[
                Container(padding=10),
                self._title,
                # add new UI to the build
                self._sub_title,
                #
                Column(
                    spacing=12,
                    controls=[
                        self.InputTextField("Email", 
                        False),
                        self.InputTextField("Password", 
                        True)
                    ],
                ),
                Container(padding=5),
                self._sign_in,
                Container(padding=5),
                # Column for alternative sig-ins
                Column(
                    horizontal_alignment="center",
                    controls=[
                        Container(
                            content=Text(
                                "Or continue with",
                                size=10,
                                color="black",
                            )
                        ),
                        self.SignInOption("./assets/facebook.png", "Facebook"),
                        self.SignInOption("./assets/google.png", "Google"),
                    ],
                )
            ],
        )

def main(page: Page):
    # add some basic setup info
    page.title =  "Flet with Firebase"
    page.bgcolor = "#F0F3FF"
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
    
    # Start developing some functions to interact with firebase
    def _register_user(e):
        try:
            # pyrebase allows us to wrap firebase code and easily execute functions.
            auth.create_user_with_email_and_password(
                # we need the email and password as arguments, which we can get from the input fields.
                # recall that we know the position of input fields and how to access their parent controls.
                _register_.controls[0].controls[3].controls[0].content.value,
                _register_.controls[0].controls[3].controls[1].content.value
            )
            
            # if we registered to firebase, we can print OK to the terminal
            print("Registration OK!")
        except Exception as e:
            print(e)

    # we can also create sign-in validation for registered users, and we can generate different type of data.
    def _sing_in(e):
        try:
            user = auth.sign_in_with_email_and_password(
                # we need to get the email an password again, as above
                _sign_in_.controls[0].controls[3].controls[0].content.value,
                _sign_in_.controls[0].controls[3].controls[1].content.value
            )

            info = auth.get_account_info(user['idToken'])

            # we can see the data generated by printing info
            # print(info)
            # so we get a lot of info from the user

            data = ["createdAt", "lastLoginAt",]

            # recall that the info we printed to the terminal was a dict data type, so we need to parse the keys and values properly
            for key in info:
                if key == 'users': # this is the user key named users
                    for item in data:
                        print(item + " " + datetime.datetime.fromtimestamp(
                                int(info[key][0][item]) / 1000
                            ).strftime("%D - %H:%M %p")
                        )
            
            # clear the input fields
            _sign_in_.controls[0].controls[3].controls[0].content.value = None
            _sign_in_.controls[0].controls[3].controls[1].content.value = None
            _sign_in_.controls[0].controls[3].update()

            # it also sends an error if the user already exists.
        except:
            print("Wrong email or password!")


    # call the class twice, one for sign in the other for registration
    _sign_in_ = UserWidget(
        "Welcome Back!",
        # add in the argument in the main function
        "Enter your account details below.",
        "Sign In",
        # partianl function, we can pass in a function as such here
        _sing_in
    )

    _register_ = UserWidget(
        "Registration",
        "Register your email and password below.",
        "Register",
        _register_user

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