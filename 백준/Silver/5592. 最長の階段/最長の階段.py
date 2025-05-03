n, k, *x = map(int, open(0).read().split())
cards = sorted(x)
if cards[0]:
    has_blank = False
    l, r = 0, 1
else:
    has_blank = True
    l, r = 1, 2
segment = []
for i in range(r, k):
    if cards[i] - cards[i - 1] > 1:
        segment.append((cards[l], cards[i - 1]))
        l = i
segment.append((cards[l], cards[k - 1]))
ans = max(b - a + 1 for a, b in segment)
if has_blank and ans < n:
    ans += 1
    for i in range(len(segment) - 1):
        if segment[i][1] + 2 == segment[i + 1][0]:
            ans = max(ans, segment[i + 1][1] - segment[i][0] + 1)
print(ans)