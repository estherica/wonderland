def calculating():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))
    sum=num1*num2
    print("Your new number is: " + str(sum))
    return sum


a=calculating()+29
print("WOW: " + str(a))

################

def calculating2(x,y):
    print("\nYour first number: " + str(x) + "\nYour second number: " + str(y))
    sum=x**y
    print("\nYour new number is: " + str(sum))
    return sum


b=int(input("Enter a number: "))
c=int(input("Enter a number: "))
esther=calculating2(b,c) + 29
print("WOW: " + str(esther))

############
def add_ip(list,ip1,ip2,ip3):
    print("List inside def: " + str(list))
    list.append(ip1)
    list.append(ip2)
    list.append(ip3)
    return list


ip_list=[]
ip_n1=input("Enter first IP: ")
ip_n2=input("Enter second IP: ")
ip_n3=input("Enter third IP: ")
ip_list=add_ip(ip_list,ip_n1,ip_n2,ip_n3)
ip_list=add_ip(ip_list,ip_n1,ip_n2,ip_n3)
print(ip_list)

###########

def add_ip(list,ip1,ip2,ip3):
    list=[]
    list.append(ip1)
    list.append(ip2)
    list.append(ip3)
    return list


ip_list=[]
ip_n1=input("Enter first IP: ")
ip_n2=input("Enter second IP: ")
ip_n3=input("Enter third IP: ")
ip_list=add_ip(ip_list,ip_n1,ip_n2,ip_n3)
ip_list=add_ip(ip_list,ip_n1,ip_n2,ip_n3)
print(ip_list)