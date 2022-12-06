N, M = map(int, input().split())
time = [[0, 0] for _ in range(N)]

for _ in range(M):
    C, keyword, HH, MM = input().split()
    C, HH, MM = map(int, [C, HH, MM])
    
    if keyword == 'START':
        time[C-1][1] = HH * 60 + MM
    else:
        time[C-1][0] += HH * 60 + MM - time[C-1][1]
    
for i in range(N):
    print(*divmod(time[i][0], 60))