from collections import defaultdict
dic = defaultdict(int)
for _ in range(int(input())):
    product, cnt = input().split()
    dic[product] += int(cnt)
for key in sorted(dic, key=lambda x: (len(x), x)):
    print(key, dic[key])