import sys
input = lambda: sys.stdin.readline().rstrip()

p = "qwertyuiop", "asdfghjkl", "zxcvbnm"
keyboard = {c: (i, j) for i in range(3) for j, c in enumerate(p[i])}
for _ in range(int(input())):
    s, l = input().split()
    words = []
    for _ in range(int(l)):
        word = input()
        dist = 0
        for a, b in zip(s, word):
            x1, y1 = keyboard[a]
            x2, y2 = keyboard[b]
            dist += abs(x1 - x2) + abs(y1 - y2)
        words.append((dist, word))
    words.sort()
    for dist, word in words:
        print(word, dist)