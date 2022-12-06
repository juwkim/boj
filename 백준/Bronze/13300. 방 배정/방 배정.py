from math import ceil
N, K = map(int, input().split())
room = [0]*12
for _ in range(N):
    s, y = map(int, input().split())
    room[s+2*(y-1)] += 1
print(sum(map(lambda x: ceil(x/K), room)))