score = [i * int(input()) for i in [3, 2, 1, 3, 2, 1]]
apple, banana = sum(score[:3]), sum(score[3:])
print('A' if apple > banana else 'B' if apple < banana else 'T')