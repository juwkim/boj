n, m = map(int, input().split())
scores = [input().split() for _ in range(n)]
num = [i for i, x in enumerate(scores[0]) if x == '100']
print(1, sum(all(score[k] == '100' for k in num) for score in scores))