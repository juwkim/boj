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
W = [[*map(int, input().split())] for _ in range(N)]
cache = [[0] * (1 << N) for _ in range(N)] 
visited_all, INF = (1 << N) - 1, 100000000
print(TSP(0, 1))