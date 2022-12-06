g = lambda: sorted(map(float, input().split()))
while (w:=float(input().split()[2])) != 0.0:
    rows, cols = g(), g()
    if all([rows[0]-w/2 <= 0, rows[-1]+w/2 >= 75, cols[0]-w/2 <= 0, cols[-1]+w/2 >= 100]):
        r_right, c_right = rows[0] + w, cols[0] + w
        if all(t-s <= w for s,t in zip(rows, rows[1:])) and all(t-s <= w for s,t in zip(cols, cols[1:])):
            print('YES')
        else:
            print('NO')
    else:
        print('NO')