tc = 1
while n:=int(input()):
    B = 0
    net = [0] * n
    for i in range(n):
        for j, w in enumerate(map(int, input().split())):
            B += w
            net[i] -= w
            net[j] += w
    A = sum(x for x in net if x > 0)
    print(f"{tc}. {B} {A}")
    tc += 1