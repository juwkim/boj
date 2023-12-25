import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

for _ in range(int(input())):
    good = {input().lower() for _ in range(int(input()))}
    words = 0
    total_words = 0
    for _ in range(int(input())):
        l = []
        p = []
        for c in input().lower():
            if c.islower():
                p.append(c)
            else:
                if p:
                    l.append(''.join(p))
                    p = []
        if p:
            l.append(''.join(p))
        total_words += len(l)
        words += sum(w in good for w in l)
    if words * 4 >= 3 * total_words:
        print("It's a hit!")
    else:
        print("Delete immediately!")