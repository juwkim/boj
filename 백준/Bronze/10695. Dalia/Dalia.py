for i in range(1, int(input())+1):
    n, r1, c1, r2, c2 = map(int, input().split())
    state = 'NO'
    if sorted(map(abs, [r2 - r1, c2 - c1])) == [1, 2]:
        state = 'YES'
    print(f'Case {i}:', state)