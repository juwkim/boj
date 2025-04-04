import sys
input = sys.stdin.readline

for _ in range(int(input())):
    K = int(input())
    ans = "GoHanGang"
    for l in range(2, int((2 * K + .25)**.5 + .5)):
        i = (2 * K + 3 * l - l**2 - 1) // (2 * l)
        if l * (2 * i + l - 1) == 2 * K:
            ans = "Gazua"
            break
    print(ans)