board = [list('***ABCDE'), list('FGHIJKLM'), list('NOPQRSTU'), list('VWXYZ***')]
words = [input() for _ in range(int(input()))]
dest = input()
buf = []

l = len(dest)
for word in words:
    if len(word) > l and word[:l] == dest:
        buf.append(word[l])
s = set(buf)

for line in board:
    for c in line:
        if c in buf:
            print(c, end='')
        else:
            print('*', end='')
    print()