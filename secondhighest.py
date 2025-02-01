num = list(map(int, input("Input numbers: ").split()))

se_num = list(set(num))

if len(se_num) < 2:
    print("Not enough numberrs")
else:
    se_num.sort()
    s_high = se_num[-2]
    print("The second highest number is:", s_high)
