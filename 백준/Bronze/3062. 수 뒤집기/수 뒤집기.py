for _ in [0]*int(input()):
    s = input()
    n = str(sum(map(int, [s, s[::-1]])))
    print('YES' if n == n[::-1] else 'NO')