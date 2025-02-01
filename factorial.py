a = int(input("Enter a non-negative integer: "))
if a < 0:
    print("Factorial can't be found for negative numbers.")
else:
    fact = 1
    for j in range(1, a + 1):
        fact *= j
    print("Factorial of", a, "is:", fact)
