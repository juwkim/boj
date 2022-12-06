m, n = map(int, input().split())
fence = [0 for _ in range(m)]

for _ in range(n):
    l, r = map(int, input().split())
    fence = fence[:l-1] + [1 for _ in range(r - l + 1)] + fence[r:]
print(['NO', 'YES'][all(fence)])