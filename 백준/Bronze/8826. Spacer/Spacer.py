from statistics import Counter
for _ in range(int(input())):
    input()
    a = Counter(input())
    print(abs(a['E'] - a['W']) + abs(a['N'] - a['S']))