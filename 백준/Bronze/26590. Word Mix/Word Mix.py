a, b = input().split()
for i in range(min(len(a), len(b))):
    if i&1:
        print(b[i], end='')
    else:
        print(a[i], end='')