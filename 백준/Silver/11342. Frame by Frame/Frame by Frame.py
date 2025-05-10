import sys
input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    tokens = []
    for c in input().split():
        if c == 'X':
            tokens.append(10)
        elif c == '/':
            tokens.append(10 - tokens[-1])
        else:
            tokens.append(int(c))
    score, frame = 0, 0
    i = 0
    while frame < 10:
        if tokens[i] == 10:
            score += 10 + tokens[i+1] + tokens[i+2]
            i += 1
        elif tokens[i] + tokens[i+1] == 10:
            score += 10 + tokens[i+2]
            i += 2
        else:
            score += tokens[i] + tokens[i+1]
            i += 2
        frame += 1
    print(score)