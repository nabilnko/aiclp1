number = list(map(int, input("Input any numbers: ").split()))
odd = 0
even = 0
for a in number:
    if a % 2 == 0:
        even += a
    else:
        odd += a
print("Sum of odds :", odd)
print("Sum of evens :", even)
