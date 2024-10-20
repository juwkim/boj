from collections import deque

to_str = lambda nums: ''.join(str(x) for x in nums)
a = [0, 0, 0, 0, 0, 0, 0, 0, 0]
b = [1, 1, 1, 1, 1, 1, 1, 1, 1]
d = {to_str(a): 0, to_str(b): 0}
dq = deque([(a, 0), (b, 0)])
while dq:
    nums, cnt = dq.popleft()
    for l in (0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6):
        for x in l:
            nums[x] ^= 1
        p = to_str(nums)
        if p not in d:
            d[p] = cnt + 1
            dq.append((nums[:], cnt + 1))
        for x in l:
            nums[x] ^= 1
for _ in range(int(input())):
    nums = "".join("01"[c == 'H'] for _ in range(3) for c in input().split())
    print(d.get(nums, -1))