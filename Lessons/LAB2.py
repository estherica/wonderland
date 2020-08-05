print("Welcome and enjoy your online-shopping!")

num=int(input("Please weigh your cucumbers: "))
print("Cucumbers: " + str((num*2)*1.17) + " NIS")

num2=int(input("Please weigh your tomatos: "))
print("Tomatos: " + str((num2*3)*1.17) + " NIS")

num3=int(input("Please enter the number of bottles: "))
print("Cola: " + str((num3*5)*1.17) + " NIS")

num4=int(input("Please weigh your chicken: "))
print("Chicken: " + str((num4*20)*1.17) + " NIS")

print("\nTotal: " + str(((num*2)*1.17) + ((num2*3)*1.17) + ((num3*5)*1.17) + ((num4*20)*1.17)) + " NIS")
a=((num*2)*1.17) + ((num2*3)*1.17) + ((num3*5)*1.17) + ((num4*20)*1.17)
i=round(float(a))
print("To payment: "+str(i))
print("Without tax: " +str((num*2) + (num2*3) + (num3*5) + (num4*20)))