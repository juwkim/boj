mode = int(input())
n, *l = map(int, input().split())
print(max(sum(l) - 2 * n, 0) if mode == 1 else min(l))