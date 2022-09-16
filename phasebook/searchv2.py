from data.search_data import USERS
import re

def search_users():

    userinput = int(input("***MAIN MENU***\n[1]Search ID\n[2]Search Name\n[3]Search Age\n[4]Search Occupation\n[0]Exit\nEnter your choice: "))
    while userinput != 0:
        if userinput == 1:
            userid = input("Enter to be ID to be search: ")
            if userid == "":
                print(USERS)
            else:
                if [user for user in USERS if user['id'] == userid]:
                    print([user for user in USERS if user['id'] == userid])
                else:
                    print("User ID not found!")
        elif userinput == 2:
            username = input("Enter to be NAME to be search: ")
            if username == "":
                print(USERS)
            else:
                if[user for user in USERS if user['name'] == username]:
                    print([user for user in USERS if user['name'] == username])
                else:
                    print("User NAME not found!")
        elif userinput == 3:
            userage = (input("Enter to be AGE to be search: "))
            if userage == "":
                print(USERS)
            else:
                user_age = int(userage)
                if [user for user in USERS if user['age'] == user_age]:
                    print([user for user in USERS if user['age'] == user_age])
                if [user for user in USERS if user['age'] == user_age+1]:
                    print([user for user in USERS if user['age'] == user_age+1])
                if [user for user in USERS if user['age'] == user_age-1]:
                    print([user for user in USERS if user['age'] == user_age-1])
                else:
                    print("User AGE not found!")
        elif userinput == 4:
            useroccupation = input("Enter to be OCCUPATION to be search: ")
            if useroccupation == "":
                print(USERS)
            else:
                if [user for user in USERS if user['occupation'] == useroccupation]:
                    print([user for user in USERS if user['occupation'] == useroccupation])
                else:
                    print("User OCCUPATION not found!")


        
        userinput = int(input("\n***MAIN MENU***\n[1]Search ID\n[2]Search Name\n[3]Search Age\n[4]Search Occupation\n[0]Exit\nEnter your choice: "))



search_users()