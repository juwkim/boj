n, k = map(int, input().split())
print(sum(a * min(i, k) for i, a in enumerate(sorted(map(int, input().split())))))