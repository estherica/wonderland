def cubes(num):
    sum = 0
    for i in range(1,num):
        sum=sum+(i**3)
    print("The sum of the cubes is " + str(sum))
    return sum

num=int(input("Please, enter an integer... "))
print(cubes(num))
