N = int(input())
if N >= 1023:
    print(-1)
else:
    a = []
    def solve(cur):
        a.append(cur)
        for i in range(cur % 10):
            num = cur * 10 + i
            solve(num)
    for i in range(10):
        solve(i)
    a.sort()
    print(a[N])