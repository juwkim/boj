check = [0] * 9
for _ in range(int(input())):
    check[int(input().split()[0])] += 1

cur = -5
for i in range(8, -1, -1):
    cur += check[i]
    if cur >= 0:
        break
print(cur)