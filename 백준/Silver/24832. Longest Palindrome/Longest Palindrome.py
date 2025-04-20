n, m = map(int, input().split())
words = [input() for _ in range(n)]
index = {w: i for i, w in enumerate(words)}
used = bytearray(n)
prefix, suffix = [], []
center = ""
for i, w in enumerate(words):
    if used[i]: 
        continue
    rev = w[::-1]
    j = index.get(rev, -1)
    if j != -1 and j != i and not used[j]:
        used[i] = used[j] = True
        prefix.append(w)
        suffix.append(rev)
for i, w in enumerate(words):
    if not used[i] and w == w[::-1]:
        center = w
        break
result = "".join(prefix) + center + "".join(reversed(suffix))
print(len(result))
print(result)