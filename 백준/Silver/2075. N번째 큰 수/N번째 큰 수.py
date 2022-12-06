import sys
import heapq
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]

N = int(input())
arr = g()
heapq.heapify(arr)
for k in range(N - 1):
    for num in g():
        if arr[0] < num:
            heapq.heappop(arr)
            heapq.heappush(arr, num)
print(arr[0])