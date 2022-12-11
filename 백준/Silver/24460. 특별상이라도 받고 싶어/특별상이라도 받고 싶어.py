N = int(input())
if N == 1:
    print(int(input()))
else:
    Map = [[*map(int, input().split())] for _ in range(N)]
    while len(Map) != 2:
        new_Map = []
        for i in range(0, len(Map), 2):
            tmp = []
            for j in range(0, len(Map), 2):
                tmp.append(sorted(Map[i][j:j+2] + Map[i+1][j:j+2])[1])
            new_Map.append(tmp)
        Map = new_Map
    ans = sorted(Map[0] + Map[1])[1]
    print(ans)