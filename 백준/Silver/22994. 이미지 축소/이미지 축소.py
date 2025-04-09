import sys
input = lambda: sys.stdin.readline().rstrip()

ni, mj = map(int, input().split())
image = [input() for _ in range(ni)]
def solve(l):
    a = len(l[0])
    for num in range(a, 1, -1):
        if a % num == 0 and all(all(len({*l[i][j:j+num]}) == 1 for j in range(0, a, num)) for i in range(len(l))):
            return num
    return 1

j, i = solve(image), solve([*zip(*image)])
print(ni // i, mj // j)
for x in range(0, ni, i):
    for y in range(0, mj, j):
        print(image[x][y], end='')
    print()