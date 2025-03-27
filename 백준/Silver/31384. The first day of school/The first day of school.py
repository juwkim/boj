import sys
input = lambda: sys.stdin.readline().rstrip()

d = {"Tuesday": 0, "Thursday": 1, "Saturday": 2}
table = [[[] for _ in range(3)] for _ in range(4)]
for _ in range(int(input())):
    name = input()
    weekday, order = input().split()
    l, cur, cnt = [], [], -1
    for word in name.split():
        if cnt + len(word) + 1 <= 10:
            cnt += len(word) + 1
            cur.append(word)
        else:
            l.append(" ".join(cur))
            cur = [word]
            cnt = len(word)
    if cur:
        l.append(" ".join(cur))
    table[int(order) - 1][d[weekday]] = l
print("+----------+----------+----------+")
for l in table:
    m = max(1, max(len(x) for x in l))
    for i in range(m):
        print("|", end="")
        for x in l:
            if i < len(x):
                print(f"{x[i]:<10}|", end="")
            else:
                print(" " * 10 + "|", end="")
        print()
    print("+----------+----------+----------+")