from collections import defaultdict
idx = {}
dic = defaultdict(int)
cnt = 0
while (s:= input()) != '0':
    if s not in idx:
        idx[s] = cnt
    dic[s] += 1
for k in sorted(dic, key=idx.get):
    print(f'{k}: {dic[k]}')
print('Grand Total:', sum(dic.values()))