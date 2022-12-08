g = lambda: [*map(int, input().split())]


N = int(input())
all_song = set()
song = [set() for i in range(N)]
new = 0
for _ in range(int(input())):
    K, *nums = g()
    if 1 in nums:
        all_song.add(new)
        for num in nums:
            song[num-1].add(new)
        new += 1
    else:
        tmp = set()
        for num in nums:
            tmp |= song[num-1]
        for num in nums:
            song[num-1] |= tmp
for i in range(N):
    if song[i] == all_song:
        print(i + 1)