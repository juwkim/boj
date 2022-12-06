import sys
input = sys.stdin.readline

def is_visited(city, visited):
    return visited & (1 << city)

def possible_to_visit(city, current):
    return W[current][city]

def TSP(current, visited):
    if visited == visited_all:
        return W[current][0] or INF
    
    if cache[current][visited]:
        return cache[current][visited]
    
    ans = INF
    for city in range(N):
        if is_visited(city, visited):
            continue
        if possible_to_visit(city, current):
            ans = min(ans, TSP(city, visited | (1 << city)) + W[current][city])
    
    cache[current][visited] = ans
    return ans

N = int(input())
pos = [[*map(int, input().split())] for _ in range(N)]
W = [[0] * N for _ in range(N)]
for i in range(N-1):
    for j in range(i+1, N):
        dist = pow(pow(pos[i][0] - pos[j][0], 2) + pow(pos[i][1] - pos[j][1], 2), 0.5)
        W[i][j] = dist
        W[j][i] = dist
cache = [[0] * (1 << N) for _ in range(N)] 
visited_all, INF = (1 << N) - 1, 100000000
print(TSP(0, 1))