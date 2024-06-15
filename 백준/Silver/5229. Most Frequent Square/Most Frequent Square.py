import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a = [bytearray(31) for _ in range(31)]
    k, *nums = map(int, input().split())
    for i in range(0, 2*k, 2):
        a[nums[i]][nums[i+1]] = 1
    buf = []
    for l in range(30, 0, -1):
        cnt = 0
        for i in range(31 - l):
            for j in range(31 - l):
                if a[i][j] and a[i][j + l] and a[i + l][j] and a[i + l][j + l]:
                    cnt += 1
        if cnt:
            buf.append((cnt, l))
    if buf:
        cnt, length = max(buf)
        print(f"LENGTH = {length}, COUNT = {cnt}")
    else:
        print("No squares among the points.")