values = ["a", "b", "c"]
index = 0
for value in values:
    print(index, value)
# the output is
# 0 a
# 0 b
# 0 c
# index stays at 0 on every iteration because there’s no code to update its value at the end of the loop

for value in values:

    index += 1  # create a variable for index and update it on each iteration by one. Integer that keeps track of how far into the list you are
    print(index, value)
# 1 a
# 2 b
# 3 c


# Another common way to approach this problem is to use range() combined with len()
# to create an index automatically.
# his way, you don’t need to remember to update the index:

for index in range(len(values)):
    # len(values) returns the length of values - 3
    # range () creates an iterator running from the default  starting value of 0 until it reaches len(values) -1
    value = values[index]
    print(index, value)
# 0 a
# 1 b
# 2 c

# use enumerate() in a loop in the same way that you use the original iterable object.

for count, value in enumerate(values):
    print(count, value)

# 0 a
# 1 b
# 2 c
# When you use enumerate(), the function gives you back two loop variables:

# The count of the current iteration
# The value of the item at the current iteration


# can use the start argument for enumerate() to change the starting count:
for count, value in enumerate(values, start=1):
    print(count, value)
# 1 a
# 2 b
# 3 c

fruits = ["Apple", "Berry", "Cherry"]
for i, j in enumerate(fruits):
    print(i, j)
# 0 Apple
# 1 Berry
# 2 Cherry

fruit = "Apple"
for index, letter in enumerate(fruit):
    print(index, letter)
# 0 A
# 1 p
# 2 p
# 3 l
# 4 e

fruit = "Apple"
for index, letter in enumerate(fruit, start=2):
    print(index, letter)
# 2 A
# 3 p
# 4 p
# 5 l
# 6 e
