import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

t1, t2 = input().split()
h1, m1 = map(int, t1.split(':'))
h2, m2 = map(int, t2.split(':'))

N, T = g()
num_per_day = ((h2 - h1) * 60 + (m2 - m1) - 1) // T
day, left = divmod(N, num_per_day)
time = (h1 * 60 + m1) + T * (left + 1)
h, m = divmod(time, 60)
print(day)
print(f"{h:02d}:{m:02d}")