def solve():
    N = int(input())
    pos = 20
    down = 0
    since_first_down = 0
    for y in map(int, input().split()):
        pos += y
        since_first_down += y
        down += 1
        if down == 4 and since_first_down < 10:
            return "Nothing"
        if since_first_down >= 10:
            down = 0
            since_first_down = 0
        if pos >= 100:
            return "Touchdown"
        if pos <= 0:
            return "Safety"
    return "Nothing"
print(solve())