a, b = int(input()), int(input())
if (a - b) & 1:
    print("Error")
elif min(a, b) >= 2:
    print("Undefined")
else:
    print(max(0, (a - b) // 2))
    print(max(0, (b - a) // 2))
    print(min(a, b))