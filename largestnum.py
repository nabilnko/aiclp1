def larger(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

j = int(input("Enter the first number: "))
k = int(input("Enter the second number: "))

largest = larger(j, k)
print("The largest number is:", largest)
