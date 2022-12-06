t = int(input())
n = -1
for _ in range(t):
    if n == -1:
        n = int(input())
    else:
        i = int(input())
        if i % n == 0:
            print(i)
            n = -1