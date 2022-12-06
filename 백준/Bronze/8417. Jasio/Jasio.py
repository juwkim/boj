def solve(word):
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            return 1
    for i in range(len(word)-2):
        if word[i] == word[i+2]:
            return 1
    return 0

a, b = 0, 0
for _ in range(int(input())):
    word = input()
    a += solve(word)
    b += solve(word.replace('i', 'j').replace('p', 'd').replace('b', 'd'))
print(a, b)