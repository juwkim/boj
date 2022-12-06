import math
while (s:= input()) != 'E':
    a1, v1, a2, v2 = s.split()
    dic = {a1: float(v1), a2: float(v2)}
    
    if 'T' not in dic:
        e = 6.11 * math.exp(5417.7530 * ((1/273.16) - (1/(dic['D']+273.16))))
        h = 0.5555 * (e - 10.0)
        dic['T'] = dic['H'] - h
        pass
    elif 'D' not in dic:
        e = 10 + (dic['H'] - dic['T']) / 0.5555
        tmp = 1/273.16 - math.log(e / 6.11, math.e) / 5417.7530
        dic['D'] = 1 / tmp - 273.16
    else:
        e = 6.11 * math.exp(5417.7530 * ((1/273.16) - (1/(dic['D']+273.16))))
        h = 0.5555 * (e - 10.0)
        dic['H'] = dic['T'] + h
    print(f"T {dic['T']:.1f} D {dic['D']:.1f} H {dic['H']:.1f}")