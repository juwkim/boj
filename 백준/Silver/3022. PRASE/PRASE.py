from collections import defaultdict
dic = defaultdict(int)
ans = 0
for _ in range(int(input())):
    name = input()
    dic[name] += 1
    ans += (2 * dic[name] > sum(dic.values()) + 1)
print(ans)