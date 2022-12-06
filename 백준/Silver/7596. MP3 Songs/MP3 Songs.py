import sys
input = lambda: sys.stdin.readline().rstrip('\n')

i = 1
while n:= int(input()):
    res = [input() for _ in range(n)]
    res.sort(key=lambda x: x.lower())
    print(i)
    i += 1
    for song in res:
        print(song)