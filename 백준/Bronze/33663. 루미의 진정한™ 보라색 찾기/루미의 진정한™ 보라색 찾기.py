hlo, hhi, slo, shi, vlo, vhi, R, G, B = map(int, open(0).read().split())

M, m = max(R, G, B), min(R, G, B)
V = M
S = 255 * (V - m) / V
if M == R:
    H = 60 * (G - B) / (V - m)
elif M == G:
    H = 120 + 60 * (B - R) / (V - m)
else:
    H = 240 + 60 * (R - G) / (V - m)
if H < 0:
    H += 360
if hlo <= H <= hhi and slo <= S <= shi and vlo <= V <= vhi:
    print("Lumi will like it.")
else:
    print("Lumi will not like it.")