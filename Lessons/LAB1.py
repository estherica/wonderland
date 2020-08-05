num=int(input("Enter a number with 4 digits: "))

a=num//1000
print("Alafim: " + str(a))

b=num//100
print("Meot: " + str(b-a*10))

print("Meot: " + str((num%1000)//100))

c=num//10
print("Asarot: " + str(c-b*10))

print("Asarot: " + str((num%100)//10))

d=num
print("Ahadot: " + str(d-c*10))

print("Ahadot: " + str(num%10))

num=int(input("Enter a number with 4 digits: "))
print("Alafim: " + str(num//1000) + "\nMeot: " + str((num%1000)//100) + "\nAsarot: " + str((num%100)//10) + "\nAhadot: " + str(num%10))