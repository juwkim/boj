g = lambda: [*map(int, input().split())]

while n:= int(input()):
    scores = sorted(g())
    print(min(j - i for i, j in zip(scores, scores[1:])))