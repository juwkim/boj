from math import pi, floor, ceil
while R:= float(input()):
    
    denominator = 1
    while True:
        numerator = denominator * pi
        a = abs(pi - floor(numerator) / denominator)
        b = abs(pi - ceil(numerator) / denominator)
        if min(a, b) <= R:
            if a < b:
                print(f'{floor(numerator)}/{denominator}')
            else:
                print(f'{ceil(numerator)}/{denominator}')
            break
        denominator += 1