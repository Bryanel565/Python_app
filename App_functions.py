""" 
Create program app. 
Logging in/Creating account input:
- ID, Password, Name:fname, lname, DOB 
Save info into a txt file. Print console messgage (Play around w/this).
Log out/quit. Log back in using saved info from txt file.
Anyone can "Create an account" at any age. 
See if I can create a new txt file for every new user and save any input user may
want to write. 
Ex. so 1 txt file w/ID's and passwords and a txt file for each user. 

"""


from asyncio.windows_events import NULL
from cmath import log
from queue import Empty


print("Would you like to log in or create an account..?")
print("(Type 'login' or 'create account')")

class Save:

    def username_password(usern, passwrd):
        fout = open('username_passwords.txt', 'a')
        fout.write(usern)
        fout.write(" ")
        fout.write(passwrd)
        fout.write("\n")
        fout.close()

class Login_Create_Account(Save):        
    def log_In():
        print("Please Enter a Username...")
        user_name = input('--> ')
        print("Please enter a Password...")
        user_pass = input('-->')
        fout = open('username_passwords.txt', 'r')
        attempts = 0
        for credintials in fout:
            if (user_name and user_pass) in credintials:
                print(credintials)
                print("You have successfully logged in...!")
                break
            else:
                continue
        if (user_name and user_pass) not in credintials:
            print("Incorrect login... bye bye...")
        fout.close()
        
    def create_Account():
        print("Please Enter a First Name...")
        account_fname = input()
        print("Please Enter a Last Name...")
        account_lname = input()
        print("Please Enter a Date of Birth (MM/DD/YYYY)...")
        account_DOB = input()
        print(" First Name:", account_fname,"\n","Last Name:", account_lname,"\n", "DOB:",account_DOB,"\n")

        print("Please Enter a Username...")
        user_name = input('--> ')
        print("Please enter a Password...")
        user_pass = input('-->')
        print("Your Username is:", user_name, "and you Password is:", user_pass)
        print("Checking to see if my create account function works...")
        Save.username_password(user_name,user_pass)
        
    while True:
        user_input = input('--> ')
        if(user_input.lower() == 'login'):
            log_In()
            break
        elif(user_input.lower() == 'create account'):
            create_Account()
            break
        else:
            print("Invalid entry try again...")


    print("Wanted to see if this works..!")
