import sys
input = lambda: sys.stdin.readline().rstrip()

for tc in range(1, 1 + int(input())):
    N, M = map(int, input().split())
    D = [input() for _ in range(N)]
    idx = []
    for d in D:
        l = [[] for _ in range(26)]
        for i, c in enumerate(d):
            l[ord(c) - ord('a')].append(i)
        idx.append(l)
    ans = []
    for _ in range(M):
        L = input()
        p, score = "", -1
        for i, d in enumerate(D):
            words = [j for j in range(N) if len(d) == len(D[j]) and i != j]
            cur_score = 0
            for c in map(lambda x: ord(x) - ord('a'), L):
                if not words:
                    if cur_score > score:
                        p, score = d, cur_score
                    break
                idx_list = [idx[word][c] for word in words]
                if not idx[i][c] and all(l == [] for l in idx_list):
                    continue
                if not idx[i][c]:
                    cur_score += 1
                words = [word for word in words if idx[i][c] == idx[word][c]]
        ans.append(p)
    print(f"Case #{tc}:", *ans)