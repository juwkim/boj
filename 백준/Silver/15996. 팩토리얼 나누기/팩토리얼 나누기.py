N, A = map(int, input().split())
ans, cur = 0, A
while cur <= N:
    ans += N // cur
    cur *= A
print(ans)