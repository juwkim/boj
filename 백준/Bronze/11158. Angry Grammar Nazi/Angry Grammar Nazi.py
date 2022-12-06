a = ['u', 'ur', 'lol']
b = ['should', 'would']
for _ in [0]*int(input()):
    words = input().split()
    count = 0
    for i, word in enumerate(words):
        if word in a or 'lol' in word or (i != len(words) - 1 and word in b and words[i+1] == 'of'):
            count += 10
    print(count)