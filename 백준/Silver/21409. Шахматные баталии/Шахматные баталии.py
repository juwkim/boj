def solve(who, r1, c1, r2, c2):
    if who == 'B':
        return abs(ord(r1) - ord(r2)) == abs(c1 - c2)
    if who == 'N':
        return sorted([abs(ord(r1) - ord(r2)), abs(c1 - c2)]) == [1, 2]
    if who == 'R':
        return r1 == r2 or c1 == c2
    if who == 'Q':
        return abs(ord(r1) - ord(r2)) == abs(c1 - c2) or (r1 == r2 or c1 == c2)
    if who == 'K':
        return abs(ord(r1) - ord(r2)) <= 1 and abs(c1 - c2) <= 1

a, r1, c1 = input()
b, r2, c2 = input()
c1, c2 = map(int, [c1, c2])
s = solve(a, r1, c1, r2, c2)
t = solve(b, r2, c2, r1, c1)
if s and t:
    print('BOTH')
elif s:
    print('WHITE')
elif t:
    print('BLACK')
else:
    print('NONE')