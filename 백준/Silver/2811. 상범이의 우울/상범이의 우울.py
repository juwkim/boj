N = int(input())
nums = [*map(int, input().split())]
idxs, prev = [], None
for i in range(N):
    if nums[i] >= 0:
        if prev != None:
            idxs.append((prev, i - prev))
            prev = None
    elif prev == None:
        prev = i
if prev != None:
    idxs.append((prev, N - prev))

Max_len, candidate = 0, []
gived = bytearray(N)
for i in range(len(idxs) - 1, -1, -1):
    idx, Len = idxs[i]
    if Len > Max_len:
        Max_len = Len
        candidate = [idx]
    elif Len == Max_len:
        candidate.append(idx)
    for j in range(max(0, idx - 2 * Len), idx):
        gived[j] = 1
ans = sum(gived)
if candidate:
    ans += max(gived[max(0, idx - 3 * Max_len):max(0, idx - 2 * Max_len)].count(0) for idx in candidate)
print(ans)