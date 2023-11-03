import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from itertools import combinations
for tc in range(1, 1 + int(input())):
    
    s, w, p, t = g()
    suspect_list = [[] for _ in range(s + 1)]
    for _ in range(w):
        si, pi, bi, fi = g()
        suspect_list[si].append((pi, bi, fi))
    
    ans = []
    for idx, suspect in enumerate(suspect_list[1:], 1):
        l = len(suspect)
        check = [1] * l
        for i in range(l - 1):
            for j in range(i + 1, l):
                pi, bi, fi = suspect[i]
                pj, bj, fj = suspect[j]
                if pi != pj and fi >= bj and fj >= bi:
                    check[i], check[j] = 0, 0
        if all(not (suspect[i][1] <= t <= suspect[i][2])  for i in range(l) if check[i]):
            ans.append(idx)

    print(f"Data Set {tc}:")
    if ans:
        print(*ans, sep='\n')
    else:
        print("No suspect.")
    print()
