chilli_wishlist = ["igloo", "chicken", "donut toy", "cardboard box"]
print(len(chilli_wishlist))
print(chilli_wishlist[-2])
chilli_wishlist.append('dig mat')
print(chilli_wishlist)
chilli_wishlist.extend(['kong', 'tennis ball', 'crocodle toy'])
print(chilli_wishlist)
chilli_wishlist.insert(1, 'peanut butter')
print(chilli_wishlist)


if "tennis bal" in chilli_wishlist:
    print("Chilli would like a tennis ball.")
else:
    print("Chilli doesn't feel like pleying fetch.")

#
#  if len(chilli_wishlist > 8):
#    print("Chilli wants a lot of stuff")
if "blueberries" in chilli_wishlist:
    print("Chilli wants blueberries")
else:
    chilli_wishlist.append("blueberries")
    print(chilli_wishlist)

chilli_wishlist = [['igloo'],  # bed
                   ['donut toy', 'tennis ball', 'crocodile toy'],  # toys
                   ['chicken', 'peanut butter'],  # treats
                   ['cardboard box', 'kong', 'dig mat']  # activity basedtoys
                   ]

print(chilli_wishlist[2][1])
print(chilli_wishlist[1][2])
chilli_wishlist[1].insert(2, "star")
print(chilli_wishlist[1][2])
chilli_wishlist.append(['couch', 'fridge'])
print(chilli_wishlist)

# Exercises
foods = [
    "orange",
    "apple",
    "banana",
    "strawberry",
    "grape",
    "blueberry",
    ["carrot", "cauliflower", "pumpkin"],
    "passionfruit",
    "mango",
    "kiwifruit"
]
print(foods[0])
print(foods[2])
print(foods[-1])
print(foods[0:3])
print(foods[-3:])
print(foods[6][-1])

# Q2  Format and print the following list:
mailing_list = [
    ["Chilli", "chilli@thechihuahua.com"],
    ["Roary", "roary@moth.catchers"],
    ["Remus", "remus@kapers.dog"],
    ["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],
    ["Ivy", "noreply@goldendreamers.xyz"],
]
print(f"{mailing_list[0][0]}: {mailing_list[0][1]}")
print(f"{mailing_list[1][0]}: {mailing_list[1][1]}")
print(f"{mailing_list[2][0]}: {mailing_list[2][1]}")
print(f"{mailing_list[3][0]}: {mailing_list[3][1]}")
print(f"{mailing_list[4][0]}: {mailing_list[4][1]}")

# Q3
names = []
names.append("izzy")
names.append("archie")
names.append("boston")

print(names)
input(f"Enter a name: {names[0]}")
input(f"Enter a name: {names[1]}")
input(f"Enter a name: {names[2]}")

# Q4
a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]
d = []
e = []

numbers = []
numbers.append(a)
numbers.append(b)
numbers.append(c)
print(numbers)

new_list = a + b + c
print(new_list)
