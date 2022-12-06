import sys
input()
print(sum([sum(map(int, line.split())) for line in sys.stdin]))