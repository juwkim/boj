import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from collections import defaultdict

dic = defaultdict(int)
Sum, Xor = 0, 0
for _ in range(int(input())):
    s = input()
    match s[0]:
        case '1':
            num = int(s[2:])
            Sum += num
            Xor ^= num
        case '2':
            num = int(s[2:])
            Sum -= num
            Xor ^= num
        case '3':
            print(Sum)
        case '4':
            print(Xor)