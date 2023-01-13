# With this method we can separate our pages as views and each view is its own python script.

# modules for the index page = landing page
from flet import View, Column, Container, Text, FilledButton, alignment

# the functions should be the same accross all views so that we can iterate and call them in the main function


def _view_():
    # This is the name of the page that route function parses when looking or changing views
    return View(
        '/about',
        controls=[
            Column(
                controls=[
                    Container(
                        width=450, 
                        height=450, 
                        bgcolor="blue800",
                        alignment=alignment.center,
                        content=Text('About Page'),
                    ),
                    FilledButton(
                        text='Contact',
                        width=120,
                        height=40,
                        # Here we pass the .go method ffrom flet rout so we can trigger the route function we'll implement in the main function
                        # this will send us to the CONTACT PAGE if clicked
                        on_click=lambda e: e.page.go("/contact")
                    )
                ]
            )
        ]
    )
