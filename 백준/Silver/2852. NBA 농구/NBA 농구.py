def update(diff):
    A, B = score
    if A > B:
        lead[0] += diff
    elif A < B:
        lead[1] += diff

score = [0, 0]
lead = [0, 0]
cur = 0
for _ in range(int(input())):
    team, time = input().split()
    h, m = map(int, time.split(':'))
    minutes = h * 60 + m
    
    update(minutes - cur)
    score[int(team) - 1] += 1
    cur = minutes

update(48 * 60 - cur)

print("%02d:%02d" % divmod(lead[0], 60))
print("%02d:%02d" % divmod(lead[1], 60))