import sys
input = lambda: sys.stdin.readline().rstrip()
MIS = lambda: [*map(int, input().split())]

for _ in range(int(input())):
    C, P = MIS()
    Coffee = {}
    for _ in range(C):
        coffee, *l = input().split()
        Coffee[coffee + 'small'] = int(l[0])
        Coffee[coffee + 'medium'] = int(l[1])
        Coffee[coffee + 'large'] = int(l[2])
    
    fee = 100 // P
    for _ in range(P):
        name, size, coffee = input().split()
        cost = fee + Coffee[coffee + size]
        q = cost % 5
        if q == 1:
            cost -= 1
        elif q == 4:
            cost += 1
            
        print(name, cost)