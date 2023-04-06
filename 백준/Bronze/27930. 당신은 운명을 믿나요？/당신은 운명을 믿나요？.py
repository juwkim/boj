a, b = "YONSEI", "KOREA"
i, j = 0, 0

for c in input():
    if c == a[i]:
        i += 1
        if i == 6:
            print(a)
            break
    if c == b[j]:
        j += 1
        if j == 5:
            print(b)
            break