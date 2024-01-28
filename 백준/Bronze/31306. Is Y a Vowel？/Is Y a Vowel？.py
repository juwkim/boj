vowel, y = 0, 0
for c in input():
    if c in 'aeiou':
        vowel += 1
    elif c == 'y':
        y += 1
print(vowel, vowel + y)