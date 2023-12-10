n = int(input())
dic = {c: i for i, c in enumerate(input(), 1)}
if len(dic) == 1:
    print("No")
else:
    a, b, *_ = dic.keys()
    print("Yes")
    print(dic[a], dic[b], 1)