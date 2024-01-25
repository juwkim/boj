import sys
input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    dic = {}
    for l in input().split(','):
        a, b = l.split(':')
        dic[a] = int(b)
    ans = min(max(dic[p] for p in l.split('&')) for l in input().split('|'))
    print(ans)