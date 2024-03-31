import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import defaultdict

tc = 1
infos, names, payment = {}, {}, defaultdict(int)
while (s:=input()) != '9':
    recode, *l = s.split(',')
    match recode:
        case '1':
            buf = []
            name, *nums = l
            for num in nums:
                a, b = map(int, num.split('.'))
                buf.append(a * 100 + b)
            infos[name] = tuple(buf)
        case '2':
            name, account = l
            names[account] = name
        case '5':
            day, name, A, tmp, B = l
            day = day[:-6]
            name1, name2 = names[A], names[B]
            a, b = map(int, tmp.split('.'))
            money = a * 100 + b
            if name != name1:
                ans = "NOT OWNER"
            elif name1 == name2:
                if money > infos[name1][0]:
                    ans = "IAT MAX EXCEEDED"
                elif payment[(day, name1, 0)] + money > infos[name1][1]:
                    ans = "IAT DEL EXCEEDED"
                else:
                    ans = "IAT OK"
                    payment[(day, name1, 0)] += money
            else:
                if money > infos[name1][2]:
                    ans = "PAYMENT MAX EXCEEDED"
                elif payment[(day, name1, 1)] + money > infos[name1][3]:
                    ans = "PAYMENT DEL EXCEEDED"
                else:
                    ans = "PAYMENT OK"
                    payment[(day, name1, 1)] += money
            print(f"INSTRUCTION {tc}: {ans}")
            tc += 1