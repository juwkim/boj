input = __import__('sys').stdin.readline
def g(): return [*map(int, input().split())]

for _ in range(int(input())):
    l, r, n, m = g()
    diff = abs(n - m)
    if diff == 0:
        ans = 'G'
    elif l >= diff and r >= diff:
        ans = 'E'
    elif l >= diff:
        ans = 'L'
    else:
        ans = 'R'
    print(ans)