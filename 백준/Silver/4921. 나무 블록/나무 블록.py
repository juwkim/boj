step = 1
dic = {'1': '45', '3': '45', '4': '23', '5': '8', '6': '23', '7': '8', '8': '67'}
while (s:= input()) != '0':
    ans = 'VALID'
    if s[0] + s[-1] != '12' or s.count('2') != 1:
        ans = 'NOT'
    else:
        for a, b in zip(s, s[1:]):
            if b not in dic[a]:
                ans = 'NOT'
                break
    print(f'{step}. {ans}')
    step += 1