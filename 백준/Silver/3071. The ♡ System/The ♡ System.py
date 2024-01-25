import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

for _ in range(int(input())):
    ans = []
    n = int(input())
    while True:
        match n % 3:
            case 0:
                ans.append('0')
                n //= 3
            case 1:
                ans.append('1')
                n //= 3
            case 2:
                ans.append('-')
                n = (n + 1) // 3
        if n == 0:
            break
    print(''.join(ans[::-1]))