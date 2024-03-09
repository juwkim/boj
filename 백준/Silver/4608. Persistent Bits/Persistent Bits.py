while True:
    t = input()
    if t == '0':
        break
    A, B, C, S = map(int, t.split())
    l = set()
    num = S
    while num not in l:
        l.add(num)
        num = (A * num + B) % C
    ans = [[0, 0] for _ in range(16)]
    for num in l:
        for i in range(15, -1, -1):
            if num & (1 << i):
                ans[15 - i][1] = 1
            else:
                ans[15 - i][0] = 1
    for i in range(16):
        if ans[i] == [1, 1]:
            print('?', end='')
        elif ans[i] == [1, 0]:
            print('0', end='')
        else:
            print('1', end='')
    print()