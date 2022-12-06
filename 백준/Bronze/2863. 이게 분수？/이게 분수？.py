A, B = map(int, input().split())
C, D = map(int, input().split())
nums = [A/C + B/D, C/D + A/B, D/B + C/A, B/A + D/C]
print(nums.index(max(nums)))