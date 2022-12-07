dic = {"1/2": 0, "1/4": 0, "3/4": 0}
for _ in range(int(input())):
    dic[input()] += 1
print(dic["3/4"] + (dic["1/2"] + 1) // 2 + max(0, (dic["1/4"] - dic["3/4"] - (dic["1/2"] & 1) * 2 + 3) // 4))