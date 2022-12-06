total, max_peoples = 0, 0
for _ in range(10):
    if total == 10000:
        print(total)
        break
    Out, In = map(int, input().split())
    total += In - Out
    if total > max_peoples:
        max_peoples = total
print(max_peoples)