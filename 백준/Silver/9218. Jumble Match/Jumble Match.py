import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import Counter

tc = 1
while (pattern:=input()) != '.':
    ans, cnt = 0, Counter(pattern)
    l = len(pattern)
    while (s:=input()) != '0':
        n, *words = s.split()
        for word in words:
            if len(word) < l: continue
            word += ' '
            cur = Counter(word[:l])
            for i in range(l, len(word)):
                num = cnt['_']
                for k in cnt | cur:
                    a, b = cnt[k], cur[k]
                    if k == '_' or a == b: continue
                    if a > b or num < b - a:
                        break
                    num -= b - a
                else:
                    ans += 1
                    break
                cur[word[i]] += 1
                cur[word[i - l]] -= 1
    print(f"Test {tc}: {ans}")
    tc += 1