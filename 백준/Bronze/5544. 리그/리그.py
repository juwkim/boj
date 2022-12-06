g = lambda: [*map(int, input().split())]

N = int(input())
score = [0] * N
for _ in range(N * (N - 1) // 2):
    A, B, C, D = g()
    score[A-1] += (C > D) * 3 + (C == D)
    score[B-1] += (D > C) * 3 + (C == D)
print(*[1 + sum(our < opp for opp in score) for our in score])