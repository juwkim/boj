dic = {i: [0, 0] for i in 'BESIGOM'}
for _ in range(int(input())):
    s, num = input().split()
    dic[s][int(num) & 1] += 1

odd = dic['M'][1] * (dic['B'][1] * dic['I'][0] + dic['B'][0] * dic['I'][1])
tmp = (dic['G'][0] * dic['O'][0] + dic['G'][1] * dic['O'][1]) * (dic['S'][0] * dic['E'][1] + dic['S'][1] * dic['E'][0])
tmp += (dic['G'][0] * dic['O'][1] + dic['G'][1] * dic['O'][0]) * (dic['S'][0] * dic['E'][0] + dic['S'][1] * dic['E'][1])
odd *= tmp

total = 1
for l in dic.values():
    total *= sum(l)
print(total - odd)