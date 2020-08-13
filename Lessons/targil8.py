num=int(input("Enter a number..."))
while(num!=7):
    print(num+100)
    num = int(input("Enter a number..."))
    break

counter=10
while(counter>0):
    print(counter*100)
    print("estherica")
    counter=counter-1
    break

print("Welcome to the Main Menu!\n-------------------------\n" + "1. Insert Number and ** it by 3" + "\n2. Insert 4 IPs to a list and print it" + "\n3. Insert 4 Entries to DNS Dictionary and print it" + "\n4. Check if a string is a Polindrom")
while(True==True):
    a=int(input("Please make your choice... \n"))
    if(a==1):
        num = int(input("Please insert a number... "))
        print("Your result is: " + str(num ** 3))

    elif(a==2):
        new_list = []
        new_list.append(input("Insert your 1st IP: \n"))
        new_list.append(input("Insert your 2nd IP: \n"))
        new_list.append(input("Insert your 3rd IP: \n"))
        new_list.append(input("Insert your 4th IP: \n"))
        print("Your Ips:\n---------\n" + str(new_list))

    elif(a==3):
        my_dict = {}
        my_dict.update({input("Please enter your URL: "): input("Please, enter your 1st DNS IP address...")})
        my_dict.update({input("Please enter your URL: "): input("Please, enter your 2nd DNS IP address...")})
        my_dict.update({input("Please enter your URL: "): input("Please, enter your 3rd DNS IP address...")})
        my_dict.update({input("Please enter your URL: "): input("Please, enter your 4th DNS IP address...")})
        print("Your DNS Ips:\n------------\n" + str(my_dict))

    elif(a==4):
        b = input("Let's play a game! Please enter a word! \n")
        c = (b[::-1])
        if (c == b):
            print("This is a Polindrom!")
        else:
            print("This is not a Polindrom!")
    else:
        print("Please choose a number from 1 to 4 only!")


    exit=input("Do you want to exit? y/n")
    if(exit=="y" or exit=="yes"):
        break
    else:
        continue
print("\nThank you, bye-bye!")