g = lambda: [*map(int, input().split())]

N = int(input())
nums = sorted(g())
print((nums[-1] + nums[-2]) // 2)