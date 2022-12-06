def cal(name):
    global minsik
    sem = [name.count('LOVE'[i]) + minsik[i] for i in range(4)]
    res = 1
    for i in range(3):
        for j in range(i+1, 4):
            res *= sem[i] + sem[j] % 100
    
    return res % 100

minsik_name = input()
minsik = [*map(lambda s: minsik_name.count(s), 'LOVE')]
print(max(sorted(input() for _ in range(int(input()))), key=cal))