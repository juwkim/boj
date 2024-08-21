d = {'tera': 12, 'giga': 9, 'mega': 6, 'kilo': 3, 'deci': -1, 'centi': -2, 'milli': -3, 'micro': -6, 'nano': -9}
pref, pw = input().split('meter')
pw = int(pw[1]) if pw else 1
res = 0
i = 0
while i < len(pref):
    if pref[i:i+4] in d:
        res += d[pref[i:i+4]]
        i += 4
    else:
        res += d[pref[i:i+5]]
        i += 5
print(res * pw)