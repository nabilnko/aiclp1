total = 0
for a in range(50, 101):
    if a % 3 == 0 and a % 5 != 0:
        total += a

print("Sum of numbers divisible by 3 and not divisible by 5 between 50 and 100:", total)
