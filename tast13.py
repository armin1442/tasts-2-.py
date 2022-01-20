fibo = []
fibo.append(1)
fibo.append(1)

n = int(input())

for i in range(2,n):
    x = fibo[i-1] + fibo[i-2] 
    fibo.append(x)

print(fibo)    