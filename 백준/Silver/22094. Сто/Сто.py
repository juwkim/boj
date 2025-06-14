import sys
input = sys.stdin.readline

for _ in range(int(input())):
    k, x = input().split()
    k = int(k)
    ans = -1
    if len(x) - k == 1:
        if '0' in x:
            ans = 0
    elif len(x) - k > 2 and x.rfind('0', 0, x.rfind('0')) > len(x) - k - 3:
        ans = x[:len(x)-k-2] + '00'
    print(ans)