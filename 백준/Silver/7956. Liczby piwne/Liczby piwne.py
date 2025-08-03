import sys
input = sys.stdin.readline

for _ in range(int(input())):
    b = bin(n:=int(input()))
    print("NTIAEK"[all((b[i+2] == b[-i-1]) == n & 1 for i in range(len(b) - 1 >> 1))::2])