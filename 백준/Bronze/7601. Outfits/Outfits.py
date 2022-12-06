i = 1
while (s:=input()) != '0 0':
    n, d = map(int, s.split())
    becs = [*range(1, 1 + n)]
    cas = [*range(n, 0, -1)]
    
    a = int(input())
    if a:
        del becs[a-1]
    
    b = int(input())
    if b:
        del cas[b-1]
    
    print('Scenario', i)
    for j in range(1, 1 + d):
        s, t = map(int, input().split())
        print('Day', j, 'ALERT' if becs[s-1] == cas[t-1] else 'OK')
    
    i += 1