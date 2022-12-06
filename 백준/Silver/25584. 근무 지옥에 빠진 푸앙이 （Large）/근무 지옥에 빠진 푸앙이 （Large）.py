from collections import defaultdict
dic = defaultdict(int)
def res(num):
    for name in input().split():
        if name != '-':
            dic[name] += num
for _ in range(int(input())):
    res(4)
    res(6)
    res(4)
    res(10)

a = dic.values()
if not a or max(a) - min(a) <= 12:
    print('Yes')
else:
    print('No')