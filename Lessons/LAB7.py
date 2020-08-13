print("Welcome to our Lottery!\n" + "-----------------------\n" + "One roulette spin costs 3 NIS.\nThe number of attempts is now limited.\n")
a=int(input("Please, make a payment!..\n"))
print("You have {0} attempts. Good luck!".format(str(a//3)))
print("Your change is... " + str(a-(a//3*3)) + " NIS. Enjoy your game!\n" + "-----------------------------------------")

from random import randint
print("Let's play...\n")
import time
time.sleep(2)
num1=(randint(1,6))
num2=(randint(1,6))
print("1st number: " + str(num1) + "\n2nd number: " + str(num2) + "\n")

if num1==num2:
    print("Congratulations! You won 100 NIS.")
elif num1==num2==6:
    print("Congratulations! You won 1000 NIS.")
elif num2==2!=num1:
    print("Congratulations! You won 40 NIS.")
elif num1==1!=num2:
    print("Congratulations! You won 20 NIS.")
else:
    print("Well, maybe next time...")

time.sleep(2)
print("\nThank you for joining us tonight! We are looking forward seeing you again!")
