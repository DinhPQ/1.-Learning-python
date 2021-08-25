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

