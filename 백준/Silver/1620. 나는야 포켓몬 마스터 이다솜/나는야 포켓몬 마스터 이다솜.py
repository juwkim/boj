import sys
names, nums = {}, {}
N, M = map(int, sys.stdin.readline().split())
for num in range(1, N+1):
    name = sys.stdin.readline().rstrip()
    names[name] = num
    nums[num] = name
for i in range(M):
    s = sys.stdin.readline().rstrip()
    print(names[s] if s.isalpha() else nums[int(s)])