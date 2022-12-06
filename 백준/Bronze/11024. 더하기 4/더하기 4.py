import sys
input()
for line in sys.stdin:
    print(sum(map(int, line.split())))