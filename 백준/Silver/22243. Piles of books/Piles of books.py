import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

def scan():
    for i in range(N):
        cur = 0
        for j in range(N):
            if nums[i][j] > cur:
                cur = nums[i][j]
                check[i][j] = True

N = int(input())
nums = [g() for _ in range(N)]
check = [bytearray(N) for _ in range(N)]
scan()
for _ in range(3):
    nums = [l[::-1] for l in zip(*nums)]
    check = [list(reversed(l)) for l in zip(*check)]
    scan()
print(sum(sum(row) for row in check))