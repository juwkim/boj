import sys
input = lambda: sys.stdin.readline().rstrip('\n')

dic = {}
for _ in range(int(input())):
    name, amount = input().split()
    if dic.get(name):
        dic[name] += int(amount)
    else:
        dic[name] = int(amount)
for k, v in sorted(dic.items()):
    print(k, v)