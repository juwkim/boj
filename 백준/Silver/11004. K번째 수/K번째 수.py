g = lambda: [*map(int, input().split())]
K = int(input().split()[1]) - 1
print(sorted(g())[K])