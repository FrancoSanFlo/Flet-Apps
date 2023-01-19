from flet import *

# this class will generate a new instance of textfield and insert it into the data table

class FormHelper(UserControl):
    def __init__(self, user_input):
        self.user_input = user_input
        super().__init__()

    # whe we update, it works, but we need to set the read only back to True after we leave the text field
    def save_value(self, e):
        self.controls[0].read_only = True
        self.controls[0].update()

    def build(self):
        return TextField(
            value=self.user_input, # we pass the form field values into here
            border_color="transparent",
            height=20,
            text_size=13,
            content_padding=0,
            cursor_color="black",
            cursor_width=1,
            color='black',
            # important changes
            read_only=True,
            on_blur=lambda e: self.save_value(e)
        )
