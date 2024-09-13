n = int(input())
ans = 1
a = [*map(int, input().split())]
while True:
    b = [sum(a[i] < a[j] for j in range(i + 1, n)) for i in range(n)]
    if a == b:
        break
    ans += 1
    a = b
print(ans)