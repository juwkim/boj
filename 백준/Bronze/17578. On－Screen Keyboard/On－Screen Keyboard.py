while (t:= input()) != '0 0':
    save = {}
    h, w = map(int, t.split())
    for i in range(h):
        for j,s in enumerate(input()):
            save[s] = [i, j]
    
    a = input()
    s = sum(save[a[0]]) + 1
    
    for x, y in zip(a, a[1:]):
        s += abs(save[x][0] - save[y][0]) + abs(save[x][1] - save[y][1]) + 1
    print(s)