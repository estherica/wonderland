def ip_menu():
    print("---------\nIP System\n---------")
    while("True"):
        choice=input("1. Search for IP address from a list\n2. Add IP address to a list\n3. Delete IP address from a list\n4. Print all the IPs to the screen\n\nAre you ready to make your choice?\n")
        time.sleep(2)
        if choice=="1":
            filename = "/Users/belleshamharoth/Documents/estherica.txt"
            file = open(filename, "r")
            a=input("Please, enter your IP address...\n")
            time.sleep(2)
            for line in file:
                if a in line: print(line)
            file.close()

        elif choice=="2":
            filename = "/Users/belleshamharoth/Documents/estherica.txt"
            file = open(filename, "r+")
            b=input("Please enter your IP address...\n")
            file.write(b + "\n")
            file.close()

        elif choice=="3":
            filename = "/Users/belleshamharoth/Documents/estherica.txt"
            file = open(filename, "r+")
            c=int(input("Please, enter the IP you would like to delete...\n"))

        elif choice=="4":
            filename = "/Users/belleshamharoth/Documents/estherica.txt"
            file = open(filename, "r")
            file_contents=file.read()
            print(file_contents)

        else:
            print("Please choose a number from 1 to 4 only!\n")
            time.sleep(2)
            continue
        exit_from_menu=input("Do you want to exit? Yes/No\n")
        if exit_from_menu=="Yes" or exit_from_menu=="yes" or exit_from_menu=="y":
            print("----------------------\nThank you and goodbye!")
            break
        else:
            continue