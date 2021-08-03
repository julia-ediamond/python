fruits = ["banana", "apple", "cherry"]
print(fruits[-1])
fruits.append("pineapple")
print(fruits)
fruits.pop(0)
print(fruits)

digits = [1, 2, 3]
decimal = [1, 2, 3]
nested = [[1, 2, 3], ["hello"]]
for item in fruits:
    print(item)

for item in nested:
    print(item)
    for i in item:
        print(i)
people = [
    ["Alice", 25, "pink"],
    ["Bob", 33, "purple"],
    ["Anne", 18, "red"],
]

vaccination = []

# Pseudo code
# go through the list

# check the age

# if age 20 or older add this prson to vaccination list


for person in people:
    # if person[1] >= 20:
    # first iteration ["Alice", 25, "pink"] person[0] - 0 because e need name to be added
    # vaccination.append(person[0])

    print(vaccination)
