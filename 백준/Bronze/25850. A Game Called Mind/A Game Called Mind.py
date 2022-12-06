buf = []
for i in map(chr, range(65, 65 + int(input()))):
    nums = list(map(int, input().split()))[1:]
    for num in nums:
        buf.append((num, i))
buf.sort()
for l in buf:
    print(l[1], end='')