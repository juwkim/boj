from collections import Counter
for _ in range(int(input())):
    A = Counter([*map(int, input().split())][1:])
    B = Counter([*map(int, input().split())][1:])
    if A == B:
        print('D')
    else:
        t = max([A, B], key=lambda x: (x[4], x[3], x[2], x[1]))
        print('A' if t == A else 'B')