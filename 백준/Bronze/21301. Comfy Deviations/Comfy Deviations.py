import statistics as s
print('NOT ' * (s.stdev(map(float, input().split())) >= 1) + 'COMFY')