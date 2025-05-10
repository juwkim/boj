import sys
input = sys.stdin.readline

while n:=int(input()):
    ans = "No such base"
    if n == 3:
        ans = 4
    elif n > 3:
        n -= 3
        for b in range(4, int(n**.5) + 1):
            if n % b == 0:
                ans = b
                break
        else:
            if n >= 12 and n % 3 == 0:
                ans = n // 3
            elif n >= 8 and n % 2 == 0:
                ans = n // 2
            elif n >= 4:
                ans = n
    print(ans)