a, b, c = map(int, input().split())
d, e = map(int, input().split())
if a and d:
    if d == 1:
        ans = ["Remember my character", "Head on"][e == 0]
    else:
        D = (a * d * e) ** 2 - a * d * (d - 1) * (a * e ** 2 + b * e + c - c * d - e)
        ans = ["Remember my character", "Go ahead", "Head on"][(D > 0) - (D < 0)]
else:
    ans = ["Head on", "Nice"][a * e ** 2 + b * e + c == c * d + e]
print(ans)