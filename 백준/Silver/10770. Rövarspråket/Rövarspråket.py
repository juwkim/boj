vowel = set('aeiou')
ans = []
for c in input():
    ans.append(c)
    if c not in vowel:
        ans.append(min('aeiou', key=lambda x: (abs(ord(x) - ord(c)), ord(x))))
        if c == 'z':
            ans.append('z')
        else:        
            num = ord(c) + 1
            if chr(num) in vowel:
                num += 1
            ans.append(chr(num))
print(*ans, sep='')