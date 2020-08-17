''''''
filename = "/Users/belleshamharoth/Documents/esther.txt"
file = open(filename, "r")
my_string=file.read()
print(type((file.read())))
file.close()
my_list=(my_string.split("\n"))
print(type(my_list))
print(my_list)
''''''

new_list=[]
filename="/Users/belleshamharoth/Documents/esther.txt"
file=open(filename, "r")
new_list=list(file.read().splitlines())
print(type(new_list))
print(new_list)
print(file.read(3))
file.close()

print("\nReading specific lines")
filename="/Users/belleshamharoth/Documents/esther.txt"
file2 = open(filename)
lines_to_read = [2]
for position, line in enumerate(file2):
    if position in lines_to_read:
        print(line)

f = open("/Users/belleshamharoth/Documents/estherica.txt", "x")
f.close()