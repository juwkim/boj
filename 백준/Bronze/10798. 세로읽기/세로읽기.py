s = [input() for _ in range(5)]
a = len(max(s, key=len))
for j in range(a):
    for i in range(5):
        try:
            print(s[i][j], end="")
        except:
            pass