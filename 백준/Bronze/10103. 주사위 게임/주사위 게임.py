n = int(input())
scoreA, scoreB = 100, 100
for _ in range(n):
    A, B = map(int, input().split())
    if A < B:
        scoreA -= B
    elif A > B:
        scoreB -= A
print(scoreA, scoreB, sep='\n')