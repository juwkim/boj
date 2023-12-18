import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

dic = {}
for _ in range(int(input())):
    t, X, V = input().split()
    penalty, is_ok = dic.get(X, [0, False])
    if is_ok or V == "CE":
        continue
    if V == "OK":
        h, m = map(int, t.split(":"))
        dic[X] = [penalty + h * 60 + m, True]
    else:
        dic[X] = [penalty + 20, False]

key = [k for k, (penalty, is_ok) in dic.items() if is_ok]
penalty = sum(dic[k][0] for k in key)
print(len(key), penalty)