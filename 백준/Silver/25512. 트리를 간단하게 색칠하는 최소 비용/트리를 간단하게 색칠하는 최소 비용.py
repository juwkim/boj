import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]

n = int(input())
tree = [[] for _ in range(n)]
for _ in range(n - 1):
    p, c = g()
    tree[p].append(c)
cost = [g() for _ in range(n)]
nums = [0, 0]
st = [(0, 0)]
while st:
    cur, d = st.pop()
    nums[0] += cost[cur][d&1]
    nums[1] += cost[cur][d+1&1]
    for nxt in tree[cur]:
        st.append((nxt, d + 1))
print(min(nums))