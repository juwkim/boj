import sys
input = lambda: sys.stdin.readline().rstrip()

tc = 1
while P:=int(input()):
    scores = [*map(int, input().split())]
    l = []
    for _ in range(int(input())):
        name, *sheets = input().split(',')
        score = 0
        for i, sheet in enumerate(sheets):
            a, b = sheet.split('/')
            if a != '0' and b != '-':
                score -= scores[i]
        l.append((score, name.lower(), name))
    print(f"Contest {tc}")
    rank, prv = 1, -1
    for i, (score, _, name) in enumerate(sorted(l), 1):
        if score != prv:
            rank = i
            prv = score
        print(f"{rank} {name} {-score}")
    tc += 1