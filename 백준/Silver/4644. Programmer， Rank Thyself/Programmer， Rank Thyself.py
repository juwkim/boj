import sys
input = sys.stdin.readline

tc = 1
while c:=int(input()):
    team = []
    for _ in range(c):
        name, *scores = input().split()
        scores = [*map(int, scores)]
        avg, correct = 1, 0
        for score in scores:
            if score != 0:
                avg *= score
                correct += 1
        if correct: avg **= 1 / correct
        else:       avg = 0
        team.append((-correct, sum(scores), int(avg + 0.5), name, scores))
    print(f"CONTEST {tc}")
    rank, prev = 1, ()
    for i, (correct, total, avg, name, scores) in enumerate(sorted(team), 1):
        if (correct, total, avg) != prev:
            rank = i
        prev = (correct, total, avg)
        print(f"{rank:02d} {name:10s} {-correct} {total:4d} {avg:3d} {' '.join(map(lambda s: f'{s:3d}', scores))}")
    tc += 1