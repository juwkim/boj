import sys
input = lambda: sys.stdin.readline().rstrip()

for tc in range(1, 1 + int(input())):
    ans, st = 0, 0
    for c in input():
        if c == 'o':
            st += 1
        elif st == 0:
            ans += 1
        else:
            st -= 1
    ans += st
    print(f"Data Set {tc}:\n{ans}\n")