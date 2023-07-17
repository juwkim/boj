dic = {"P": 1500, "M": 6000, "S": 15500, "C": 40000, "T": 75000, "H": 125000}
print(sum(dic[input()[0]] for i in range(int(input()))))