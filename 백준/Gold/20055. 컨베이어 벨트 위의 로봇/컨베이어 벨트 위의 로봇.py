from collections import deque

N, K, *A = map(int, open(0).read().split())
ans, zero, s = 0, 0, 0
belt = deque([0] * N)
while zero < K:
    ans += 1
    s = (s - 1) % (2 * N)
    belt.rotate()
    if A[s]:
        belt[0] = 1
        A[s] -= 1
        zero += A[s] == 0
    else:
        belt[0] = 0
    for i in range(N - 1, 0, -1):
        if not belt[i]:
            continue
        if i == N - 1:
            belt[i] = 0
        elif not belt[i + 1] and A[idx := ((s + i + 1) % (2 * N))]:
            belt[i], belt[i + 1] = 0, 1
            A[idx] -= 1
            zero += A[idx] == 0
print(ans)