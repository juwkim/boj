from math import dist, pi
def g(): return [*map(int, input().split())]
def f(): return [*map(float, input().split())]

earth = (0, 0, 0)
earth_radius = 40000 / (2 * pi)

def check(satellite, target):
    return dist(satellite, earth) ** 2 - earth_radius ** 2 >= dist(satellite, target) ** 2    

while sum(l:= g()):

    k, m = l
    satellite_list = [f() for _ in range(k)]
    
    ans = 0
    for _ in range(m):
        target = f()
        ans += any(check(satellite, target) for satellite in satellite_list)
    print(ans)