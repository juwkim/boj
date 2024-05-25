import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]

while N := int(input()):
    nums = sorted(g() for _ in range(N))
    x, y = (nums[0][0] + nums[-1][0]) / 2, (nums[0][1] + nums[-1][1]) / 2
    if all((x, y) == ((nums[i][0] + nums[N - i - 1][0]) / 2, (nums[i][1] + nums[N - i - 1][1]) / 2) for i in range(1, (N + 1) // 2)):
        print(f"V.I.P. should stay at ({x},{y}).")
    else:
        print("This is a dangerous situation!")