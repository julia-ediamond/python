name = "Ana"  # global variable


def ask_name():
    name = input("What is your name?")  # local var
    return name


asli_name = ask_name()  # call it
print(asli_name)
