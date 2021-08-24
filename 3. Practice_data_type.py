student_grades = [9.1, 8.8, 10.0, 7.7, 6.8, 8.0, 10.0, 8.1, 10.0, 9.9]
detail_student_grades = {"Dinh" : 9.1,"Diep" : 8.8,"Minh Anh" : 10.0,"Dang Long" : 7.7}

#Pick the name of each student in the dictionary '{}'
Name = dict.keys(detail_student_grades)
print(Name)

##Return the index number of the list
print(student_grades.index(10.0))
print(student_grades.index(10.0, 4))

#Print the average of student grades
mysum = sum(student_grades)
counting = len(student_grades)
print(mysum/counting)

#Print the number of student grades 10.0
print(student_grades.count(10.0))

#Append the value to the list using list.append
seconds = [1.2323442655, 1.4534345567, 1.023458894]
current = 1.10001399445
seconds.append(current)

#Get the value of certain key in Dictionary
search_engines_users = {"google": 1000000000, "bing": 127000000, "duck duck go":12000000}
print(search_engines_users['google'])