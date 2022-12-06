import sys
input = lambda: sys.stdin.readline().rstrip()

for _ in range(int(input())):
    input()
    nums = set(input().split())
    input()
    for num in input().split():
        print(+(num in nums))