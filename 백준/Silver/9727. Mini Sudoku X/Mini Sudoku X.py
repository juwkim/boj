import sys
input = lambda: sys.stdin.readline().rstrip()

g = lambda: [*map(int, input().split())]
for _ in range(1, 1 + int(input())):
    Map = [g() for _ in range(6)]
    if any(sum(line) != 21 for line in Map):
        ans = 0
    elif any(sum(line) != 21 for line in zip(*Map)):
        ans = 0
    elif sum(Map[i][i] for i in range(6)) != 21:
        ans = 0
    elif sum(Map[5-i][i] for i in range(6)) != 21:
        ans = 0
    elif any(sum(Map[i][:3]) + sum(Map[i+1][:3]) != 21 for i in range(0, 6, 2)):
        ans = 0
    elif any(sum(Map[i][3:]) + sum(Map[i+1][3:]) != 21 for i in range(0, 6, 2)):
        ans = 0
    else:
        ans = 1
    print(f'Case#{_}:', ans)