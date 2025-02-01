number = list(map(int, input("Input any numbers: ").split()))

smallest = number[0]
for a in number:
    if a < smallest:
        smallest = a

print("Smallest number is:", smallest)
