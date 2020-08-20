##For loops

for x in range(1,11):
    print(x)
    print("wow\n")

list_esther=["banana","apple","mango"]
for x in range(len(list_esther)):
    print(list_esther[x])

for x in range (1,11,2):
    print(x)
    print("wow\n")

print("Now we will get all the details about your class!")
for i in range(1,4):
    name=input("\nEnter your name: ")
    age=int(input("Enter your age: "))
    phone=input("Enter your phone: ")
    print("Printing student number \n" + str(i) + " Details...\n")
    import time
    time.sleep(3)
    print("\nFull name: " + name + "\nAge: " + str(age) + "\nPhone: " + phone + "\n")

