import sys
Br, Bc, Dr, Dc, Jr, Jc = map(int, sys.stdin.read().split())
bessie = max(abs(Br - Jr), abs(Bc - Jc))
daisy = abs(Dr - Jr) + abs(Dc - Jc)
print('bessie' if bessie < daisy else 'daisy' if bessie > daisy else 'tie')