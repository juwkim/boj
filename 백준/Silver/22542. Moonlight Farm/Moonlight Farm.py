import sys
input = sys.stdin.readline

while N:=int(input()):
    dic = {}
    for _ in range(N):
        L, *l = input().split()
        P, A, B, C, D, E, F, S, M = map(int, l)
        dic[L] = (F * S * M - P) / (A + B + C + (D + E) * M)
    ans = sorted(dic, key=lambda x: (-dic[x], x))
    print(*ans, '#', sep='\n')