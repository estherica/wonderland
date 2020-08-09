##exercise 1
print("Net4U, is the best place \n      ...in the world")

##exercise 2
from datetime import datetime
now=datetime.now()
dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
print("\nCurrent date and time:\n",dt_string)

##exercise 3
a=input("\nPlease, enter your first name... ")
b=input("Please, enter your family name... ")
print("Your name is: " + b + " " + a)

##exercise 4
filename=input("\nPlease, enter the filename... ")
print("Output: " + repr(filename.split(".")[-1]))

##exercise 5
n=input("\nPlease, enter an integer... ")
n1=int("%s" %n)
n2=int("%s%s" % (n,n))
n3=int("%s%s%s" % (n,n,n))
print(n1+n2+n3)

##exercise 6
print("\nThis program will find out whether a given number is even or odd.")
a=int(input("Please, enter a number..."))
mod = a % 2
if mod > 0:
    print("Your number in odd!")
else:
    print("Your number is even!")

##exercise 7
print("\nThis program will convert height from feet and inches to centimeters.")
a=int(input("Please enter your height in feet... "))
b=int(input("Please enter your height in inches... "))
print("Your height in centimeters is " + str((float(a*30.48)+float(b*2.54))) + "cm")

##exercise 8
n=20
d={"x":200}
print("\nEmpty a variable without destroying it\n")
print(type(n)())
print(type(d)())

##exercise 9
my_dict={0:10,1:20}
my_dict.update({2:30})
print("\nAdd a key to a dictionary\n" + str(my_dict))

##exercise 10
from collections import defaultdict, Counter
str1='net4u'
new_dict={}
for letter in str1:
    new_dict[letter]=new_dict.get(letter,0) + 1
new_dict.update({"t":2})
print("\nA dictionary from a string: " + str(new_dict))

##exercise 11
def chars_mix_up(a,b):
    new_a=b[:2] + a[2:]
    new_b=a[:2] + b[2:]
    return new_a + " " + new_b
print("Expected Result: " + str(chars_mix_up('abc', 'xyz')))

def chars(a,b):
    new_a=b[3:] + a[1:]
    new_b=b[:3] + a[:1]
    return new_a + " " + new_b
print("\nExpected Result: " + chars('nist', 'dolm'))

##exercise 12
str2="thequickbrownfoxjumpsoverthelazydog"
count = {}
for z in str2:
    if z in count:
        count[z] += 1
    else:
        count[z] = 1
for key in count:
    if count[key] > 1:
        print(key, count[key])

## exercise 13
my_list=[1, 2, 4, 5, 67, 100]
def sum_list(list, size):
   if (size ==0):
       return 0
   else:
       return list[size - 1] + sum_list(list, size - 1)
total = sum_list(my_list, len(my_list))
print("\nTotal Sum: ", total)

##exercise 14
color_list=["Red", "Green", "White", "Black", "Pink", "Yellow"]
color_list.pop(0)
color_list.pop(4)
color_list.pop(3)
print(color_list)