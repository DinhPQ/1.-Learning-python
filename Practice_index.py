student_grades = [9.1, 8.8, 10.0, 7.7, 6.8, 8.0, 10.0, 8.1, 10.0, 9.9]
detail_student_grades = {"Dinh" : 9.1,"Diep" : 8.8,"Minh Anh" : 10.0,"Dang Long" : 7.7}

#Pick the grades of each student in the dictionary '{}'
Value = dict.values(detail_student_grades)
print(Value)

#Print the proportion of the list [1:4] - that will print the value from the first value to the THIRD value.
print(student_grades[1:4])

#Using the short-cut will give the same result - this sample is printing the first letter to the third letter
print(student_grades[0:4])
print(student_grades[:4])

#Using the short-cut will give the same result - this sample is printing the sixth letter to the last letter
print(student_grades[6:10])
print(student_grades[6:])

#To print with the negative indexies - This sample is printing the second from the left
print(student_grades[-2])

##Pick the index with mixed data type
mix_index = ('string', 1, 2.3, 4)
print(mix_index[0][2])

print('abcdef'[2])

##First three items of a list:
#days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
#days[:3]
#Output:['Mon', 'Tue', 'Wed'] 

##Last three items of a list:
#days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
#days[-3:]
#Output: ['Fri', 'Sat', 'Sun']

##Everything but the last:
#days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
#days[:-1] 
#Output: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'] 

##Everything but the last two:
#days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
#days[:-2] 
#Output: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'] 

##A single in a dictionary can be accessed using its key:
#phone_numbers = {"John Smith":"+37682929928","Marry Simpsons":"+423998200919"}
#phone_numbers["Marry Simpsons"]
#Output: '+423998200919'