import sys
input = lambda: sys.stdin.readline().rstrip()

ans = 0
n, m = map(int, input().split())
p = [input() for _ in range(n)]
c = [input() for _ in range(n)]
for i in range(n):
    for j in range(m):
        a = p[i][j]
        match c[i][j]:
            case '0':
                if a != '.':
                    ans = 1
                    break
            case '1':
                if a not in '.R':
                    ans = 1
                    break
            case '2':
                if a not in '.G':
                    ans = 1
                    break
            case '3':
                if a not in '.RG':
                    ans = 1
                    break
            case '4':
                if a not in '.B':
                    ans = 1
                    break
            case '5':
                if a not in '.RB':
                    ans = 1
                    break
            case '6':
                if a not in '.GB':
                    ans = 1
                    break
    else:
        continue
    break
print(("correct", "incorrect")[ans])