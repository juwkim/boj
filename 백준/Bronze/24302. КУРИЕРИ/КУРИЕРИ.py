def cost1(x):
    if x <= 5: return 4
    if x <= 10: return 7
    if x <= 20: return 12
    if x <= 30: return 17
    return x * .57

def cost2(x):
    if x <= 2: return 0.9 + 0.9 * x
    if x <= 5: return 1.0 + 0.85 * x
    if x <= 20: return 1.25 + 0.80 * x
    if x <= 40: return 3.25 + 0.70 * x
    return 9.25 + .55 * x

def cost(x):
    return min(cost1(x), cost2(x))
a, b = map(lambda x: int(x)//1000, input().split())
print("%.2f" % (cost(a) + cost(b)))