mul = [1, 5, 10, 20, 50, 100]
ans, cnt = 0, 0
for a, b in zip(mul, map(int, input().split())):
    cur = a * b
    if cur > ans * cnt or (cur == ans * cnt and b < cnt):
        ans = a
        cnt = b
print(ans)