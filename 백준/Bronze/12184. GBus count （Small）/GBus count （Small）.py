import sys
input = sys.stdin.readline

g = lambda: [*map(int, input().split())]
for cnt in range(1, 1 + int(input())):
    N = int(input())
    bus = g()
    city = [0] * 501
    for i in range(0, 2*N, 2):
        for j in range(bus[i], bus[i+1]+1):
            city[j] += 1
    P = int(input())
    buf = [city[int(input())] for _ in range(P)]
    print(f'Case #{cnt}:', *buf)
    input()