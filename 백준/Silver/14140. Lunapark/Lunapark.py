from math import dist
def move(point, num):
    point[0] += dx[cmd[num]]
    point[1] += dy[cmd[num]]

dx = {"L": 0, "R": 0, "U": -1, "D": 1}
dy = {"L": -1, "R": 1, "U": 0, "D": 0}

L, cmd = input().split()
K = int(input())
P, Q = [0, 0], [0, 0]
for i in range(K):
    move(P, i)
ans = dist(P, Q) < 1.5
for i in range(K, int(L)-1):
    move(P, i)
    move(Q, i-K)
    ans += dist(P, Q) < 1.5
print(int(ans))