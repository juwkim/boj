buf = ['.***..', '*.....', '*.*...', '**....', '**.*..', '*..*..', '***...', '****..', '*.**..', '.**...']
dic = {buf[i]: i for i in range(10)}

while N:= int(input()):
    cmd = input()
    if cmd == 'S':
        ans = [[' '] * (3 * N - 1) for _ in range(3)]
        for j, num in enumerate(map(int, input())):
            s = buf[num]
            ans[0][3*j] = s[0]
            ans[0][3*j+1] = s[1]
            ans[1][3*j] = s[2]
            ans[1][3*j+1] = s[3]
            ans[2][3*j] = s[4]
            ans[2][3*j+1] = s[5]
        for line in ans:
            print(*line, sep='')
    else:
        mat = [input().split() for _ in range(3)]
        for a, b, c in zip(*mat):
            print(dic[a + b + c], end='')
        print()