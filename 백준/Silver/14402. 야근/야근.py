from collections import defaultdict
dic = defaultdict(int)
ans = 0
for _ in range(int(input())):
    name, cmd = input().split()
    if cmd == '+':
        dic[name] += 1
    elif dic[name] == 0:
        ans += 1
    else:
        dic[name] -= 1
ans += sum(dic.values())
print(ans)