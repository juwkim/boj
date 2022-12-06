N = int(input())
buf = []
for _ in range(N):
    a, b = input().split()
    if a.isalpha():
        buf.append([int(b), a])
    else:
        buf.append([int(a) / 2, b])
buf.sort()
for size, color in buf:
    print(color)