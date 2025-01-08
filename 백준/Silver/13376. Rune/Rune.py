import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N, *W = input().split()
    rune = []
    for s in W:
        cnt, suc = 0, 0
        for c in s:
            if c in "aeiou":
                if suc == 0:
                    cnt += 1
                suc += 1
            else:
                suc = 0
        rune.append((-cnt, s))
    rune.sort()
    print(" ".join(w for _, w in rune))