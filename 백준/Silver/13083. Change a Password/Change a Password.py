from itertools import permutations

ans = (0, old:=int(S:=input()))
N = len(S)
for new in map(lambda p: int(''.join(p)), permutations('0123456789', N)):
    d = abs(new - old)
    ans = min(ans, (-min(d, 10**N - d), new))
print(str(ans[1]).zfill(N))