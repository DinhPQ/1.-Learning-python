student_grades = [9.1, 8.8, 10.0, 7.7, 6.8, 8.0, 10.0, 8.1, 10.0, 9.9]
for grades in student_grades:
    print(round(grades))

for letter in 'Hello':
    print(letter.lower())

colors = [11, 34, 98, 43, 45, 54, 54]
for n in colors:
    if n > 50:
        print(n)

#Print if value of Color_codes is integer
color_codes = [11, 34, 98, 43, 45, 54, 54]
for n in color_codes:
    if isinstance(n,int):
        print(n)

#Print if value of color is greater than 50 and is integer
colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]
for n in colors:
    if n > 50 and isinstance(n,int):
        print(n)

#The loop that call the function and add the value to each of value in the list by loop.
def celsius_to_kelvin(cels):
    return cels + 100
monday_temperatures = [9.1, 8.8, -270.15]
for temperature in monday_temperatures:
    print(celsius_to_kelvin(temperature))

#Loop in dictionary data_type
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
for pair in phone_numbers.items():
    print("{} has as phone number {}".format(pair[0], pair[1]))

#Same results as previous
phone_numbers = {"John Smith": "+0963", "Marry Simpons": "+0962"}
for key, value in phone_numbers.items():
    print("{} has as phone number {}".format(key, value))

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
for n in phone_numbers.items():
    print("%s : %s" %(key, value))