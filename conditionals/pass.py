# Writeaprogramthataskstheusertoentertheirusernameandpassword,andoutputsasuccessmessage if they are correct, or a failure messageif they are incorrect
username = "fleur"
password = "password123"
username_check = input("Enter a username: ")
pass_check = input("Enter a password: ")
if username_check == username and pass_check == password:
    print("correct")
else:
    print("your credentials are ivalid")
