for t in range(1, 1 + int(input())):
    n = int(input())
    mat = [input().rfind('1') for _ in range(n)]
    ans = 0
    for i in range(n):
        j = i
        while mat[j] > i:
            j += 1
        ans += j - i
        tmp = mat[j]
        del mat[j]
        mat.insert(i, tmp)
    print(f'Case #{t}: {ans}')