# this is the main file where we handle user input data

# modules
from flet import *
from controls import return_control_reference
from form_helper import FormHelper

# get the global map dict
control_map = return_control_reference()

def update_text(e):
    # here, if the user double click the cells, it can become editable by turning off the read_only parameter
    e.control.content.controls[0].read_only = False
    e.control.content.controls[0].update()

# this method will handle the main data from the user.
# but before we can start taking in the data, we need a place store it.
def get_input_data(e):
    # recall that the form instance is saved in the dictionary
    # we can access this now...
    for key, value in control_map.items():
        # get the key called AppForm since it's where the values are
        if key == 'AppForm':
            # once we're in the key, we need to create a DataRow
            data = DataRow(cells=[])
            # once we have the key, we can now loop over the textfields and get the values

            # first for loop is the first row
            for user_input in value.controls[0].content.controls[0].controls[:]:
                # here, we can now append that DataRow...
                data.cells.append(
                    # call the FormHelper class...
                    # make sure to wrap the class in a DATACELL!!
                    DataCell(
                        FormHelper(user_input.content.controls[1].value),
                        # the data cells can now take in some important events,
                        # namely tap events/click events
                        on_double_tap=lambda e: update_text(e)
                    )
                    
                )


            # second for loop is the second row
            for user_input in value.controls[0].content.controls[1].controls[:]:
                # here, we can now append that DataRow...
                data.cells.append(
                    # call the FormHelper class...
                    DataCell(
                        FormHelper(user_input.content.controls[1].value),
                        on_double_tap=lambda e: update_text(e)

                    )
                )

            # now that we have access to the values, we should create a data row + cell to insert it to the data table

        # WE NEED TO UPDATE THE DATA TABLE AFTER WE APPEND
        if key == "AppDataTable":
            value.controls[0].controls[0].rows.append(data)
            value.controls[0].controls[0].update()

# for the button UI, this can be changed to fit the application theme
def return_form_button():
    return Container(
        alignment=alignment.center,
        content=ElevatedButton(
            on_click=lambda e: get_input_data(e),
            bgcolor='#081D33',
            color="white",
            content=Row(
                controls=[
                    Icon(
                        name=icons.ADD_ROUNDED,
                        size=12
                    ),
                    Text(
                        "Add Input Field To Table",
                        size=11,
                        weight="bold",
                    ),
                ],
            ),
            style=ButtonStyle(
                shape={
                    "": RoundedRectangleBorder(radius=6),
                },
                color={
                    "": "white",
                },
            ),
            height=42,
            width=220,
        ),
    )