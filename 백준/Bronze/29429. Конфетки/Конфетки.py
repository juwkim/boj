a, b = input(), input()
if len(a) < len(b) or a == b:
    print("Bad luck")
elif len(a) > len(b) or a > b:
    print(0)
else:
    for i in range(len(b)):
        if a[i] > b[i]:
            break
        if a[i] < b[i]:
            print(f"1\n{i + 1}")
            break