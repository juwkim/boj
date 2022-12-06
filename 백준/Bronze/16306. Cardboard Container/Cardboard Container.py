V = int(input())
k = int(V**.5)+1
cost = 10**10
for a in range(1, k):
    for b in range(1, k):
        c = V/(a*b)
        if c == int(c):
            now = int(2*(a*b + b*c + c*a))
            if now < cost:
                cost = now
print(cost)