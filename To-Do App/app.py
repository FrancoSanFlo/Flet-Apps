"""
    To-Do App created with flet
    Notes:
        1.- This is a full app => UI + Database function
        2.- Slighlty longer video but with more explainations
        3.- Database is local with sqlite3
"""

# modules
import flet
from flet import *
from datetime import datetime
import sqlite3

# Create form class

# UI part is done, now for the final part, we can implement a
# database to store the tasks
# we can create a class for this
class Database:
    def ConnectToDatabse():
        try:
            db = sqlite3.connect('todo.db')
            c = db.cursor()
            c.execute("""CREATE TABLE if not exists tasks (id INTEGER PRIMARY KEY,
            Task VARCHAR(255) NOT NULL, Date VARCHAR(255) NOT NULL)""")
            return db
        except Exception as e:
            print(e)
    
    def ReadDatabase(db):
        c = db.cursor()
        # make sure to name the columns and not SELECT * FROM...
        c.execute("""SELECT Task, Date FROM tasks""")
        records = c.fetchall()
        return records

    def InsertDatabase(db, values):
        c = db.cursor()
        # also make sure to use ? for the inputs for security purposes
        c.execute("INSERT INTO tasks (Task, Date) VALUES (?,?)", values)
        db.commit()

    def DeleteDatabase(db, value):
        c = db.cursor()
        # quick note: here we're assuming that no two task description are the
        # same and as a result we are deleting based on task
        # an ideal app would not do this but instead delete based on the actual inmutable
        # database ID. but for the sake of the tutorial and length, we will do it this way...
        c.execute("DELETE FROM tasks WHERE Task=?", value)
        db.commit()

    def UpdateDatabase(db, value):
        c = db.cursor()
        c.execute("UPDATE tasks SET Task=? WHERE Task=?", value)
        db.commit()

# now that we have all CRUD functions, we can start using with the app

class FormContainer(UserControl):
    def __init__(self, func):
        self.func = func
        super().__init__()

    def build(self):
        return Container(
            width=280,
            height=80,
            bgcolor="bluegrey500",
            opacity=1,  # change later
            border_radius=40,
            margin=margin.only(left=-20, right=-20),
            animate=animation.Animation(400, 'decelerate'),
            animate_opacity=200,
            padding=padding.only(top=45, bottom=45),
            content=Column(
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    TextField(
                        height=48,
                        width=255,
                        filled=True,
                        text_size=12,
                        color='black',
                        border_color="transparent",
                        hint_text='Description...',
                        hint_style=TextStyle(
                            size=11,
                            color='black'
                        ),
                    ),
                    IconButton(
                        content=Text('Add Task'),
                        width=180,
                        height=44,
                        on_click=self.func,  # pass function here
                        style=ButtonStyle(
                            bgcolor={"": 'black'},
                            shape={"": RoundedRectangleBorder(radius=8)},
                        ),
                    ),
                ],
            ),
        )

# need a class to generate a task when the user adds one


class CreateTask(UserControl):
    def __init__(self, task: str, date: str, func1, func2):
        # create two arguments so we can pass in the delete function and edit function when we create an instance of this
        self.task = task
        self.date = date
        self.func1 = func1
        self.func2 = func2
        super().__init__()

    def TaskEditDelete(self, name, color, func):
        return IconButton(
            icon=name,
            width=30,
            icon_size=18,
            icon_color=color,
            opacity=0,
            animate_opacity=200,
            on_click=lambda e: func(self.GetContainerInstance())
        )

    # need the instance identifier so that we can delete it need to be delete
    def GetContainerInstance(self):
        return self  # return the self instance

    def ShowIcons(self, e):
        if e.data == 'true':
            (
                e.control.content.controls[1].controls[0].opacity,
                e.control.content.controls[1].controls[1].opacity
            ) = (1, 1)
            e.control.content.update()
        else:
            (
                e.control.content.controls[1].controls[0].opacity,
                e.control.content.controls[1].controls[1].opacity
            ) = (0, 0)
            e.control.content.update()

    def build(self):
        return Container(
            width=280,
            height=60,
            border=border.all(0.85, 'white54'),
            border_radius=8,
            # show the icons when we hover over them...
            on_hover=lambda e: self.ShowIcons(e),
            clip_behavior=ClipBehavior.HARD_EDGE,
            padding=10,
            content=Row(
                alignment=MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    Column(
                        spacing=1,
                        alignment=MainAxisAlignment.CENTER,
                        controls=[
                            Text(
                                value=self.task,
                                size=10
                            ),
                            Text(
                                value=self.date,
                                size=9,
                                color='white54'
                            ),
                        ],
                    ),
                    # Icon edit and delete
                    Row(
                        spacing=0,
                        alignment=MainAxisAlignment.CENTER,
                        controls=[
                            self.TaskEditDelete(
                                icons.DELETE_ROUNDED, "red500", self.func1),
                            self.TaskEditDelete(
                                icons.EDIT_ROUNDED, "white70", self.func2),
                        ]
                    )
                ],
            ),
        )


