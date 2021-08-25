user_input = input("Type in your name: ")
message = "Hello %s! Welcome to python" %user_input
print(message)

#To print the multiple input
name = input("Type in your name: ")
surname = input("Type in your surname: ")
message_string = "Hello %s %s!" % (name, surname)
print(message_string)

def foo(name):
    return "Hi %s" % name.title()

#The input function halts the execution of the program and gets text input from the user:
name = input("Enter your name: ")

#The input function converts any input to a string, but you can convert it back to int or float:
experience_months = input("Enter your experience in months: ")
experience_years = int(experience_months) / 12

#You can format strings with (works both on Python 2 and 3):
name = "Sim"
experience_years = 1.5
print("Hi %s, you have %s years of experience." % (name, experience_years))

#You can also format strings with:
name = "Sim"
experience_years = 1.5
print("Hi {}, you have {} years of experience".format(name, experience_years))
#Output: Hi Sim, you have 1.5 years of experience.