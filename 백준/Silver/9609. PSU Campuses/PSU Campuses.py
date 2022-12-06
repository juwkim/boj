dic = {'HP': 103, 'HS': 329, 'HK': 466, 'HT': 148, 'PS': 408, 'PK': 577,
       'PT': 260, 'SK': 287, 'ST': 226, 'KT': 312, 'PH': 103, 'SH': 329,
       'KH': 466, 'TH': 148, 'SP': 408, 'KP': 577, 'TP': 260, 'KS': 287,
       'TS': 226, 'TK': 312}

for _ in range(1, 1 + int(input())):
    s = 'H' + input() + 'H'
    ans = sum(dic[s[i:i+2]] for i in range(len(s)-1))
    print(f'Case {_}:', ans)