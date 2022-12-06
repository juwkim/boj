import re
for _ in range(int(input())):
    text = input()
    vowel = len(re.findall("[aeiouAEIOU]", text))
    consonant = len(text) - vowel - text.count(' ')
    print(consonant, vowel)