N = int(input())
ans = [0, 0]
idx = [0, 0]
for i, num in enumerate(map(int, input().split())):
    what = num & 1
    ans[what] += i - idx[what]
    idx[what] += 1
print(min(ans))