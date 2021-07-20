# Writeaprogramthataskstheusertoentertheiremailaddressandcheckswhetheritisvalidornot.Forthepurposeofthisexercise,youcanmaketheassumptionthatavalidemailaddresscontainsa“@”symboland a “.” symbol.
import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
#user_input = input("Enter your email: ")


def check(email):

    # pass the regular expression
    # and the string in search() method
    if(re.match(regex, email)):
        print("Valid Email")

    else:
        print("Invalid Email")


if __name__ == '__main__':

    # Enter the email
    email = "ankitrai326@gmail.com"

    # calling run function
    check(email)

    email = "my.ownsite@our-earth.org"
    check(email)

    email = "ankitrai326.com"
    check(email)
