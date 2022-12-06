g = lambda: [*map(int, input().split())]
from bisect import bisect_left
for _ in range(int(input())):
    n, *l = g()
    l.sort()
    nums = [num ** 2 for num in l]
    buf = []
    for i in range(n-2):
        for j in range(i+1, n-1):
            c = nums[i] + nums[j]
            k = bisect_left(nums, c)
            if k < n and c == nums[k]:
                buf.append('{' + ' '.join(map(str, [l[i], l[j], l[k]])) + '}')
    if buf:
        print('Found Pythogorean triples: ', *sorted(buf))
    else:
        print('No Pythogorean triples found in the sequence.')