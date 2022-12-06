import sys
input = lambda: sys.stdin.readline().rstrip('\n')

log = set()
for _ in range(int(input())):
    name, what = input().split()
    if what == 'enter':
        log.add(name)
    else:
        log.remove(name)
for name in sorted(log, reverse=True):
    print(name)