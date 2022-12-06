n = int(input())
auc = [input() for _ in range(2 * n)]
print(auc[auc.index(max(auc[1::2], key=int)) - 1])