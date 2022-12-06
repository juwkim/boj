vowel = 'aeiou'
s = input()
if s[0] in vowel: a, b = 0, 1
else: a, b = 1, 0
print(+(all(s[i] in vowel for i in range(a, len(s), 2)) and all(s[i] not in vowel for i in range(b, len(s), 2))))