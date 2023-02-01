A, B = map(int, input().split())

ans = 0
while A != B:
    A, B = max(A, B) - min(A, B), min(A, B)
    ans += 1
print(ans)