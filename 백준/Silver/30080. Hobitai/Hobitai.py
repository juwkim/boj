from collections import defaultdict

n = int(input())
dic = defaultdict(list)
S = input()
for i in range(n - 7):
    p = S[i:i + 8]
    if not dic[p] or i - dic[p][-1] >= 8:
        dic[p].append(i)
k = max(dic, key=lambda x: len(dic[x]))
print(len(dic[k]) * 8)
print(k)