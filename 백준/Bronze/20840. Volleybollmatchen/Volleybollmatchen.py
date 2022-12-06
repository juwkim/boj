score = [0, 0]
set_score = [0, 0]
end = 25
N = int(input())
for c in input():
    set_score[c == 'B'] += 1
    if max(set_score) >= end and abs(set_score[0] - set_score[1]) >= 2:
        score[set_score.index(max(set_score))] += 1
        set_score = [0, 0]
        if score == [1, 1]:
            end = 15
print(*score)