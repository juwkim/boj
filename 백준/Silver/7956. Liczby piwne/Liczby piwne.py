import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    b = bin(n)[2:]
    if n & 1:
        if b == b[::-1]:
            print("TAK")
        else:
            print("NIE")
    elif all(b[i] != b[-i-1] for i in range(len(b) + 1 >> 1)):
        print("TAK")
    else:
        print("NIE")