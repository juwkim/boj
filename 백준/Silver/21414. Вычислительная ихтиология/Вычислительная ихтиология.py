import heapq

n, *a = map(int, open(0))
hq = [(max(1000 - a, 1), a, i) for i, a in enumerate(a)]
heapq.heapify(hq)
cur_time, cur_pos = 0, 0
while True:
    birth_time, size, position = heapq.heappop(hq)
    travel_time = abs(position - cur_pos)
    if cur_time + travel_time > birth_time:
        print(birth_time)
        break
    size += 1
    heapq.heappush(hq, (birth_time + max(1000 - size, 1), size, position))
    cur_time, cur_pos = birth_time, position