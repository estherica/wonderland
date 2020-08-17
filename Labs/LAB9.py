from time import sleep

def main_menu():
    print("\nWelcome to the Main Menu!\n-------------------------\n1. Dogs' details\n2. Friends' list\n3. N Azzeret")

    counter=0
    while(True):
        a=input("\nPlease, make your choice...\n")
        if(a=="1"):
            dogs()

        elif(a=="2"):
            friends()

        elif(a=="3"):
            azzeret()

        else:
            print("Please, choose a number from 1 to 3 only...\n")
            continue

        exit = input("Do you want to exit? yes/no\n")
        if exit == "yes":
            print("Thank you!")
            break


def dogs():
    a=input("Please enter your dog's name: ")
    b=int(input("Please enter your dog's age: "))
    print("Your dog's name is " + a + ", he is " + str(b) + " years old that is equal to " + str (b*7) + " human years.")

def friends():
    list=[]
    for i in range(5):
        list.append(input("Please, enter friend's name... "))
    name=input("Please add new name... ")
    if(name) in list:
        print("Wow you found him!")
    else:
        print("Maybe next time...")


def azzeret():
    num=int(input("Please, enter a number... "))
    sum=1
    for a in range(1,num+1):
        sum=sum*a
    print(str(num) + " Azzeret: " + str(sum) + "\n")


main_menu()