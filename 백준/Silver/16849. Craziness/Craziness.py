for tc in range(1, int(input()) + 1):
    n = int(input())
    mat = [[*map(float, input().split())] for _ in range(n)]
    max_crazy = -1e9
    for mask in range(1, 1 << n):
        idxs = [i for i in range(n) if (mask & (1 << i))]
        s = sum(mat[i][i] for i in idxs)
        for i in range(len(idxs) - 1):
            for j in range(i + 1, len(idxs)):
                s += mat[idxs[i]][idxs[j]]
        max_crazy = max(max_crazy, s)
    print(f"Data Set {tc}:\n{max_crazy:.2f}")