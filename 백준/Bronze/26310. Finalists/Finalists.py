score = {}
N = int(input())
for _ in range(6):
    nation, *l = input().split()
    score[nation] = sum(a * b for a, b in zip(map(int, l), (0.56, 0.24, 0.14, 0.06, 0.3)))

rank_taiwan = 1 + sum(score[nation] > score['Taiwan'] for nation in score)
print(N // 6 + (rank_taiwan <= N % 6))