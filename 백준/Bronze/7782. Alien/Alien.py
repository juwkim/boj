g = lambda: [*map(int, input().split())]

n = int(input())
b1, b2 = g()
flag = 'No'
for _ in range(n):
    lx, ly, hx, hy = g()
    if lx <= b1 <= hx and ly <= b2 <= hy:
        flag = 'Yes'
        break
print(flag)