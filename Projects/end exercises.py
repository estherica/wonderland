#1
print("Twinkle, twinkle, little star,\n       How I wonder what you are!\n             Up above the world so high,\n             Like a diamond in the sky. \nTwinkle, twinkle, little star,\n       How I wonder what you are")

#2
color_list = ["Red","Green","White" ,"Black"]
color_list.pop(2)
color_list.pop(1)
print(color_list)

#3
num=int(input("Please, enter an integer... "))
total=num+((num*10)+num)+((num*100)+(num*10)+num)
print("Total number is: " + str(total))

#4
from datetime import date
a=int(input("Please, enter the first day... "))
b=int(input("Please, enter the first month... "))
c=int(input("Please, enter the first year... "))
d=int(input("Please, enter the second day..."))
e=int(input("Please, enter the second month..."))
f=int(input("Please, enter the second year..."))
date1=date(c, b, a)
date2=date(f, e, d)
delta = date2 - date1
print("\nThe number of days between two dates is " + str(delta.days) + " days.")

#5
def three_times(a, b, c):
    a=int(input("\nPlease enter the first number... "))
    b=int(input("Please, enter the second number..."))
    c=int(input("Please, enter the third number..."))
    sum=a+b+c
    if(a==b==c):
        sum=sum*3
    return sum

print(three_times(a,b,c))

#6

def sum_20():
    a=int(input("Please, enter the first number..."))
    b=int(input("Please, enter the second number..."))
    sum=a+b
    if sum>15 and sum<20:
        sum=20
    return sum

print("The sum is " + str(sum_20()))

#7
a=input("\nPlease, enter your name... ")
b=input("Please, enter your age... ")
c=input("Please, enter your address...")
print("Your name is " + a + "\nYour age is " + str(b) + " years old.\nYour address is " + c)

#8
x=int(input("Please, enter x... "))
y=int(input("Please, enter y... "))
print("\nThe answer is " + str((x+y)*(x+y)))

#9
print("\nThis program will convert height from feet and inches to centimeters.")
a=int(input("Please enter your height in feet... "))
b=int(input("Please enter your height in inches... "))
print("Your height in centimeters is " + str((float(a*30.48)+float(b*2.54))) + "cm")

#10
string='esthericasurkis'
print()
print(list(string))
print()

#11
def cubes(num):
    sum = 0
    for i in range(1,num):
        sum=sum+(i**3)
    print("The sum of the cubes is " + str(sum))
    return sum

num=int(input("Please, enter an integer... "))
print(cubes(num))