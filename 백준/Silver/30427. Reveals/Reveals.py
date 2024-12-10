import sys
input = lambda: sys.stdin.readline().rstrip()

def solve():
    input()
    home = [input() for _ in range(int(input()))]
    if "dongho" in home:
        return "dongho"
    names = {*home}
    for _ in range(int(input())):
        names.discard(input())
    if not names:
        return "swi"
    if "bumin" in names:
        return "bumin"
    if "cake" in names:
        return "cake"
    if "lawyer" in names:
        return "lawyer"
    return min(names)

print(solve())