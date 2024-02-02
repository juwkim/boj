import sys
input = lambda: sys.stdin.readline().rstrip()
from itertools import product

vowels = {
    "110101", "101101", "010101", "111011"
}
symbols = {
    "110111", "110011", "110000", "101111",
    "101011", "101000", "010111", "010011",
    "010000", "111101", "111111", "111000"
}

def solve(idx, cnt, prev_vowel, with_vowel):
    global ans
    if idx == len(check):
        if with_vowel:
            ans += cnt
        return
    if check[idx][0] and not prev_vowel:
        solve(idx + 1, cnt * check[idx][0], True, True)
    if check[idx][1]:
        solve(idx + 1, cnt * check[idx][1], False, with_vowel)

for _ in range(int(input())):
    S = int(input())
    check = []
    for _ in range(S):
        l = input()
        idx = [i for i, x in enumerate(l) if x == '?']
        vowel, symbol = 0, 0
        if not idx:
            if l in vowels:    vowel += 1
            elif l in symbols: symbol += 1
        else:
            for p in product("01", repeat=len(idx)):
                l_ = list(l)
                for i, x in zip(idx, p): l_[i] = x
                l_ = "".join(l_)
                if l_ in vowels:    vowel += 1
                elif l_ in symbols: symbol += 1
        check.append((vowel, symbol))
    ans = 0
    solve(0, 1, False, False)
    if ans > 10000:
        ans = "CANNOT DECIPHER"
    print(ans)