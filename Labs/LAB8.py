#part 1

fibo = [1, 2]
for b in range(2, 7):
    fibo.append(fibo[b - 1] + fibo[b - 2])
print("My Fibonacci list is: " + str(fibo))

fibo2 = [1, 2, 3, 5, 8, 13, 21]
for a in range(2, len(fibo2)):
    print(fibo2[a])
    print(fibo2[a-1])
    print(fibo2[a-2])
    print("\n")
    boolean = "True"
    if fibo2[a] == (fibo2[a - 1] + fibo2[a - 2]):
        boolean = "False"
        break
if boolean == "True":
    print("It is fibo series")
else:
    print("It isn't fibo series")

#part 2
from time import sleep
print("\nWelcome to the Main Menu!\n-------------------------\n1. Count from 1 to 100\n2. Check if your list is fibo\n3. Play a lottery game")

counter=0
while(True):
    a=input("\nPlease, make your choice...")
    if(a=="1"):
        sleep(2)
        for i in range(1,101):
            print(i)
    elif(a=="2"):
        sleep(2)
        fibo3=[]
        for d in range(7):
            fibo3.append(input("Please, enter a number: "))
        boolean = "True"
        for d in range(2, len(fibo3)):
            print(fibo3[d])
            print(fibo3[d - 1])
            print(fibo3[d - 2])
            print("\n")
            if fibo3[d] == (fibo3[d - 1] + fibo3[d - 2]):
                boolean = "False"
                break
        if boolean == "True":
            print("This is fibo series")
        else:
            print("This is not fibo series")

    elif(a=="3"):
        from random import randint
        sleep(2)
        print("Welcome to our Lottery!\n" + "-----------------------\n")
        print("Let's play...\n")
        sleep(2)
        counter = 1
        num=randint(1,12)
        while(num!=12 and counter<11):
            print("Counter: " + str(counter) + "    Number: " + str(num) + "\n")
            counter=counter+1
            num = randint(1, 12)

    else:
        print("Please, choose a number from 1 to 3 only...")
        continue

    exit=input("Do you want to exit? yes/no")
    if exit=="yes":
        print("Thank you!")
        break