ans = []
for i in range(5):
    print("".join(ans) + "t" * (5 - i), flush=True)
    a = input()
    if a[0] == 'c':
        break
    print("".join(ans) + "f" + "t" * (4 - i), flush=True)
    b = input()
    if b[0] == 'c':
        break
    num1 = int(a.split()[1])
    num2 = int(b.split()[1])
    if num1 > num2:
        ans.append("t")
    else:
        ans.append("f")