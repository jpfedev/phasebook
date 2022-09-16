from itertools import count
from random import randint
from typing import Counter

fave_numbers_1 = []
fave_numbers_2 = []
matched = []

def matching():
    for i in range(5):
        number = randint(1,15)
        while number in fave_numbers_2:
            number = randint(1,15)
        fave_numbers_2.append(number)

    for x in range(5):
        user = int(input(f"From 1 to 15, Enter your favorite number [{x+1}]: "))
        while (user in fave_numbers_1 or user<1 or user>15):
            print("Out of range, Please enter a number again!")
            user = int(input(f"From 1 to 15, Enter your favorite number [{x+1}]: "))
        fave_numbers_1.append(user)

    print(f"\n{fave_numbers_1} are your favorite numbers")
    print(f"{fave_numbers_2} are your friends favorite numbers")

    if is_match(fave_numbers_1,fave_numbers_2):
        return True

def is_match(number1, number2):
    counter = 0
    for i in number1:
        if i in number2:
            counter += 1
            matched.append(i)
    print(f"\n{counter} has matched! and {matched} is/are the matched number(s)!") 

matching()
        
