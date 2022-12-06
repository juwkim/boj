n = int(input())
total, j = 0, 0
for i in range(1, int(n**.5)+1):
    for j in range(i, n+1):
        if i * j <= n:
            total += 1
        else:
            break
print(total)