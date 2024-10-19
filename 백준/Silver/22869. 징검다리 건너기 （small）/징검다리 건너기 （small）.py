def solve():
    N, K, *A = map(int, open(0).read().split())
    visited = bytearray(N)
    st = [0]
    while st:
        i = st.pop()
        for j in range(i + 1, min(N, i + K + 1)):
            if not visited[j] and (j - i) * (1 + abs(A[j] - A[i])) <= K:
                if j == N - 1:
                    return "YES"
                visited[j] = 1
                st.append(j)
    return "NO"
print(solve())