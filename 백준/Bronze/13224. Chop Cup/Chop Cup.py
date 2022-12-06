X = 1
change = {'A': [1, 2], 'B': [2, 3], 'C': [1, 3]}
for move in input():
    if X in change[move]:
        X = sum(change[move]) - X
print(X)