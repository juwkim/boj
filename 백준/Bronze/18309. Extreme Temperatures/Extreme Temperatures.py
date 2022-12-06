import sys
Min, Max = 100, -100
for i in sys.stdin:
    a = [*map(int, i.split()[1:])]
    Min = min(Min, min(a))
    Max = max(Max, max(a))
print(Min, Max)