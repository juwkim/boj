p = [[*map(int, input().split())] for _ in range(int(input()))]
for _ in range(int(input())):
    i, d = map(int, input().split())
    x, y = p[i-1]
    print(sum((x - a)**2 + (y - b)**2 <= d*d for a, b in p) - 1)