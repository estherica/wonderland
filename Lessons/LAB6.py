print("Welcome to the Main Menu!\n")
a=int(input("Please choose a number... \n"))
if(a==1):
    num = int(input("Please insert a number... "))
    print("Your result is: " + str(num ** 3))
elif(a==2):
    new_list = []
    new_list.append(input("Insert your 1st IP: \n"))
    new_list.append(input("Insert your 2nd IP: \n"))
    new_list.append(input("Insert your 3rd IP: \n"))
    new_list.append(input("Insert your 4th IP: \n"))
    print("Your Ips: " + str(new_list))
elif(a==3):
    my_dict = {}
    my_dict.update({"www.google.com": input("Please, enter your 1st DNS IP address...")})
    my_dict.update({"www.google2.com": input("Please, enter your 2nd DNS IP address...")})
    my_dict.update({"www.google3.com": input("Please, enter your 3rd DNS IP address...")})
    my_dict.update({"www.google4.com": input("Please, enter your 4th DNS IP address...")})
    print("Your DNS Ips: " + str(my_dict))
elif(a==4):
    b = input("Let's play a game! Please insert a word! \n")
    c = (b[::-1])
    if (c == b):
        print("This is a Polindrom!")
    else:
        print("This is not a Polindrom!")
else:
    print("Please choose a number from 1 to 4 only!")
print("\nThank you, bye-bye!")