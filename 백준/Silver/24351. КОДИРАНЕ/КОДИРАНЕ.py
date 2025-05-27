from functools import lru_cache

n = int(input())
l = len(s:=input())

@lru_cache(None)
def solve(i):
    if i == l:
        return 1
    ret = solve(i + 1)
    if i + 1 < l and 10 <= int(s[i:i+2]) <= 9 + n:
        ret += solve(i + 2)
    return ret
print(solve(0))