S, T = input(), input()
p, count = len(T), 0
for i in range(len(S) - p + 1):
    count += all(x!=y for x, y in zip(S[i:i+p], T))
print(count)