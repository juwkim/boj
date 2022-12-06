from itertools import permutations
while (s:= input())[0] != '0':
    t, msg = s.split()
    t = int(t)
    msg = sorted([ord(c) - 64 for c in msg], reverse=True)
    ans = False
    for v, w, x, y, z in permutations(msg, 5):
        if v - w**2 + x**3 - y**4 + z**5 == t:
            ans = v, w, x, y, z
            break

    if ans:
        print(''.join(map(lambda x: chr(x + 64), ans)))
    else:
        print('no solution')