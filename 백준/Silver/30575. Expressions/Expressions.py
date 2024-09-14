import sys
input = sys.stdin.readline

N, M = map(int, input().split())
i, s = 1, input().split()
nums, group, now = [-1, int(s[0]) & 1], [-1], ~int(s[0])&1
to_group = [-1]
while i < len(s):
    to_group.append(len(group))
    num = int(s[i + 1])
    if s[i] == '*':
        now += ~num&1
    else:
        group.append(now)
        now = ~num&1
    nums.append(num & 1)
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
            ans ^= (group[idx] == 0)
        else:
            group[idx] += 1
            ans ^= (group[idx] == 1)
    print(("even", "odd")[ans & 1])