n = int(input())
prev = ' '
for word in input().split():
    if len(prev) > len(word):
        c = ' '
    else:
        c = word[len(prev) - 1]
    prev = word
    print(c, end='')