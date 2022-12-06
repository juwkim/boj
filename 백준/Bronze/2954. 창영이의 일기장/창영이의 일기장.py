s = input()
for vowel in 'aeiou':
    s = s.replace(vowel + 'p' + vowel, vowel)
print(s)