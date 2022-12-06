g = lambda: [*map(int, input().split())]

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
while N:= int(input()):
    dic = {0: (0, 0)}
    for i in range(1, N):
        a, b = g()
        dic[i] = (dic[a][0] + dx[b], dic[a][1] + dy[b])
    x_list = sorted([p[0] for p in dic.values()])
    y_list = sorted([p[1] for p in dic.values()])
    h = x_list[-1] - x_list[0] + 1
    w = y_list[-1] - y_list[0] + 1
    print(w, h)