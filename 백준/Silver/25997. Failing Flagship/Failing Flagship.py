X, Y = input().split()
def solve(s):
    if len(s) == 1:
        match s:
            case "N": return 0
            case "E": return 90
            case "S": return 180
            case "W": return 270
    match s[-2:]:
        case "NE":
            d = {"N": -1, "E": 1}
            ret = 45
        case "SE":
            d = {"E": -1, "S": 1}
            ret = 135
        case "SW":
            d = {"S": -1, "W": 1}
            ret = 225
        case "NW":
            d = {"W": -1, "N": 1}
            ret = 315
    num = 22.5
    for i in range(len(s) - 3, -1, -1):
        ret += num * d[s[i]]
        num /= 2
    return ret

a, b = solve(X), solve(Y)
print(min((a - b) % 360, (b - a) % 360))