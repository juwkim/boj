import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]

N, M, q = g()
array = [g() for _ in range(N)]
for _ in range(q):
    cmd, *nums = g()
    if cmd == 0:
        i, j, k = nums
        array[i][j] = k
    else:
        i, j = nums
        array[i], array[j] = array[j], array[i]
for line in array:
    print(*line)