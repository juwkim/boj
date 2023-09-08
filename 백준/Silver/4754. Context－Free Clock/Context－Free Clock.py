dang_per_sec = 11
while True:
    target_ang, time = input().split()
    if target_ang == "-1":
        break
    target_ang = int(target_ang) * 120
    h, m, s = map(int, time.split(':'))
    ang = ((m * 720 + s * 12) - (h * 3600 + m * 60 + s)) % (360 * 120)

    ds = (target_ang - ang) % (360 * 120) // dang_per_sec
    t = (h * 3600 + m * 60 + s + ds) % (24 * 60 * 60)
    h, m, s = t // 3600, t % 3600 // 60, t % 60
    print(f"{h:02d}:{m:02d}:{s:02d}")