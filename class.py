class User:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        print("A new user has been made")


pass
# 2 instances of the user class
user1 = User("Joe", "Smith", 68)
user2 = User("Blanca", "Lopez", 41)
# user3 = User()  # call it user1 is instance

# print(user1)  # it prints <__main__.User object so it works
# exercise
print(user1.first, user1.last)  # prints Joe Smith
print(user2.first, user2.last)  # Blanca Lopez


class Vehicle:
    pass


car = Vehicle()
boat = Vehicle()


class Comment:
    def __init__(self, username, text, likes):
        self.username = username
        self.text = text
        self.likes = likes


pass
comment1 = Comment("davey123", "lol you're so silly", 3)
comment2 = Comment("rosa77", "sooo cute", 0)

# davey123 lol you're so silly 3
print(comment1.username, comment1.text, comment1.likes)
print(comment2.username, comment2.text, comment2.likes)  # rosa77 sooo cute 0
