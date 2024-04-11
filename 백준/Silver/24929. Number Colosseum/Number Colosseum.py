N, *x = map(int, open(0).read().split())
p, n = [], []
for num in x:
    if num > 0:
        p.append(num)
    else:
        n.append(num)
    while p and n:
        if p[-1] > -n[-1]:
            p[-1] += n[-1]; n.pop()
        elif p[-1] < -n[-1]:
            n[-1] += p[-1]; p.pop()
        else:
            p.pop(); n.pop()
if p:
    print("Positives win!")
    print(*p)
elif n:
    print("Negatives win!")
    print(*n)
else:
    print("Tie!")