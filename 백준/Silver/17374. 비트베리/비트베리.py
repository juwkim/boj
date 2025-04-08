import sys
input = sys.stdin.readline

for _ in range(int(input())):
    P, Q, A, B, C, D = map(int, input().split())
    q, coin = divmod(Q // C * D, B)
    bit = P + q * A
    ans = min(bit, coin)
    if bit > coin:
        q, r = divmod(bit - coin, A + B)
        ans = max(ans, min(bit - q * A, coin + q * B))
        ans = max(ans, min(bit - (q + 1) * A, coin + (q + 1) * B))
    else:
        q, r = divmod(coin - bit, A + B)
        ans = max(ans, min(bit + q * A, coin - q * B))
        ans = max(ans, min(bit + (q + 1) * A, coin - (q + 1) * B))
    print(ans)