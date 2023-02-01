def update(time, d):

    time += d
    if time == 13:
        time = 1
    elif time == 0:
        time = 12
    return time

time = 1
d = 1
for _ in range(int(input())):
    S, X = input().split()
    ans = 'NO'
    if S[0] == 'H' and time == int(X):
        pass
    elif S[0] == 'H':
        d = -d
    elif time == int(X):
        ans = 'YES'
    
    print(time, ans)
    time = update(time, d)