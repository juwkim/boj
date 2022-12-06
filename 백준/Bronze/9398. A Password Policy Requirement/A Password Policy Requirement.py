import re
g = lambda s: re.search('[A-Z]', s) and re.search('[a-z]', s) and re.search('[\d]', s)
for _ in range(int(input())):
    s, flag = input(), 0
    for i in range(6, len(s)+1):
        if any([g(s[j:i+j]) for j in range(0, len(s)-i+1)]):
            flag = 1
            break
    print(i*flag)