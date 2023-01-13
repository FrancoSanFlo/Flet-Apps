# Showcasing a quick and cleaner way of routing in Flet - using minimal code and better dir managment

from flet import flet, UserControl, Page
import os, importlib.util

# if we have say 10, 20, even 30 pages, importing all like we did now would be counter intuitive. Instead we can use
# some python modules to help us iterate over the files in the pages folder

_moduleList = {}

# Looking the pages folder using os.walk
# so when using os.walk, we get a tuple with three elements inside each -> we are interested in the root and 
# the folders, not the files.
for root, dirs, __ in os.walk(r'./'):
    # so nowq we want to iterate over the available folders in the root directory
    for dir in dirs:
        #if a folder called pages is there..
        if dir == 'pages':
            # if PAGES directory exists, we want to loop thorugh the files inside it
            for filename in os.listdir(dir):
                # we want the path to the filename which will become our module
                _file = os.path.join(dir, filename)
                # now we wnat to check that the file is indeed a file
                if os.path.isfile(_file):
                    # for all the files... remove the .py extension
                    filename = filename.strip(".py")
                    # now we can append the module into a dictionary...
                    # not append, but add new keys and values
                    _moduleList['/'+filename] = importlib.util.spec_from_file_location(filename, _file)
                    # this importlib.util using the the spec format is beyond the scope for this tutorial, but in
                    # brief, what we did here was generate a key that is string with the 
                    # filename (/index, /contact, /about) and each key has value of a module, just like imported before

# Basic setup in the main function
def main(page: Page):
    page.title = "Flet Routing"

    # then we would create the routing
    def route_change(route):
        page.views.clear()
        # Now, instead of writing a bunch of if statements, we can simply iterate over the disctionary however the route is changed
        for key in _moduleList:
            if page.route == key:
                page.views.append(_moduleList[key].loader.load_module()._view_())
                # recall that the _view_() is the function in each file, and it should be the same across all pages
        page.update()

    # removing top view
    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    # call the route functions
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

    # we need to have a view here because it's the first one to show...
    page.views.append(_moduleList['/index'].loader.load_module()._view_())
    page.update()


if __name__ == '__main__':
    flet.app(target=main, port=5433)

# Rest of the pages and see how we can import them more effeciently