n, k = map(int, input().split())
ext = bytearray(n)
idx = (k - 1) % n
while ext[idx] == 0:
    ext[idx] = 1
    idx = (idx + k) % n
print(ext.count(0))