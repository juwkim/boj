def kmp(T, P):
    n, m = len(T), len(P)
    pi = [0] * m
    j = 0
    for i in range(1, m):
        while j > 0 and P[i] != P[j]:
            j = pi[j - 1]
        if P[i] == P[j]:
            j += 1
            pi[i] = j
    j = 0
    ans = []
    for i in range(n):
        while j > 0 and T[i] != P[j]:
            j = pi[j - 1]
        if T[i] == P[j]:
            if j == m - 1:
                ans.append(i - m + 2)
                j = pi[j]
            else:
                j += 1
    return ans

T, P = input(), input()
ans = kmp(T, P)
print(len(ans))
print(*ans)