def rut_validation(rut):
    if '-' not in rut:
        if len(rut) == 9:
            return True, '{0}.{1}.{2}-{3}'.format(rut[:2], rut[2:5], rut[5:8], rut[-1])
        elif len(rut) == 8:
           return True, '{0}.{1}.{2}-{3}'.format(rut[:1], rut[1:4], rut[4:7], rut[-1])
    else:
        if len(rut) == 10:
            return True, '{0}.{1}.{2}'.format(rut[:2], rut[2:5], rut[5:])
        elif len(rut) == 9:
            return True, '{0}.{1}.{2}'.format(rut[:1], rut[1:4], rut[4:])
    
    return False, rut


def phone_validation(phone):
    if len(phone) < 8:
        return False, phone
    
    return True, f'9{phone}'