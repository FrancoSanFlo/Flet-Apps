"""
    Calculator App with Flet
"""

import flet 
from flet import *
from calculator_app import *

def main(page: Page):
    page.title = "Calculator App"
    result = Text(value= "0")
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'

    page.add(
        CalculatorApp()
    ) 
    page.update()

if __name__ == "__main__":
    app(target=main)
    