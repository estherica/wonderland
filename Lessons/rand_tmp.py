from random import randint

print("Random numbers game\n")
num1=(randint(1,37))
num2=(randint(1,37))
print("1st number: " + str(num1) + "\n2nd number: " + str(num2) + "\n")

if (num1==num2):
    print("You won 100$! \n")
else:
    print("Maybe next time...")
print("\nBye-bye!")