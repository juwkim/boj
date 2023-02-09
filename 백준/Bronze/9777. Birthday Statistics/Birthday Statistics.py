from collections import defaultdict

dic = defaultdict(int)
for i in range(int(input())):
    _, l = input().split()
    dic[l.split('/')[1]] += 1
for i in range(1, 13):
    print(i, dic[str(i)])