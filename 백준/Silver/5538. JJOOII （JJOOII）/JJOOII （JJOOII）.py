ans = 0
J, O, I = 0, 0, 0
prv = 'J'
for c in input():
    match prv + c:
        case "JJ": J += 1
        case "JO": O = 1
        case "JI": J = 0
        case "OJ": J, O = 1, 0
        case "OO": O += 1
        case "IJ": J, O, I = 1, 0, 0
        case "IO": J, O, I = 0, 0, 0
        case _:
            I += 1
            if J >= O and O == I and I > ans: ans = I
    prv = c
print(ans)