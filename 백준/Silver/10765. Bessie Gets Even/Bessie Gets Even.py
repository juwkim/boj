dic = {i: [0, 0] for i in 'BESIGOM'}
for _ in range(int(input())):
    s, num = input().split()
    dic[s][int(num) & 1] += 1

def solve(a, b, num):
    if num == 0:
        return dic[a][0] * dic[b][0] + dic[a][1] * dic[b][1]
    else:
        return dic[a][0] * dic[b][1] + dic[a][1] * dic[b][0]

odd = dic['M'][1] * solve('B', 'I', 1) * (solve('G', 'O', 0) * solve('S', 'E', 1) + solve('G', 'O', 1) * solve('S', 'E', 0))
total = 1
for l in dic.values():
    total *= sum(l)
print(total - odd)