import sys

N, X = map(int, sys.stdin.readline().split())
sequence = list(map(int, sys.stdin.readline().split()))

for num in sequence:
    if num < X:
        print(num, end=" ")