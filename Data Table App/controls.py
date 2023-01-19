# in this file, we create a few lines of code to map and keep
# note of the class instances. This will allow us to easily 
# access each instance when we need to change something.

global control_reference
control_reference = {}

def add_to_control_reference(key, value):
    # this function will be called before making an instance
    # of class. It takes in two arguments, a key and a value
    # which will be paired in the global dict, as a key:value pair
    global control_reference
    try:
        control_reference[key] = value
    except KeyError as e:
        print(e)
    finally:
        pass

# we cann create another function that returns the dict
def return_control_reference():
    global control_reference
    return control_reference