N, K = map(int, input().split())
def solve():
    buf = ['?'] * N
    cur = 0
    check = set()
    for _ in range(K):
        s, c = input().split()
        cur = (cur - int(s)) % N
        if buf[cur] != c and (c in check or buf[cur] != '?'):
            print('!')
            return
        check.add(c)
        buf[cur] = c
    print(*buf[cur:], *buf[:cur], sep='')
solve()