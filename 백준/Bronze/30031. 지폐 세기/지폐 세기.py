d = {'136': 1000, '142': 5000, '148': 10000, '154': 50000}
ans = 0
for _ in range(int(input())):
    ans += d[input()[:3]]
print(ans)