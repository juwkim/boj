ans = 0
J, O, I = 0, 0, 0
prv = 'J'
for c in input():
    match prv + c:
        case "JJ": J += 1
        case "JO": O = 1
        case "JI": J = 0
        case "OJ": J = 1; O = 0
        case "OO": O += 1
        case "OI":
            I = 1
            if J >= O and O == I and I > ans: ans = I
        case "IJ":
            if J >= O and O == I and I > ans: ans = I
            J = 1; O = 0; I = 0
        case "IO":
            if J >= O and O == I and I > ans: ans = I
            J = 0; O = 0; I = 0
        case "II":
            I += 1
            if J >= O and O == I and I > ans: ans = I
    prv = c
print(ans)