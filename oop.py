name = "asli"
age = 26
print(type(name))  # class str
print(type(age))  # class int
print(name.upper())
print(dir(name))  # prints all the built in functions
# build your own class

# create a class DOg


class Dog:
    # init name of the method - special tyope, program knows what to do with it. to initialize the object
    # self will always be the first parameter,
    # age, breed, size, colour are attributes
    #methods /actions - talk, walk, play
    def __init__(self, age, breed):
        #age = 3
        # Jetts breed = pug
        # init can't return
        self.age = age
        self.breed = breed

    def talk(self):
        return "Bark"


Jett = Dog(3, "pug")
Chilli = Dog(4, "chi")
Jett.talk()
Chilli.talk()
