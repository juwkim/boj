while (s := input()) != '0 0':
    r, c = map(int, s.split())
    cnt = 0
    margin = ['.' * (c + 2)]
    a = ['.' + input() + '.' for _ in range(r)]
    a = margin + a + margin
    for i in range(1, 1+r):
        for j in range(1, 1+c):
            if a[i][j-1:j+2] == '.#.' and a[i-1][j-1:j+2] == '...' and a[i+1][j-1:j+2] == '...':
                cnt += 1
    print(cnt)