import random
import string

characters = list(string.ascii_letters + string.digits + " !@#$%^&*()")

def generate_password():
    password_length = int(input("Enter the desired length of your password : "))
    
    random.shuffle(characters)
    
    password = []
    
    for x in range(password_length):
        password.append(random.choice(characters))
    
    random.shuffle(password)
    
    password = "" .join(password)
    print(password)


option = input("Generate Password? (Yes/No) : ")


if option == "Yes":
    generate_password()
elif option == "No":
    print("Program ended")
    quit()
else:
    print("Invalid entry, please enter Yes or No")
    quit()