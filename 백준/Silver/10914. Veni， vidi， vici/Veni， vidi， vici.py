n = int(input())
for word in input().split():
    for i in range(0, len(word)-1, 2):
        x = (ord(word[i]) + ord(word[i+1]) - n - 97 * 2) % 26 + 97
        print(chr(x), end='')
    print(' ', end='')