import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

dist = {
    "Seoul": 0.0,
    "Yeongdeungpo": 9.1,
    "Anyang": 23.9,
    "Suwon": 41.5,
    "Osan": 56.5,
    "Seojeongri": 66.5,
    "Pyeongtaek": 75.0,
    "Seonghwan": 84.4,
    "Cheonan": 96.6,
    "Sojeongni": 107.4,
    "Jeonui": 114.9,
    "Jochiwon": 129.3,
    "Bugang": 139.8,
    "Sintanjin": 151.9,
    "Daejeon": 166.3,
    "Okcheon": 182.5,
    "Iwon": 190.8,
    "Jitan": 196.4,
    "Simcheon": 200.8,
    "Gakgye": 204.6,
    "Yeongdong": 211.6,
    "Hwanggan": 226.2,
    "Chupungnyeong": 234.7,
    "Gimcheon": 253.8,
    "Gumi": 276.7,
    "Sagok": 281.3,
    "Yangmok": 289.5,
    "Waegwan": 296.0,
    "Sindong": 305.9,
    "Daegu": 323.1,
    "Dongdaegu": 326.3,
    "Gyeongsan": 338.6,
    "Namseonghyeon": 353.1,
    "Cheongdo": 361.8,
    "Sangdong": 372.2,
    "Miryang": 381.6,
    "Samnangjin": 394.1,
    "Wondong": 403.2,
    "Mulgeum": 412.4,
    "Hwamyeong": 421.8,
    "Gupo": 425.2,
    "Sasang": 430.3,
    "Busan": 441.7,
}

N, Q = map(int, input().split())
arrival, departure = {}, {}
prv_dtime, prv_atime = -1, -1
day = 0
for _ in range(N):
    station, atime, dtime = input().split()
    if atime[0] != '-':
        hh, mm = map(int, atime.split(':'))
        atime = hh * 60 + mm + day * 1440
        if atime <= prv_dtime:
            day += 1
            atime += 1440
        arrival[station] = atime
        prv_atime = atime
    if dtime[0] != '-':
        hh, mm = map(int, dtime.split(':'))
        dtime = hh * 60 + mm + day * 1440
        if dtime <= prv_atime:
            day += 1
            dtime += 1440
        departure[station] = dtime
        prv_dtime = dtime
for _ in range(Q):
    s1, s2 = input().split()
    d = abs(dist[s1] - dist[s2])
    time = arrival[s2] - departure[s1]
    print(d * 60 / time)