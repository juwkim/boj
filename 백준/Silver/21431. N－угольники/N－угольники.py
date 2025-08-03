n, k = map(int, input().split())
seq = [1] * (n - 1)
while True:
    nxt = sum(seq[-(n-1):])
    if nxt > k:
        break
    seq.append(nxt)
print(len(seq))
print(*seq)