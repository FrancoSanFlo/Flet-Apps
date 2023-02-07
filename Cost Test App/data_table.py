# main class for datya table UI
# modules
from flet import *
from controls import add_to_control_reference

class AppDataTable(UserControl):
    def __init__(self):
        super().__init__()

    def app_data_table_instance(self):
        add_to_control_reference("AppDataTable", self)

    def build(self):
        self.app_data_table_instance()
        return Row(
            expand=True,
            controls=[
                DataTable(
                    expand=True,
                    border_radius=8,
                    border=border.all(2, '#EBEBEB'),
                    horizontal_lines=border.BorderSide(1, "#EBEBEB"),
                    columns=[
                        DataColumn(
                            Text(
                                "Categoría",
                                size=12,
                                color="black",
                                weight="bold"
                            ),
                        ),
                        DataColumn(
                            Text(
                                "Unidad",
                                size=12,
                                color="black",
                                weight="bold"
                            ),
                        ),
                        DataColumn(
                            Text(
                                "Cantidad",
                                size=12,
                                color="black",
                                weight="bold"
                            ),
                        ),
                        DataColumn(
                            Text(
                                "Valor unitario",
                                size=12,
                                color="black",
                                weight="bold"
                            ),
                        ),
                        DataColumn(
                            Text(
                                "Subtotal",
                                size=12,
                                color="black",
                                weight="bold"
                            ),
                        ),
                    ],
                    # here, we will configure the from button to append the data rows
                    rows=[

                    ],
                ),
            ],
        )