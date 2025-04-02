import sys
from math import dist, ceil
from collections import defaultdict
input = sys.stdin.readline
g = lambda: map(int, input().split())

class Planet:
    def __init__(self, x, y, s, p):
        self.x, self.y, self.s, self.p = x, y, s, p
        self.owner = 0
        self.arrivals = defaultdict(list)
    
    def __str__(self):
        return f"{('Neutral', 'Player1', 'Player2')[self.owner]} {self.p}"
    
    def run(self, time):
        cnt = [0, 0, 0]
        cnt[self.owner] = self.p
        for ships, owner in self.arrivals[time]:
            cnt[owner] += ships
        self.battle(cnt, 1, 2)
        self.battle(cnt, 0, 1)
        self.battle(cnt, 0, 2)
        for i in range(3):
            if cnt[i]:
                self.owner = i
        self.p = cnt[self.owner]
        self.produce()

    def battle(self, cnt, i, j):
        destroyed = min(cnt[i], cnt[j])
        cnt[i] -= destroyed
        cnt[j] -= destroyed
    
    def produce(self):
        if self.owner:
            self.p += self.s
    
    def set_owner(self, owner):
        self.owner = owner
    
    def send_fleet(self, destination, ships, time):
        self.p -= ships
        arrival_time = time + ceil(dist((self.x, self.y), (destination.x, destination.y)))
        destination.arrivals[arrival_time].append((ships, self.owner))

n = int(input())
planets = [[]] + [Planet(*g()) for _ in range(n)]
s1, s2 = g()
planets[s1].set_owner(1)
planets[s2].set_owner(2)
for i in range(1, n + 1):
    planets[i].produce()

time = 0
for _ in range(int(input())):
    cmd, *args = g()
    match cmd:
        case 0:
            for i in range(1, n + 1):
                planets[i].run(time)
            time += 1
        case 1:
            sp, dp, ships = args
            planets[sp].send_fleet(planets[dp], ships, time)
        case 2:
            print(planets[args[0]])