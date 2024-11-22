input()
print(*[1+bin(int(p))[::-1].index('1')for p in input().split()])