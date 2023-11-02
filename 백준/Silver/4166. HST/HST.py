import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

for _ in range(int(input())):
    N, M = g()
    dic = {}
    for _ in range(N):
        name, *l = input().split()
        taxes = []
        for num in l:
            tax = num[:-1]
            idx = tax.find('.')
            if idx == -1:
                taxes.append(int(tax) * 100)
            else:
                taxes.append(int(tax[:idx]) * 100 + int(tax[idx+1:]))
        dic[name] = taxes
    ans = 0
    for _ in range(M):
        name, cost = input().split()
        cost = int(cost[1:-3]) * 100 + int(cost[-2:])
        buf = []
        for tax in dic[name]:
            q, r = divmod(cost * tax, 10000)
            if r >= 5000:
                q += 1
            buf.append(q)
        PST, GST, HST = buf
        ans += HST - PST - GST
    print("%.2f" % (ans / 100))