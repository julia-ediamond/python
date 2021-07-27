

for number in range(10):
    print("Hello")

for numbers in range(10):
    print(numbers)

#start, stop, step
for num in range(1, 11, 2):
    print(num)

# for numbers in range(1, 101):
#    print(numbers)


# for more_numbers in range(0, 100, 5):
#    print(more_numbers)

letters = ["a", "b", "c", "d"]
result = ""

for letter in letters:
    result = result + letter  # overwrittern empty string in result by itself with a letter
    print(result)
print(result)


chilli_wishlist = ["igloo", "chicken", "donut toy", "cardboard box"]

for item in range(len(chilli_wishlist)):  # range(4) item is int  item is 0
    print(chilli_wishlist[item])  # index

for item in chilli_wishlist:
    print(item)  # string

# print(Chilli wants: item)
for item in chilli_wishlist:
    print(f"Chilli wants: {item}")

# print each item in a list from a previous exercise or example
programming_languages = ['JavaScript', 'Python', 'C#']
for language in programming_languages:
    print(language)

# nested loop

numbers = [  # outer list
    [1, 2, 3],
    [4],
    [5, 6]
]
# print(numbers[2][-1])  # printing sublist and the last element
for number in numbers:  # [1,2,3]
    for digit in number:  # 1 - next 2, next 3 at the end of the sublist it will switch to the next sublist
        print(digit)  # it goes through whole list #1
