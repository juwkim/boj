import sys
input = lambda: sys.stdin.readline().rstrip()

def solve():
    input()
    home = {input() for _ in range(int(input()))}
    if "dongho" in home: return "dongho"
    for _ in range(int(input())): home.discard(input())
    if not home: return "swi"
    if "bumin" in home: return "bumin"
    if "cake" in home: return "cake"
    if "lawyer" in home: return "lawyer"
    return min(home)

print(solve())