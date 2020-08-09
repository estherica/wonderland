NAME=input("Enter your name... ")
if(NAME=="estherica"):
    print("Hello, Estherica!\n")
    AGE=int(input('Enter your age... '))
    if (AGE == 32):
        print("Wow you're 32 years old!")
    else:
        print("You are too young!\n")
else:
    print("Where is Estherica?\n")

number=int(input("Enter a number: \n"))
if(number!=6):
    print(number*2)
else:
    print(number-1)

name=input("Enter your name: \n")
age=int(input("Enter you age: \n"))
if((name=="estherica" or name=="Esther") and (age>=18)):
    print("Welcome to the club!")
else:
    print("You are not allowed to enter!")

if 4 or 5>7:
    print('good')
else:
    print('bad')

if not 9:
    pass
else:
    raise Exception('bad')

if (5+3) > 10 and 'man' in 'mana' or 100!=3 and 90<=91:
    print("fa")
elif True is False:
    pass
else:
    print('else')