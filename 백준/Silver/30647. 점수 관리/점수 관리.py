import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N = int(input())
l = eval("".join(input() for _ in range(N)))
l.sort(key=lambda x: (-x["score"], x["name"]))

rank = 1
prev_score = float("inf")
for i in range(N):
    p = l[i]
    if prev_score != p["score"]:
        rank = i + 1
    prev_score = p["score"]
    if p["isHidden"] == 0:
        print(rank, p["name"], p["score"])