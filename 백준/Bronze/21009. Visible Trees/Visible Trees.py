def count(line):
    top, res = line[0], 1
    for a in line[1:]:
        if a > top:
            res += 1
            top = a
    return res

N = int(input())
trees = [[*map(int, input().split())] for _ in range(N)]
print(*map(count, zip(*trees)))
print(*map(count, trees))