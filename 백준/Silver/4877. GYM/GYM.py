g = lambda: [*map(int, input().split())]

l = g()
buf = [l]
n = len(l)
nums = [sum(l)]
for _ in range(n-1):
    l = g()
    buf.append(l)
    nums.append(sum(l))

p = [1] + [0] * (n - 1)
for _ in range(10):
    for num in p:
        print("%.5f" % num, end=' ')
    print()
    p = [sum(buf[j][i] * p[j] / nums[j] for j in range(n)) for i in range(n)]