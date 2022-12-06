from collections import Counter
for _ in range(int(input())):
    nums = sorted(int(input()) for _ in range(int(input())))
    a = Counter(nums).most_common()[0][0]
    print(a)