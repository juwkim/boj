import sys
input = sys.stdin.readline

scores = []
for _ in range(int(input())):
    s, r = input().split()
    scores.append((int(s), int(float(r) * 2)))

cnt, my_score = 0, int(input())
for s, r in sorted(scores, reverse=True):
    cur = r - 2 * cnt - 1
    if s == my_score:
        print(cnt + 1, cnt + cur)
        break
    cnt += cur