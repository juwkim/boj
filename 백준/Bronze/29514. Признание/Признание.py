S = input()
def solve(lower):
    T, cnt = [], 0
    for c in S:
        if not c.isalpha():
            T.append(c)
            continue
        if c.isupper() and lower:
            cnt += 1
            T.append(c.lower())
        elif c.islower() and not lower:
            cnt += 1
            T.append(c.upper())
        else:
            T.append(c)
        lower ^= 1
    return "".join(T), cnt

T1, cnt1 = solve(True)
T2, cnt2 = solve(False)
if cnt1 < cnt2:
    print(T1)
else:
    print(T2)