def main(page: Page):
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'

    def AddTaskToScreen(e):
        # everytime the user adds a task, we neet to fetch the data and output it to the ain column
        # there are 2 data we need: the task + the date
        #
        dateTime = datetime.now().strftime("%b %d, %Y %I:%M")

        # first, open a connection to the database
        db = Database.ConnectToDatabse() # this returns the db
        Database.InsertDatabase(db, (form.content.controls[0].value, dateTime))
        # we have both values, one the date and time and the other user task
        # finally close the connect
        db.close()

        # we could place the db function within the if statement...

        # recall that we set the form container to form variable. we can use
        # this now to see if there's any content in the textfield
        if form.content.controls[0].value:
            _main_column_.controls.append(
                # we can create an instance of CreateTask() class...
                CreateTask(
                    # it takes two arguments
                    form.content.controls[0].value,  # task description
                    dateTime,
                    # now, the instance takes two more arguments when called...
                    DeleteFunction,
                    UpdateFunction,
                )
            )
            _main_column_.update()

            # recall the show.hide function for the form here
            CreateToDoTask(e)
        else:
            db.close() # make sure it closes even if there is no user input
            pass

    def DeleteFunction(e):
        # delete of task within the DB
        db = Database.ConnectToDatabse()
        Database.DeleteDatabase(db, (e.controls[0].content.controls[0].controls[0].value,))
        # the e.control... is the value from the instance itself
        # we passed it as (value) because it need to be a tuple data type
        db.close()

        # when we want to delete, recall that these instance are in a list => so that means
        # we can simply remove them we want to
        # the instance is passed on as e
        _main_column_.controls.remove(e)  # e is the instance iteself
        _main_column_.update()

    def UpdateFunction(e):
        # we want to update from the form, so we need to pass whatever the user
        # had from the instance back to the form, then change the functions and pass ir back again...
        form.height, form.opacity = 200, 1  # show the form
        (
            form.content.controls[0].value,
            # here we are changing the button function and name...
            # we need to change it from add task to update and so on...
            form.content.controls[1].content.value,
            form.content.controls[1].on_click
        ) = (
            # this is the instance of the task
            e.controls[0].content.controls[0].controls[0].value,
            'Update',
            lambda _: FinalizeUpdate(e),
        )
        form.update()

        # once the user edits, we need to send the correct data back
    def FinalizeUpdate(e):
        # finally, we can update the DB as well
        db = Database.ConnectToDatabse()
        Database.UpdateDatabase(
            db,
            (
                # first we need to get the data we want to change with...
                form.content.controls[0].value,
                # second, we insert the data to check against (the value that
                # this query should look for)
                e.controls[0].content.controls[0].controls[0].value,
            ),
        )

        # we can simply reverse the values from above...
        e.controls[0].content.controls[0].controls[0].value = form.content.controls[0].value
        e.controls[0].content.update()
        # so we can hide the container...
        CreateToDoTask(e)

    # function to show/hide form container
    def CreateToDoTask(e):
        # when we click the ADD iconbutton ...
        if form.height != 200:
            form.height, form.opacity = 200, 1
            form.update()
        else:
            form.height, form.opacity = 80, 0

            form.content.controls[0].value = None
            form.content.controls[1].content.value  = "Add Text"
            form.content.controls[1].on_click = lambda e:AddTaskToScreen(e)
            form.update()

    _main_column_ = Column(
        scroll='hidden',
        expand=True,
        alignment=MainAxisAlignment.START,
        controls=[
            Row(
                alignment=MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    # Some title stuff...
                    Text(
                        "To-Do Items",
                        size=18,
                        weight="bold"
                    ),
                    IconButton(
                        icons.ADD_CIRCLE_ROUNDED,
                        icon_size=18,
                        on_click=lambda e: CreateToDoTask(e),
                    ),
                ],
            ),
            Divider(
                height=8,
                color="white24"
            )
        ],
    )

    # set up some bg and main container
    # The general UI will copy that of a mobile app
    page.add(
        Container(
            # Big bg container
            width=1500,
            height=800,
            margin=10,
            bgcolor="bluegrey900",
            alignment=alignment.center,
            content=Row(
                alignment=MainAxisAlignment.CENTER,
                vertical_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    # Main container
                    Container(
                        width=280,
                        height=600,
                        bgcolor="#0F0F0F",
                        border_radius=40,
                        border=border.all(0.5, "white"),
                        padding=padding.only(top=35, left=20, right=20),
                        clip_behavior=ClipBehavior.HARD_EDGE,  # clip contents to container
                        content=Column(
                            alignment=MainAxisAlignment.CENTER,
                            expand=True,
                            controls=[
                                # main column here...
                                _main_column_,
                                # Form class here ...
                                # pass in the argument for the form class here
                                FormContainer(lambda e:AddTaskToScreen(e)),
                            ]
                        )
                    )
                ],
            ),
        )
    )

    page.update()

    # the form container index is as follows. We can set the long element index
    # as a variable so it can be called faster and easier
    form = page.controls[0].content.controls[0].content.controls[1].controls[0]
    # now we can call form whenever we want to do something with it...

    # now to display it, we need to read the database
    # another note: Flet keepson refreshing when we call the database functions,
    # this could be from my code or from flet itself, but it should be addressed...
    #
    # open connection
    db = Database.ConnectToDatabse()
    # remember that te readatabase() function returns the records...
    # note: return is a tuple data type!!
    # using [::-1] reverses the tuple
    # using [:-1] reverses a list 
    for task in Database.ReadDatabase(db)[::-1]:
        _main_column_.controls.append(
            # same process as before: we create an instance of this class...
            CreateTask(
                task[0], # first item of the returned tuple
                task[1],
                DeleteFunction,
                UpdateFunction
            )
        )
    _main_column_.update()

if __name__ == "__main__":
    flet.app(target=main)
