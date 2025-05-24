import sys
from math import factorial
from collections import Counter
input = lambda: sys.stdin.readline().rstrip()

def count_perms(values):
    ret = factorial(sum(values))
    for v in values:
        ret //= factorial(v)
    return ret

for _ in range(int(input())):
    word = input()
    cnt = Counter(word)
    sorted_chars = sorted(cnt)
    rank = 0    
    for ch in word:
        for c in sorted_chars:
            if c >= ch:
                break
            cnt[c] -= 1
            rank += count_perms(cnt.values())
            cnt[c] += 1
        cnt[ch] -= 1
        if cnt[ch] == 0:
            sorted_chars.remove(ch)
    print(rank)