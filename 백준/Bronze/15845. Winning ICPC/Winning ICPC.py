N, M = map(int, input().split())
Tcase = [*map(int, input().split())]
sub = [len([1 for x, y in zip(map(int, input().split()), Tcase) if x == y]) for _ in range(N)]
print(sub.index(max(sub)) + 1)