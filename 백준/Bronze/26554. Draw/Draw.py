import sys
input = sys.stdin.readline

for _ in range(int(input())):
    name, *nums, t = input().split()
    match name:
        case "rectangle":
            r, c = map(int, nums)
            a = [['#' for _ in range(c)] for _ in range(r)]
            if t == 'n':
                for i in range(1, r - 1):
                    for j in range(1, c - 1):
                        a[i][j] = ' '
        case "right":
            n = int(nums[1])
            a = [['#' for _ in range(n)] for _ in range(n)]
            for i in range(n - 1):
                for j in range(n - i - 1):
                    a[i][j] = ' '
            if t == 'n':
                for i in range(2, n - 1):
                    for j in range(n - i, n - 1):
                        a[i][j] = ' '
        case "left":
            n = int(nums[1])
            a = [['#' for _ in range(n)] for _ in range(n)]
            for i in range(n - 1):
                for j in range(i + 1, n):
                    a[i][j] = ' '
            if t == 'n':
                for i in range(2, n - 1):
                    for j in range(1, i):
                        a[i][j] = ' '
        case "diamond":
            n = int(nums[0])
            a = [['#' for _ in range(n)] for _ in range(n)]
            for i in range(n):
                for j in range(abs(n // 2 - i)):
                    a[i][j] = ' '
                    a[i][n - j - 1] = ' '
            if t == 'n':
                for i in range(1, n - 1):
                    for j in range(abs(n // 2 - i) + 1, n - 1 - abs(n // 2 - i)):
                        a[i][j] = ' '
    for l in a:
        print("".join(l).rstrip())