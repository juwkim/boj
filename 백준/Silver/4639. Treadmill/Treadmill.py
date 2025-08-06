def decode_bit(a, b):
    if a in (4, 5) and b in (4, 5):
        return 0
    if a in (0, 1) and b in (8, 9):
        return 1
    return None

tc = 1
n, *nums = map(int, open(0).read().split())
it = iter(nums)
for _ in range(n):
    l = []
    while (v:=next(it)) != 10:
        l.append(v)
    print(f"Program {tc}")
    i, L = 0, len(l)
    while i + 16 <= L:
        bits = []
        ok = True
        for b in range(8):
            bit = decode_bit(l[i + 2*b], l[i + 2*b + 1])
            if bit is None:
                ok = False
                break
            bits.append(bit)
        if ok and bits[0] == 0 and bits[1] == 1:
            speed = bits[2] + (bits[3] << 1) + (bits[4] << 2)
            incl  = bits[5] + (bits[6] << 1) + (bits[7] << 2)
            mm, ss = divmod(i // 3, 60)
            print(f"{mm:02d}:{ss:02d} Speed {speed} Inclination {incl}")
            i += 16
        else:
            i += 1
    tc += 1