import sys
input = sys.stdin.readline

num = 100_0001
buf = [1] * num
for i in range(2, num):
    for j in range(i, num, i):
        buf[j] += i
for i in range(2, num):
    buf[i] += buf[i-1]

for _ in range(int(input())):
    print(buf[int(input())])