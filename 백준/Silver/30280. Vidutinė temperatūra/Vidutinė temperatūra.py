N = int(input())
px = [0] * (N + 1)
for i, c in enumerate(input()):
    px[i + 1] = px[i] + (-1, 1)[c == '+']
ans, d = 0, {}
for i, num in enumerate(px):
    if num in d:
        ans = max(ans, i - d[num])
    else:
        d[num] = i
print(ans)