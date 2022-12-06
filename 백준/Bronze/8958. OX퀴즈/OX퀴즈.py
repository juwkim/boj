import sys

N = int(input())
for _ in range(N):
    res = list(sys.stdin.readline())
    score = 0
    pos = 0
    for i in range(len(res)):
        if res[i] == "O":
            pos += 1
            score += pos
        else:
            pos = 0
    print(score)