H, N = sorted(map(int, input().split()))
l = [1]
for _ in range(N - H):
    P = [l[0]]
    for i in range(1, len(l)):
        P.append(l[i] + P[-1])
    P.append(P[-1])
    l = P
print(l[-1])