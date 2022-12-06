import sys
W, N = map(int, [input(), input()])
area = sum(eval(sys.stdin.readline().replace(' ', '*')) for _ in range(N))
print(area//W)