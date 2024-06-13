import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a, b = 0, 0
    for num in map(int, input().split()):
        a, b = max(a, b), a + num
    print(max(a, b))