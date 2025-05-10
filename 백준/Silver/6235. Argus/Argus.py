import sys
import heapq
input = lambda: sys.stdin.readline().rstrip()

heap = []
while (line:=input()) != "#":
    q_num, period = map(int, line.split()[1:])
    heapq.heappush(heap, (period, q_num, period))
time, q_num, period = 1e9, 1e9, 1e9
for _ in range(int(input())):
    time, q_num, period = heapq.heappushpop(heap, (time + period, q_num, period))
    print(q_num)