monday_tempretures = [9.1, 8.8, 7.6]

for temperature in monday_tempretures:
    print(round(temperature))

# print(round(monday_tempretures[0]))
for letter in "hello":
    print(letter)

colors = [11, 34, 98, 43, 45, 54, 54]
for number in colors:
    if number > 50:
        print(number)

new_colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]
for color in new_colors:
    if isinstance(color, int):
        print(color)

colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]
for item in colors:
    if item > 50 and isinstance(item, int):
        print(item)

student_grades = {"Mary": 9.1, "Sim": 8.8, "John": 7.5}
for grades in student_grades.items():
    print(grades)
for grades in student_grades.keys():
    print(grades)
for grades in student_grades.values():
    print(grades)

# while loop

username = ""
while username != "pypy":
    username = input("Enter username: ")
