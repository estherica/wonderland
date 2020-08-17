fibo = [1, 2]
for i in range(2,7):
    fibo.append(fibo[i-1]+fibo[i-2])
print(fibo)
