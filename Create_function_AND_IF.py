def foo(password):
    if len(password) < 8:
        print('False')
    else:
        print('True')
    return foo
print(foo('wrongpassword'))

def temperature(bumm):
    if bumm > 25:
        print('Hot')
    elif 25 >= bumm >= 15:
        print('Warm')
    else:
        print('Cold')
    return temperature
print(temperature(10))