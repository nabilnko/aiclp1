a = int(input("numbers of Fibonacci needed? "))
fibo = []

j, k = 0, 1
for _ in range(a):
    fibo.append(j)
    j, k = k, j + k

print("Fibonacci series:")
print(fibo)
