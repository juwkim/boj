ans = 'No solution'
S, T = input(), input()

Set = set()
for i in range(1, len(S) + 1):

    q, r = divmod(len(S), i)
    if r:
        continue
    if S[:i] * q == S:
        Set.add(S[:i])

for i in range(1, len(T) + 1):

    q, r = divmod(len(T), i)
    if r:
        continue
    if T[:i] * q == T and T[:i] in Set:
        ans = T[:i]
        break
print(ans)