import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
received = set()
for _ in range(M):
    s, t = input().split()
    received.add(t)
ans = []
for _ in range(N - M):
    s, t = input().split()
    if t not in received and K:
        K -= 1
        received.add(t)
        ans.append(s)
print(len(ans))
print(*ans, sep='\n')