N, M = map(int, input().split())
one = N
two = N // 2
three = (N + 1) // 2
four = N // 3 + (N % 3 != 0)

ans = 1
ans += one <= M
ans += N >= 2 and two <= M
ans += N >= 2 and three <= M
ans += N >= 3 and four <= M
ans += N >= 3 and one + four <= M
ans += N >= 3 and two + four <= M
ans += N >= 3 and three + four <= M
print(ans)