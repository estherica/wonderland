new_list=["Estherica",32,"belleshamharoth@gmail.com","0546136456"]
print("My name is: " + new_list[0] + "\nMy age is: " + str(new_list[1]) + "\nMy E-mail is: " + new_list[2] + "\nMy phone is: " + new_list[3])

new_list2=['192.168.15.32', '193.154.31.40']
print("\nMy IPs: " + str(new_list2))
new_list2.append('194.198.60.1')
new_list2.append('170.20.10.1')
new_list2.append('172.20.10.5')
print("New IPs: " + str(new_list2))

new_list2.pop(2)
print("Delete one IP: " + str(new_list2))

print("\nThe length is: " + str(len(new_list2)))