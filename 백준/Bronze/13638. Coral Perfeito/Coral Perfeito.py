import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]

while True:
    try:
        n = int(input())
        nums = g()
        r, q = divmod(sum(nums), n)
        if q:
            print(-1)
        else:
            ans = sum(abs(r - num) for num in nums) // 2 + 1
            print(ans)
    except:
        break