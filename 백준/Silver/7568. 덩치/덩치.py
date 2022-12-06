N = int(input())
bodys = [tuple(map(int, input().split())) for i in [0] * N]
ranks = [1] * N
for i in range(N - 1):
    for j in range(i + 1, N):
        if bodys[i][0] > bodys[j][0] and bodys[i][1] > bodys[j][1]:
            ranks[j] += 1
        elif bodys[i][0] < bodys[j][0] and bodys[i][1] < bodys[j][1]:
            ranks[i] += 1
            
for rank in ranks:
    print(rank)