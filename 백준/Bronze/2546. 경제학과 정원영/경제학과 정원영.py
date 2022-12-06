from statistics import *
g = lambda: [*map(int, input().split())]
for _ in range(int(input())):
    input(), input()
    a, b = g(), g()
    me_a, me_b = mean(a), mean(b)
    print(sum(me_b < i < me_a for i in a))