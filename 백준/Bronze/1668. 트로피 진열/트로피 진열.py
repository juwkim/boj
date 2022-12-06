t = [int(input()) for _ in range(int(input()))]
L, R = 0, 0
max_L, max_R = 0, 0
for x in t:
    L += (x > max_L)
    max_L = max(x, max_L)
for x in t[::-1]:
    R += (x > max_R)
    max_R = max(x, max_R)
print(L, R)