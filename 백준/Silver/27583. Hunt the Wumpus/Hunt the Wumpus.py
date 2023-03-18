pos = set()
s = int(input())
while len(pos) != 4:
    s += s // 13 + 15
    pos.add(divmod(s % 100, 10))
cnt = 0
while pos:
    cnt += 1
    i, j = map(int, input())
    if (i, j) in pos:
        pos.remove((i, j))
        print("You hit a wumpus!")
    if pos:
        print(min(abs(s - i) + abs(t - j) for s, t in pos))
print(f'Your score is {cnt} moves.')