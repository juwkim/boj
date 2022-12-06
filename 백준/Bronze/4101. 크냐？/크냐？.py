import sys
while True:
    a, b = map(int, sys.stdin.readline().split())
    if (a, b) == (0, 0):
        break
    print('Yes' if a > b else 'No')