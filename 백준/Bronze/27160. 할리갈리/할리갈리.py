from collections import defaultdict
dic = defaultdict(int)
for _ in range(int(input())):
    name, amount = input().split()
    dic[name] += int(amount)
if 5 in dic.values():
    print('YES')
else:
    print('NO')