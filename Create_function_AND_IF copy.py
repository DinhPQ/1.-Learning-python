def average(mylist):
    the_mean = sum(mylist) / len(mylist)
    return average

print(average([1,3,5]))

#Calculate the mean by classify the data type
student_grades = [9.1, 8.8, 10.0, 7.7, 6.8, 8.0, 10.0, 8.1, 10.0, 9.9]
detail_student_grades = {"Dinh" : 9.1,"Diep" : 8.8,"Minh Anh" : 10.0,"Dang Long" : 7.7}

def mean(number):
    if type(number) == dict:
        the_mean = sum(number.values()) / len(number)
    else:
        the_mean = sum(number) / len(number)
    return the_mean
print(mean(detail_student_grades))

def mean(number):
    #instance act as the validation
    if isinstance(number, dict):
        the_mean = sum(number.values()) / len(number)
    else:
        the_mean = sum(number) / len(number)
    return the_mean
print(mean(student_grades))