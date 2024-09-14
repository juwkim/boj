import sys
input = sys.stdin.readline

N, M = map(int, input().split())
i, s = 1, input().split()
nums, group, now = [-1, int(s[0]) & 1], [-1], int(s[0]) % 2 == 0
to_group = [-1]
while i < len(s):
    to_group.append(len(group))
    if s[i] == '*':
        now += int(s[i + 1]) % 2 == 0
    else:
        group.append(now)
        now = int(s[i + 1]) % 2 == 0
    nums.append(int(s[i + 1]) & 1)
    i += 2
to_group.append(len(group))
group.append(now)
ans = group.count(0) & 1
print(("even", "odd")[ans & 1])
for _ in range(M):
    X, Y = map(int, input().split())
    if (Y & 1) != nums[X]:
        nums[X] = Y & 1
        idx = to_group[X]
        if Y & 1:
            group[idx] -= 1
            if group[idx] == 0:
                ans ^= 1
        else:
            group[idx] += 1
            if group[idx] == 1:
                ans ^= 1
    print(("even", "odd")[ans & 1])