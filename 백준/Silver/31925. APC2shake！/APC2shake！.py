import sys
input = lambda: sys.stdin.readline().rstrip()

buf = []
for _ in range(int(input())):
    name, attending, icpc_win, shake_rank, apc_rank = input().split()
    shake_rank = int(shake_rank)
    if attending == "hewhak" or icpc_win == "winner" or (shake_rank != -1 and shake_rank <= 3):
        continue
    buf.append((int(apc_rank), name))
buf = sorted(buf)[:10]
ans = sorted(buf[i][1] for i in range(len(buf)))
print(len(ans), *ans)