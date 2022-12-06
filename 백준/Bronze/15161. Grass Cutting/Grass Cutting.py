k = int(input())
grass = [[1 for _ in range(10)] for _ in range(10)]

for _ in range(k):
    
    for i in range(10):
        for j in range(10):
            grass[i][j] += 1
            
    cut = [*map(int, input().split())]
    
    for a in cut[:3]:
        for i in range(10):
            grass[a-1][i] = 1

    for a in cut[3:]:
        for i in range(10):
            grass[i][a-1] = 1

for a in grass:
    print(*a)