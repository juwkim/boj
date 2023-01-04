l = ["***********", "*abcdefghi*", "*jklmnopqr*", "*stuvwxyz**", "***********"]
dic = {}
for i in range(1, 4):
    for j in range(1, 10):
        dic[l[i][j]] = set()
        for x in range(i - 1, i + 2):
            for y in range(j - 1, j + 2):
                if (x != i or y != j) and l[x][y] != '*':
                    dic[l[i][j]].add(l[x][y])
   
for _ in range(int(input())):
    a, b = input().split()
    ans = 3
    if len(a) == len(b):
        if a == b:
            ans = 1
        elif all(s == t or t in dic[s] for s, t in zip(a, b)):
            ans = 2
    print(ans)