N, K, *nums = map(int, open(0).read().split())
order = [[1e9] for _ in range(K + 1)]
for i in range(K - 1, -1, -1):
    order[nums[i]].append(i)
ans, state = 0, set()
for num in nums:
    order[num].pop()
    if num in state:
        continue
    if len(state) == N:
        state.remove(max(state, key=lambda x: order[x][-1]))
        ans += 1
    state.add(num)
print(ans)