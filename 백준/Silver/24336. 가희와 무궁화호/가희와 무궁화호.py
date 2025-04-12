import sys
input = lambda: sys.stdin.readline().rstrip()

dist = {
    "Seoul": 0.0, "Yeongdeungpo": 9.1, "Anyang": 23.9, "Suwon": 41.5,
    "Osan": 56.5, "Seojeongri": 66.5, "Pyeongtaek": 75.0, "Seonghwan": 84.4,
    "Cheonan": 96.6, "Sojeongni": 107.4, "Jeonui": 114.9, "Jochiwon": 129.3,
    "Bugang": 139.8, "Sintanjin": 151.9, "Daejeon": 166.3, "Okcheon": 182.5,
    "Iwon": 190.8, "Jitan": 196.4, "Simcheon": 200.8, "Gakgye": 204.6,
    "Yeongdong": 211.6, "Hwanggan": 226.2, "Chupungnyeong": 234.7,
    "Gimcheon": 253.8, "Gumi": 276.7, "Sagok": 281.3, "Yangmok": 289.5,
    "Waegwan": 296.0, "Sindong": 305.9, "Daegu": 323.1, "Dongdaegu": 326.3,
    "Gyeongsan": 338.6, "Namseonghyeon": 353.1, "Cheongdo": 361.8,
    "Sangdong": 372.2, "Miryang": 381.6, "Samnangjin": 394.1,
    "Wondong": 403.2, "Mulgeum": 412.4, "Hwamyeong": 421.8,
    "Gupo": 425.2, "Sasang": 430.3, "Busan": 441.7
}

N, Q = map(int, input().split())
arr, dep = {}, {}
day, prev = 0, [-1, -1]

def to_min(t, prev_time):
    global day
    if t[0] == '-': return -1
    m = int(t[:2]) + int(t[3:]) / 60 + day * 24
    if m <= prev_time: 
        day += 1
        m += 24
    return m

for _ in range(N):
    st, a, d = input().split()
    if (amin := to_min(a, prev[1])) != -1:
        arr[st] = amin
        prev[0] = amin
    if (dmin := to_min(d, prev[0])) != -1:
        dep[st] = dmin
        prev[1] = dmin

for _ in range(Q):
    s, e = input().split()
    print(abs(dist[s] - dist[e]) / (arr[e] - dep[s]))
