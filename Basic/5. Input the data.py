def temperature(bumm):
    if bumm > 25:
        return "Hot"
    elif 25 >= bumm >= 15:
        return "Warm"
    else:
        return "Cold"

user_input = float(input("Input the temperature:"))
print(temperature(user_input))

#Since the input data is string format, the programe need to convert it into float type.