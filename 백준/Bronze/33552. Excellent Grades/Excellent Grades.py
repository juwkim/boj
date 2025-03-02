w = int(input())
n = int(input())
ans, sum_score, sum_w = "IMPOSSIBLE", 0, w
for _ in range(n):
    gi, wi = input().split()
    gi, wi = int(10 * float(gi)), int(wi)
    if gi < 58:
        break
    sum_score += gi * wi
    sum_w += wi
else:
    num = (80 * sum_w - sum_score + w - 1) // w
    if num <= 100:
        ans = max(58, num) / 10
print(ans)