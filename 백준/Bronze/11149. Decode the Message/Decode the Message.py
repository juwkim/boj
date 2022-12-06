for _ in range(int(input())):
    words = [(sum(map(ord, i)) + 11 * len(i)) % 27 for i in input().split()]
    for word in words:
        print(' ' if word == 26 else chr(word + 97), end='')
    print()