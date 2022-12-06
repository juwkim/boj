T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    kids = [candy // K for candy in map(int, input().split())]
    print(sum(kids))