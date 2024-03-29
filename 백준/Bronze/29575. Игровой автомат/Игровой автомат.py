dic = {}
for _ in range(int(input())):
    c, w = input().split()
    dic[c] = int(w)
print(sum(dic.get(input(), 0) - 10 for _ in range(int(input()))))