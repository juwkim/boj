keyword = input()
k = int(input())

dic = {}
num = 65 + (k - 1)
for c in keyword:
    if c not in dic:
        dic[c] = chr(num)
        num += 1
        if num == 91:
            num = 65


for alpha in map(chr, range(65, 91)):
    if alpha not in dic:
        dic[alpha] = chr(num)
        num += 1
        if num == 91:
            num = 65

for c in input():
    print(dic[c], end='')