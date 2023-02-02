from collections import defaultdict

dic = defaultdict(int)
for _ in range(int(input())):
    addr = input()
    idx = addr.find('//')
    if idx != -1:
        addr = addr[idx + 2:]
    addr = addr.split('/')[0]
    ext = addr.split('.')[-1]
    dic[ext] += 1
    
Max = max(dic.values())
print(Max)
for key in dic:
    if dic[key] == Max:
        print(key, end=' ')