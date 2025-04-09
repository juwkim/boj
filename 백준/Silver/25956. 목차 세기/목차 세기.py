n, *nums = map(int, open(0))
nums.append(0)
cnt = [0] * (n + 1)
ans = [0] * n
st, prv = [], 0
for i in range(n + 1):
    num = nums[i]
    if prv + 1 < num:
        ans, st = [-1], []
        break
    while st and num <= st[-1][1]:
        idx, level = st.pop()
        ans[idx] = cnt[level]
        cnt[level] = 0
    st.append((i, num))
    cnt[num - 1] += 1
    prv = num
print(*ans)