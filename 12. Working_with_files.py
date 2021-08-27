#Original way to open the file is using the open function
myfile = open("sample.txt")
print(myfile.read())
myfile.close()

#RECOMMENDED way to open the files without closing it is using the parameter "with"
with open("sample.txt") as myfile:
    content = myfile.read()

print(content)