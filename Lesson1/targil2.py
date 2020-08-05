num=4567

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