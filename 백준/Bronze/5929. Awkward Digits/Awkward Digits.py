a, b = input(), input()
for i in range(len(a)):
    s = int(a[:i] + str(1-int(a[i])) + a[i+1:], 2)
    for j in range(len(b)):
        for k in range(1, 3):
            t = int(b[:j] + str((k+int(b[j]))%3) + b[j+1:], 3)
            if s == t:
                print(s)
                break