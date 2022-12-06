score = [0, 0]
last_scored_times = [-11] * 9
for _ in range(int(input())):
    t, a, b = map(int, input().split())
    within = (t - last_scored_times[a] <= 10)
    score[a > 4] += 100 + within * 50
    last_scored_times[a] = t
print(*score) 