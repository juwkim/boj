g = lambda: [*map(int, input().split())]

dist = g()
time = [0, 0]
velo = [[], []]
for _ in range(20):
    name, t = input().split()
    name = name.lower()
    t = float(t)
    time[name == 'e'] += t
    velo[name == 'e'].append(dist[name == 'e'] / t)
print('Method 1')
print(f'African: {dist[0] * 10 / time[0]:.2f} furlongs per hour')
print(f'European: {dist[1] * 10 / time[1]:.2f} furlongs per hour')   

print('Method 2')
print(f'African: {sum(velo[0]) / 10:.2f} furlongs per hour')
print(f'European: {sum(velo[1]) / 10:.2f} furlongs per hour')  