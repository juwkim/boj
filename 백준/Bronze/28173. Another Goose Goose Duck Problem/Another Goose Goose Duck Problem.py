l, r, b, k = map(int, input().split())
ans = (l + b - 1) // b * b * k
print(ans)