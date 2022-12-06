N, M = map(int, input().split())
friends = [0]*(N+1)
for _ in range(M):
    A, B = map(int, input().split())
    friends[A] += 1
    friends[B] += 1
print(*friends[1:])