print("Welcome to our Lottery!\n" + "-----------------------\n" + "One roulette spin costs 3 NIS.\nThe number of attempts is now limited.\n")
a=int(input("Please, make a payment!..\n"))
turns=(a//3)
print("You have {0} attempts. Good luck!".format(str(turns)))
print("Your change is... " + str(a%3) + " NIS. Enjoy your game!\n" + "-----------------------------------------")

from random import randint
from time import sleep
print("Let's play...\n")
sleep(2)
total=0

for i in range(turns):
    print("Round # " + str(i+1) + "\n--------")
    sleep(2)
    num1=(randint(1,6))
    num2=(randint(1,6))
    print("1st number: " + str(num1) + "\n2nd number: " + str(num2) + "\n")

    if num1==num2:
        total=total+100
    elif num1==6==num2:
        total=total+1000
    elif num2==2!=num1:
        total=total+40
    elif num1==1!=num2:
        total=total+20

sleep(2)
print("Congratulations! You won " + str(total) + " NIS" + "\nThank you for joining us tonight! \nWe are looking forward seeing you again!")