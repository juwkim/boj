import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a = input()
    print(sum(a[i:i+3] == "WOW" for i in range(len(a) - 2)))