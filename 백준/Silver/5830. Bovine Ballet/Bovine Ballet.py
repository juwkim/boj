import sys
input = sys.stdin.readline

def solve():
    dx = 0, 1, 0, -1
    dy = 1, 0, -1, 0
    feet = {'FL': (0, 1), 'FR': (1, 1), 'RL': (0, 0), 'RR': (1, 0)}
    d = 0
    min_x = min_y = max_x = max_y = 0
    def rotate(px, py, x, y):
        return px + y - py, py - x + px
    for _ in range(int(input())):
        s = input()
        foot, action = s[:2], s[2]
        if action == 'P':
            for f in feet:
                if f != foot:
                    feet[f] = rotate(*feet[foot], *feet[f])
            d = (d + 1) % 4
        else:
            idx = (d + "FRBL".index(action)) % 4
            x, y = feet[foot]
            feet[foot] = x + dx[idx], y + dy[idx]
        if len(feet.values()) < 4:
            return -1
        for x, y in feet.values():
            min_x, max_x = min(min_x, x), max(max_x, x)
            min_y, max_y = min(min_y, y), max(max_y, y)
    return (max_x - min_x + 1) * (max_y - min_y + 1)
print(solve())