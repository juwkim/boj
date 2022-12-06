import sys
input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: [*map(int, input().split())]

while (s:= MIS()) != [0, 0, 0]:
    N, C, K = s
    buf = [0] * K
    for _ in range(N):
        for num in MIS():
            buf[num-1] += 1
    Min = min(buf)
    buf = [i+1 for i in range(K) if buf[i] == Min]
    print(*buf)