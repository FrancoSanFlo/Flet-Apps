global control_reference
control_reference = {}

def add_to_control_reference(key, value):
    global control_reference
    try:
        control_reference[key] = value
    except KeyError as e:
        print(e)
    finally:
        pass

def return_control_reference():
    global control_reference
    return control_reference

global url_configuration
url_configuration = {}

def add_url_control_reference(key, value):
    global url_configuration
    try:
        url_configuration[key] = value
    except KeyError as e:
        print(e)
    finally:
        pass

def return_url_control_reference():
    global url_configuration
    return url_configuration