import re
word = ''
while (s := input()).find('E-N-D') == -1:
    word = max([word] + re.findall('[a-zA-Z-]+', s), key=len)
print(word.lower())