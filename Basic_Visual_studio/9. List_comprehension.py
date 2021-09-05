temps = [91, 88, 100, 77, 68, 80, 100, 81, 100, 99]

new_temps = [temp / 10 for temp in temps]
print(new_temps)

new_temps = [temp / 10 for temp in temps if temp != 100]
print(new_temps)

#Return the list with number are integer
def foo(mixed_list):
    return [item for item in mixed_list if isinstance(item , int)]

#Return the number that greater than 0
def foo(positive):
    return [n for n in positive if n > 0]

#Return the number that greater than 0 otherwise replace it by 0
temps = [91, 88, 100, 77, 68, 80, 100, 81, 100, -99]
postive_temps = [temp / 10 if temp > 0 else 0 for temp in temps]
print(postive_temps)

#Return if the data is integer therwise replace it by 0
temps = [91, 88, "get", 77, 68, 80, 100, 81, "out", -99]
def foo(temps):
    return [n if isinstance(n,int) else 0 for n in temps]
print(foo(temps))