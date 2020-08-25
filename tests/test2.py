import time
from random import randint

from typing import List

print("-----------------------\n" + "Welcome to our Lottery!\n" + "-----------------------\n" + "One row costs 3 NIS.\nThe number of attempts is now limited.\n")
a=int(input("Please, make a payment!..\n"))
turns=(a//3)
print("You have {0} attempts. Good luck!".format(str(turns)))
print("Your change is... " + str(a%3) + " NIS. Enjoy your game!\n" + "-----------------------------------------")

print("Let's play...")
time.sleep(1)
total = 0

for i in range(turns):
    print("\nRound # " + str(i + 1) + "\n--------")
    time.sleep(1)
    b = int(input("Please, enter any number from 1 to 10... "))
    c = int(input("Please, enter any number from 1 to 10... "))
    d = int(input("Please, enter any number from 1 to 10... "))
    e = int(input("Please, enter any number from 1 to 10... "))
    f = int(input("Please, enter any number from 1 to 10... "))
    g = int(input("Please, enter any number from 1 to 10... "))
    num1 = randint(1, 10)
    num2 = randint(1, 10)
    num3 = randint(1, 10)
    num4 = randint(1, 10)
    num5 = randint(1, 10)
    num6 = randint(1, 10)
    print("The winning numbers are " + str(num1) + ", " + str(num2) + ", " + str(num3) + ", " + str(
        num4) + ", " + str(num5) + ", " + str(num6) + ".")


    if b == num1 and c == num2 and d == num3 and e == num4 and f==num5 and g==num6:
        total=total+1000000
    elif b==num1 and c==num2 and d==num3 and e==num4 and f==num5:
        total=total+5000
    elif b==num1 and c==num2 and d==num3 and e==num4:
        total=total+100
    elif b==num1 and c==num2 and d==num3:
        total=total+10

time.sleep(1)
print("\nCongratulations! You won " + str(total) + " NIS" + "\nThank you for joining us tonight! \nWe are looking forward seeing you again!")


