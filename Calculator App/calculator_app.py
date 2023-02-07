import flet
from flet import *


class CalculatorApp(UserControl):
    def __init__(self):
        super().__init__()
        

    def button_clicked(self, e):
        if e.control.data == "0":
            if self.text_field.value == '0':
                pass
            else:
                self.text_field.value = self.text_field.value + '0'
                self.text_field.update()
        if e.control.data == "1":
            if self.text_field.value == '0':
                self.text_field.value = '1'
                self.text_field.update()
            else:
                self.text_field.value = self.text_field.value + '1'
                self.text_field.update()
        if e.control.data == "2":
            if self.text_field.value == '0':
                self.text_field.value = '2'
                self.text_field.update()
            else:
                self.text_field.value = self.text_field.value + '2'
                self.text_field.update()
        if e.control.data == "3":
            if self.text_field.value == '0':
                self.text_field.value = '3'
                self.text_field.update()
            else:
                self.text_field.value = self.text_field.value + '3'
                self.text_field.update()
        if e.control.data == "4":
            if self.text_field.value == '0':
                self.text_field.value = '4'
                self.text_field.update()
            else:
                self.text_field.value = self.text_field.value + '4'
                self.text_field.update()
        if e.control.data == "5":
            if self.text_field.value == '0':
                self.text_field.value = '5'
                self.text_field.update()
            else:
                self.text_field.value = self.text_field.value + '5'
                self.text_field.update()
        if e.control.data == "6":
            if self.text_field.value == '0':
                self.text_field.value = '6'
                self.text_field.update()
            else:
                self.text_field.value = self.text_field.value + '6'
                self.text_field.update()
        if e.control.data == "7":
            if self.text_field.value == '0':
                self.text_field.value = '7'
                self.text_field.update()
            else:
                self.text_field.value = self.text_field.value + '7'
                self.text_field.update()
        if e.control.data == "8":
            if self.text_field.value == '0':
                self.text_field.value = '8'
                self.text_field.update()
            else:
                self.text_field.value = self.text_field.value + '8'
                self.text_field.update()
        if e.control.data == "9":
            if self.text_field.value == '0':
                self.text_field.value = '9'
                self.text_field.update()
            else:
                self.text_field.value = self.text_field.value + '9'
                self.text_field.update()
        if e.control.data == "AC":
            self.text_field.value = '0'
            self.text_field.update()
        if e.control.data == "+/-":
            if self.text_field.value == '0':
                pass
            else:
                if int(self.text_field.value) > 0:
                    self.text_field.value = '-' + self.text_field.value
                    self.text_field.update()

                    pass
                elif int(self.text_field.value) < 0:
                    if '-' in self.text_field.value:
                        self.text_field.value = self.text_field.value.replace(self.text_field.value[0], "")
                        self.text_field.update()
        if e.control.data == "%":
            if self.text_field.value == '0':
                pass
            else:
                self.text_field.value = self.text_field.value + '%'
                self.text_field.update()
        if e.control.data == "/":
            if self.text_field.value == '0':
                pass
            else:
                self.text_field.value = self.text_field.value + '/'
                self.text_field.update()
        if e.control.data == "*":
            if self.text_field.value == '0':
                pass
            else:
                self.text_field.value = self.text_field.value + '*'
                self.text_field.update()
        if e.control.data == "-":
            if self.text_field.value == '0':
                pass
            else:
                self.text_field.value = self.text_field.value + '-'
                self.text_field.update()
        if e.control.data == "+":
            if self.text_field.value == '0':
                pass
            else:
                self.text_field.value = self.text_field.value + '+'
                self.text_field.update()
        if e.control.data == ".":
            if self.text_field.value == '0':
                self.text_field.value = self.text_field.value + '.'
                self.text_field.update()
            else:
                self.text_field.value = self.text_field.value + '.'
                self.text_field.update()
        if e.control.data == "=":
            if self.text_field.value == '0':
                pass
            else:
                try:
                    self.text_field.value = str(eval(str(self.text_field.value)))
                    self.text_field.update()
                except SyntaxError as sy:
                    print(sy)

    def btn_field(self, value:str, _expand:int, _data:str, _bgcolor, _color):
        return ElevatedButton(
            text=value,
            bgcolor=_bgcolor,
            color=_color,
            expand=_expand,
            on_click=lambda e: self.button_clicked(e),
            data=_data
        )

    def build(self):

        self.text_field = Text(
            value="0",
            size=26
        )

        return Container(
            bgcolor='black',
            height=330,
            width=400,
            expand=True,
            padding=20,
            border_radius=10,
            content=Column(
                expand=True,
                controls=[
                    Row(
                        alignment=MainAxisAlignment.END,
                        controls=[
                            self.text_field
                        ]
                    ),
                    Row(
                        controls=[
                            self.btn_field("AC", 1, "AC", colors.BLUE_GREY_100, colors.BLACK),
                            self.btn_field("+/-", 1, "+/-", colors.BLUE_GREY_100, colors.BLACK),
                            self.btn_field("%", 1, "%", colors.BLUE_GREY_100, colors.BLACK),
                            self.btn_field("/", 1, "/", "#F29508", "#D6D7D8"),
                        ]
                    ),
                    Row(
                        controls=[
                            self.btn_field("7", 1, "7", "#393E41", "#D6D7D8"),
                            self.btn_field("8", 1, "8", "#393E41", "#D6D7D8"),
                            self.btn_field("9", 1, "9", "#393E41", "#D6D7D8"),
                            self.btn_field("*", 1, "*", "#F29508", "#D6D7D8"),
                        ]
                    ),
                    Row(
                        controls=[
                            self.btn_field("4", 1, "4", "#393E41", "#D6D7D8"),
                            self.btn_field("5", 1, "5", "#393E41", "#D6D7D8"),
                            self.btn_field("6", 1, "6", "#393E41", "#D6D7D8"),
                            self.btn_field("-", 1, "-", "#F29508", "#D6D7D8"),
                        ]
                    ),
                    Row(
                        controls=[
                            self.btn_field("1", 1, "1", "#393E41", "#D6D7D8"),
                            self.btn_field("2", 1, "2", "#393E41", "#D6D7D8"),
                            self.btn_field("3", 1, "3", "#393E41", "#D6D7D8"),
                            self.btn_field("+", 1, "+", "#F29508", "#D6D7D8"),
                        ]
                    ),
                    Row(
                        controls=[
                            self.btn_field("0", 2, "0", "#393E41", "#D6D7D8"),
                            self.btn_field(".", 1, ".", "#393E41", "#D6D7D8"),
                            self.btn_field("=", 1, "=", "#F29508", "#D6D7D8"),
                        ]
                    ),
                ],
            ),
        )