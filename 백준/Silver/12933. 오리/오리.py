import sys
input = lambda: sys.stdin.readline().rstrip()

dic = {c: 0 for c in "quack"}
ans = -1
for c in input():
    dic[c] += 1
    if not (dic['q'] >= dic['u'] >= dic['a'] >= dic['c'] >= dic['k']):
        break
    ans = max(ans, dic['q'] - dic['k'])
if len(set(dic.values())) != 1:
    ans = -1
print(ans)