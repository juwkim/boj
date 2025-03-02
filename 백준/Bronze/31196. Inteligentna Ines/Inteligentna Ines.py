n = len(a := input())
r = int(n**.5)
while r > 1 and n % r:
    r -= 1
for i in range(r):
    print(a[i::r], end="")