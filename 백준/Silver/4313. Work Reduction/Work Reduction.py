for tc in range(1, 1 + int(input())):
    N, M, L = map(int, input().split())
    dic = {}
    for _ in range(L):
        name, l = input().split(':')
        A, B = map(int, l.split(','))
        num = 0
        cur = N
        while cur > M:
            if cur // 2 >= M and (cur - cur // 2) * A > B:
                cur //= 2
                num += B
            else:
                cur -= 1
                num += A
        dic[name] = num
    print(f'Case {tc}')
    for name, num in sorted(dic.items(), key=lambda x: (x[1], x[0])):
        print(name, num)