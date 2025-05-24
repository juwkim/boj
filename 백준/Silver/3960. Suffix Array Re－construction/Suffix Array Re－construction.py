import sys
input = sys.stdin.readline

def solve():
    l, s = map(int, input().split())
    result = [''] * l
    for p, suf in [input().split() for _ in range(s)]:
        p = int(p) - 1
        asterisk = -1
        for i in range(p, l):
            if suf[i - p] == '*':
                asterisk = i - p
                break
            if result[i] != '' and result[i] != suf[i - p]:
                return "IMPOSSIBLE"
            result[i] = suf[i - p]
        if asterisk != -1:
            for i in range(l - 1, asterisk + l - len(suf), -1):
                if result[i] != '' and result[i] != suf[i - l + len(suf)]:
                    return "IMPOSSIBLE"
                result[i] = suf[i - l + len(suf)]
    if all(result):
        return ''.join(result)
    return "IMPOSSIBLE"

for _ in range(int(input())):
    print(solve())