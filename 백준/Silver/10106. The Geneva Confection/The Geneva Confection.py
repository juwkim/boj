import sys
input = sys.stdin.readline

for _ in range(int(input())):
    nums = [int(input()) for _ in range(int(input()))]
    cur, side = 1, []
    while True:
        if nums and nums[-1] == cur:
            nums.pop()
            cur += 1
        elif side and side[-1] == cur:
            side.pop()
            cur += 1
        elif nums:
            side.append(nums.pop())
        else:
            break
    print("N" if side else "Y")