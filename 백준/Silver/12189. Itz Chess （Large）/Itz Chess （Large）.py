f = iter(open(0).read().split())
input = lambda: next(f)

def solve(attacker, target):
    ax, ay, atype = attacker
    tx, ty, _ = target
    dx = tx - ax
    dy = ty - ay
    if atype == 'K':
        return max(abs(dx), abs(dy)) == 1
    if atype == 'N':
        return (abs(dx), abs(dy)) in ((1, 2), (2, 1))
    if atype == 'P':
        return dx == 1 and abs(dy) == 1

    directions = []
    if atype in 'RQ':
        directions.extend(((1, 0), (-1, 0), (0, 1), (0, -1)))
    if atype in 'BQ':
        directions.extend(((1, 1), (1, -1), (-1, 1), (-1, -1)))
    for dx_dir, dy_dir in directions:
        x, y = ax + dx_dir, ay + dy_dir
        while 0 <= x < 8 and 0 <= y < 8:
            if (x, y) == (tx, ty):
                return True
            if (x, y) in pos_set:
                break
            x += dx_dir
            y += dy_dir
    return False

T = input()
assert T.isnumeric()
for tc in range(1, int(T) + 1):
    p = input()
    assert p.isnumeric()
    N = int(p)
    pieces = []
    pos_set = set()
    for _ in range(N):
        s = input()
        assert s[2] == '-' and len(s) == 4
        pos, ptype = s.split('-')
        assert pos[0] in 'ABCDEFGH' and pos[1] in '12345678'
        assert ptype in 'KQRNBP'
        x, y = ord(pos[0]) - 65, int(pos[1]) - 1
        pieces.append((x, y, ptype))
        pos_set.add((x, y))
    ans = 0
    for i in range(N - 1):
        for j in range(i + 1, N):
            ans += solve(pieces[i], pieces[j])
            ans += solve(pieces[j], pieces[i])            
    print(f"Case #{tc}: {ans}")