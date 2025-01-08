s = input()
def solve(l, r):
    if l > r:
        print('0', end='')
    else:
        c = s[l] if s[l].isdigit() else '0'
        print(f"({c})+", end='')
        solve(l + 1, r)
solve(0, len(s) - 1)