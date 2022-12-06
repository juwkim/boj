s = input()
idxs = [i for i in range(len(s)) if s[i].isupper()]
n = sum(3 - (b - a - 1) % 4 for a, b in zip(idxs, idxs[1:]))
print(n)