import time

def main_menu():
    print("---------\nMain Menu\n---------")
    while("True"):
        choice1=input("a.IP System\nb.DNS System\n---------\nAre you ready to make your choice?..\n")
        time.sleep(1)
        if choice1=="a":
            choice = input("1. Search for IP address from a list\n2. Add IP address to a list\n3. Delete IP address from a list\n4. Print all the IPs to the screen\n\nAre you ready to make your choice?\n")
            time.sleep(1)
            if choice == "1":
                ip_search()
            elif choice=="2":
                ip_add()
            elif choice=="3":
                ip_delete()
            elif choice=="4":
                ip_print()
            else:
                print("Please choose a number from 1 to 4 only!\n")
                time.sleep(1)
                continue
            exit_from_menu = input("Do you want to exit? Yes/No\n")
            if exit_from_menu == "Yes" or exit_from_menu == "yes" or exit_from_menu == "y":
                print("----------------------\nThank you and goodbye!")
                break
            else:
                continue

        elif choice1=="b":
            print("---------\nDNS System\n---------")
            choice3 = input("1. Search the URL from a dictionary\n2. Add URL + IP address to a dictionary\n3. Delete URL from a dictionary\n4. Update the IP address of specific URL\n5. Print all the URL:IP to the screen\n\nAre you ready to make your choice?\n")
            time.sleep(1)
            if choice3 == "1":
                url_search()
            elif choice3 == "2":
                url_add()
            elif choice3 == "3":
                url_delete()
            elif choice3 == "4":
                url_update()
            elif choice3 == "5":
                url_print()
            else:
                print("Please choose a number from 1 to 5 only!\n")
                time.sleep(1)
                continue
            exit_from_menu = input("Do you want to exit? Yes/No\n")
            if exit_from_menu == "Yes" or exit_from_menu == "yes" or exit_from_menu == "y":
                print("----------------------\nThank you and goodbye!")
                break
            else:
                continue

        else:
            print("Please choose a-b only!\n")
            time.sleep(1)
            continue
        exit_from_menu = input("Do you want to exit? Yes/No\n")
        if exit_from_menu == "Yes" or exit_from_menu == "yes" or exit_from_menu == "y":
            print("----------------------\nThank you and goodbye!")
            break
        else:
            continue


def ip_search():
    filename = "/Users/belleshamharoth/Documents/estherica.txt"
    file = open(filename, "r")
    a = input("Please, enter your IP address...\n")
    time.sleep(1)
    for line in file:
        if a in line:
            print("Your IP is in the text file.")
    file.close()

def ip_add():
    filename = "/Users/belleshamharoth/Documents/estherica.txt"
    file = open(filename, "a")
    b = input("Please enter your IP address...\n")
    file.write("\n" + b)
    file.close()
    print("Please, see your updated text file.")

def ip_delete():
    filename = "/Users/belleshamharoth/Documents/estherica.txt"
    a_file = open(filename, "r")

    lines = a_file.readlines()
    a_file.close()

    new_file = open(filename, "w")
    c = input("Please, enter the IP you would like to delete...\n")
    for line in lines:
        if line.strip("\n") != c:
            new_file.write(line)
    new_file.close()

    print("Please, see your updated file.")

def ip_print():
    filename = "/Users/belleshamharoth/Documents/estherica.txt"
    file = open(filename, "r")
    file_contents = file.read()
    print(file_contents)

def url_search():
    while ("True"):
        my_dict = {"www.google.com": "1.1.1.1", "www.facebook.com": "2.2.2.2", "www.instagram.com": "3.3.3.3",
                   "www.twitter.com": "4.4.4.4"}
        search_string = input("Please enter the URL you want to find... ")
        for i in my_dict:
            if i in search_string:
                print(i)
        break

def url_add():
    my_dict = {"www.google.com": "1.1.1.1", "www.facebook.com": "2.2.2.2", "www.instagram.com": "3.3.3.3",
               "www.twitter.com": "4.4.4.4"}
    my_dict.update({input("Please enter your URL: "): input("Please, enter your DNS IP address...")})
    print("Your DNS Ips:\n------------\n" + str(my_dict))

def url_delete():
    my_dict = {"www.google.com": "1.1.1.1", "www.facebook.com": "2.2.2.2", "www.instagram.com": "3.3.3.3",
               "www.twitter.com": "4.4.4.4"}
    del my_dict[input("Please, enter the URL you would like to delete...")]
    print(my_dict)

def url_update():
    my_dict = {"www.google.com": "1.1.1.1", "www.facebook.com": "2.2.2.2", "www.instagram.com": "3.3.3.3",
               "www.twitter.com": "4.4.4.4"}
    my_dict.update(
        {input("Please, enter the URL you would like to update..."): input("Please, enter the new DNS IP...")})
    print(my_dict)

def url_print():
    my_dict = {"www.google.com": "1.1.1.1", "www.facebook.com": "2.2.2.2", "www.instagram.com": "3.3.3.3",
               "www.twitter.com": "4.4.4.4"}
    print(my_dict)
