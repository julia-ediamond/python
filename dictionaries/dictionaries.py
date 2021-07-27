#students = ['Angela', 'Jen', 'Bel']

# creating a dictionary
students_dict = {"Angela": 1, "Jen": 2, "Bel": 3}
print(students_dict)
# print(students_dict["Angela"])
# add value
students_dict["Asli"] = 4
print(students_dict)
# result {'Angela': 1, 'Jen': 2, 'Bel': 3, 'Asli': 4}
students_dict["Jen"] = 10
print(students_dict)
#{'Angela': 1, 'Jen': 10, 'Bel': 3, 'Asli': 4}

# delete value
del students_dict["Asli"]
print(students_dict)
#{'Angela': 1, 'Jen': 10, 'Bel': 3}

print(students_dict.keys())
#dict_keys(['Angela', 'Jen', 'Bel'])

print(students_dict.items())
#dict_items([('Angela', 1), ('Jen', 10), ('Bel', 3)])

# Iteration
for key in students_dict:
    print(key, students_dict[key])
# Angela
# Jen
# Bel
# Angela 1
# Jen 10
# Bel 3


for key, value in students_dict.items():
    print(key, value)

students_dict = {"Angela": 1, "Jen": 2, "Bel": 3}
print(students_dict.get("Bel"))
# 3
