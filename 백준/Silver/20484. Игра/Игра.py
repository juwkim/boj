l = len(n := input())
if l & 1:
    winner = "First"
    for i in range(l - 1):
        if i & 1:
            if n[i] != '0':
                winner = "Second"
                break
        elif n[i] != '9':
            break
else:
    winner = "Second"
    for i in range(l - 1):
        if i & 1:
            if n[i] != '9':
                break
        elif n[i] != '01'[i == 0]:
            winner = "First"
            break
print(winner)