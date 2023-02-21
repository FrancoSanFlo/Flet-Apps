def rut_validation(rut):
    #12 345 678 - 9
    if len(rut) != 10 or rut[len(rut) - 2] != '-':
        return False
    return True