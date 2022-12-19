from collections import Counter
N = int(input())
Map = [[[int(i) for i in input()] for _ in range(11)] for _ in range(N)]
for _ in range(int(input())):
    cnt = Counter(map(int, input().split()))
    buf = [[0] * 10 for _ in range(10)]
    for key, val in cnt.items():
        for i in range(10):
            for j in range(10):
                buf[i][j] += Map[key][i][j] * val
    for line in buf:
        for num in line:
            print("%02d" % num, end=' ')
        print()
    print()