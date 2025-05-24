from collections import defaultdict, Counter

a, b, c = map(int, input().split())
w = input()
p = input()
cost = Counter()
last_index = defaultdict(lambda: -1)
for i, ch in enumerate(p):
    if last_index[ch] == -1:
        cost[ch] += c
    else:
        cost[ch] += min((i - last_index[ch] - 1) * a, 2 * c)
    cost[ch] += b
    last_index[ch] = i

for ch in w:
    if last_index[ch] != -1:
        cost[ch] += c
    print(cost[ch])