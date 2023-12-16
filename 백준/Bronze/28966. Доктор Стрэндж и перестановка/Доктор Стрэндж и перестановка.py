import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

n = int(input())
nums = g()
odd = [i + 1 for i in range(0, n, 2) if nums[i] % 2 == 0]
even = [i + 1 for i in range(1, n, 2) if nums[i] % 2 == 1]

if len(odd) == len(even) and len(odd) <= 1:
    if len(odd):
        print(odd[0], even[0])
    elif n >= 3:
        print(1, 3)
    else:
        print(-1, -1)
else:
    print(-1, -1)