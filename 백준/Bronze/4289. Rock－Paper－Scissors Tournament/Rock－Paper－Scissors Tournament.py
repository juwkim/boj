import sys
input = sys.stdin.readline

while (s:=input().rstrip()) != '0':
    n, k = map(int, s.split())
    win, los = [0] * n, [0] * n
    for _ in range(k*n*(n-1)//2):
        p1, m1, p2, m2 = input().split()
        p1, p2 = map(int, [p1, p2])
        if m1 == m2:
            pass
        elif m1[0] + m2[0] in 'rs sp pr':
            win[p1-1] += 1
            los[p2-1] += 1
        else:
            win[p2-1] += 1
            los[p1-1] += 1
    for a, b in zip(win, los):
        if a + b:
            r = 10000 * a // (a + b)
            if r % 10 >= 5:
                r += 10 - r % 10
            print(f'{r / 10000:.3f}')
        else:
            print('-')
    print()