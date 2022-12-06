N = int(input())
A = [*map(int, input().split())]
X, Y = map(int, input().split())
print(N * X // 100, sum(score >= Y for score in A))