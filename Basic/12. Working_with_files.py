#Original way to open the file is using the open function
myfile = open("sample.txt")
print(myfile.read())
myfile.close()

#RECOMMENDED way to open the files without closing it is using the parameter "with"
with open("sample.txt") as myfile:
    content = myfile.read()
print(content)

#To print the first 90 letters in the text file. As method myfile.read() return the string value so we can use [:90] to abstract the first 90 letters from this
with open("sample01.txt") as myfile:
    file = myfile.read()
print(file[:90])

#Define the function that get the string "food" and the file and return the number of concurences of that "food" in the file.
def foo(character, filepath = "sample01.txt"):
    file = open(filepath)
    content = file.read()
    return content.count(character)
print(foo("food"))

#To write the first 90 letter in the file "sample01.txt" into the new file name "replace_with_text.txt"
with open("sample01.txt") as file:
    content = file.read()

with open("replace_with_text.txt", "w") as file:
    file.write(content[:90])

#To open the file and insert the new value into its. However, when to print the file, the cursor is at the end of the string as the insertation is pushing the cursor to the very end "position"in the string.
#To move the cursor to the very beggining of the file we use "file.seek(0)"
#The value "+" to help opening the file for reading and writing at the same time. So when we "a" - append the value into the file, we still can print it out without breaking the command
with open("sample.txt", "a+") as myfile:
    myfile.write("\nokra")
    myfile.seek(0)
    content = myfile.read()
print(content)

with open("replace_with_text.txt", "a+") as myfile:
    myfile.seek(0)
    content = myfile.read()
    myfile.seek(0)
    myfile.write("\n")
    myfile.write(content)
    myfile.write("\n")
    myfile.write(content)