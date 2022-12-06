import sys
input = sys.stdin.readline

cnt = int(input())
for step in range(1, 1 + cnt):
    n, m, T = map(int, input().split())
    moneys = [0] * n
    for _ in range(m):
        i, t, d = input().split()
        if 0 <= T - int(t) < 1000:
            moneys[int(i) - 1] += float(d)
    votes = [input().rstrip() for _ in range(n)]
    pro, con = 0, 0
    for vote, money in zip(votes, moneys):
        if vote == 'Y':
            pro += 1
        else:
            con += 10000 / (10000 + money)
    print(f'Data Set {step}:\n{pro:.2f} {con:.2f}')
    if i != cnt:
        print()