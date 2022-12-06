A, B, C, M = map(int, input().split())
work, tiredness = 0, 0
for _ in range(24):
    if tiredness + A <= M:
        tiredness += A
        work += B
    else:
        tiredness = max(0, tiredness - C)
print(work)