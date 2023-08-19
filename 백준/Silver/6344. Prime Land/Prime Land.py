g = lambda: [*map(int, input().split())]

from collections import defaultdict
while True:
    nums = g()
    if nums == [0]:
        break
    num = 1
    for i in range(0, len(nums), 2):
        num *= pow(nums[i], nums[i + 1])
    num -= 1
    dic = defaultdict(int)
    div = 2
    while num != 1:
        if num % div:
            div += 1
        else:
            num //= div
            dic[div] += 1
    for k, v in sorted(dic.items(), reverse=True):
        print(k, v, end=' ')
    print()