from collections import Counter
cows = [*input()]
count = 0
for _ in range(25):
    idx = cows[1:].index(cows[0]) + 1
    count += sum(i == 1 for i in Counter(cows[1:idx]).values())
    del cows[idx]
    del cows[0]
print(count)