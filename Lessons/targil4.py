# lists

new_list=[2,6.6,"estherica", 44]
print(type(new_list))
print(new_list)
print(new_list[2])

new_list2=new_list+[77]
print(new_list2)

new_list3=new_list+new_list2
print(new_list3)

new_list4=new_list3*3
print(new_list4)

my_list=[1,2,32,6.6,"esther surkis"]
print("my name: " + my_list[4])
print("my age:" + str(my_list[2]))

mylist3=list("1234567")
print(mylist3)

my_string=' A '.join(mylist3)
print(my_string)
my_string2="estherica, how're you"
print(my_string2)

my_list4=my_string.split()
print(my_list4)

my_list5=my_string2.splitlines()
print(my_list5)

my_list6=["hello", 1, 66.6, "estherica"]
print("The length is: " + str(len(my_list6)))

my_str="12345678923434868768347658"
print("The length is: " + str(len(my_str)))

new_list.append("wow")
new_list.append("kotichka")
print(new_list)
print("The new length is: " + str(len(new_list)))

new_list.insert(2,7)
print(new_list)
new_list.insert(0,"meow")
print(new_list)

new_list.pop()
print(new_list)

new_list0=["google", "facebook", "ebay", "net4u", "apple"]
print("net4u" in new_list0)