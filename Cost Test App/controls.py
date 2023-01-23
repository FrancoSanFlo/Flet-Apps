global control_reference
control_reference = {}

def add_to_control_reference(key, value):
    global control_reference
    try:
        control_reference[key] = value
        print(control_reference)
    except KeyError as e:
        print(e)
    finally:
        pass

def return_control_reference():
    global control_reference
    return control_reference