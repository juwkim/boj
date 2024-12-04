import sys
input = sys.stdin.readline

for _ in range(int(input())):
    B, D = input().split()
    b = int(B) - 1
    ans = 0
    for c in map(int, D):
        ans = (ans + c) % b
    print(ans)