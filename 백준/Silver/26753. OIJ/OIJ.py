cnt = 0
for c in input():
    cnt += c == 'oij'[cnt % 3]
print(cnt // 3 or 'NIE')