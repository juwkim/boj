n = int(input())
board = [input() for _ in range(n)]
board += [''.join(i) for i in zip(*board)]
print(int(all(l.count('B') * 2 == n and 'BBB' not in l and 'WWW' not in l for l in board)))