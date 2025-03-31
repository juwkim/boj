import sys
input = sys.stdin.readline

ans = 1
P, G = 0, 0
for _ in range(int(input())):
    cmd, K = input().split()
    K = int(K)
    if cmd == 'P':
        ans += P < G <= P + K
        P += K
    else:
        ans += max(0, min(P - G, K))
        G += K
print(ans)