import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

nums = [
    "####.##.##.####",
    "..#..#..#..#..#",
    "###..#####..###",
    "###..####..####",
    "#.##.####..#..#",
    "####..###..####",
    "####..####.####",
    "###..#..#..#..#",
    "####.#####.####",
    "####.####..####",
]

tmp = [input() for _ in range(5)]
ans = []
for time in ["".join(tmp[i][j:j+3] for i in range(5)) for j in range(0, 13, 4)]:
    for i, num in enumerate(nums):
        if all(a + b != '.#' for a, b in zip(num, time)):
            ans.append(str(i))
            break
h = ans[0] + ans[1]
m = ans[2] + ans[3]
print(h + ":" + m)