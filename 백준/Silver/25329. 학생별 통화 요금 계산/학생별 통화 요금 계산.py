from collections import defaultdict
dic = defaultdict(int)
for _ in range(int(input())):
    t, name = input().split()
    h, m = map(int, t.split(':'))
    dic[name] += h * 60 + m
for key in dic:
    cost = 10
    if dic[key] > 100:
        cost += (dic[key] - 51) // 50 * 3
    dic[key] = cost
for name, val in sorted(dic.items(), key=lambda x: (-x[1], x[0])):
    print(name, val)