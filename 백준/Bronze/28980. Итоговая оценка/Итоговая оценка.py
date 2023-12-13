S = input()
bad = ord(max(S))
q, r = divmod(sum(map(ord, S)), len(S))
if r * 2 > len(S):
    q += 1
ans = max(q, bad - 1)
print(chr(ans))