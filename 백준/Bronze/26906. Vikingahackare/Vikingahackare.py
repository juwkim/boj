dic = {}
for _ in range(int(input())):
    c, num = input().split()
    dic[num] = c
s = input()
for i in range(0, len(s), 4):
    if s[i:i+4] in dic:
        c = dic[s[i:i+4]]
    else:
        c = '?'
    print(c, end='')