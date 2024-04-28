from collections import Counter

def solution(clothes):
    cnt = Counter([*zip(*clothes)][1])
    ans = 1
    for v in cnt.values(): ans *= v + 1
    return ans - 1