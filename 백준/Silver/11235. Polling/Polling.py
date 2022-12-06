from statistics import*
print(*sorted(multimode([l[:-1] for l in open(0)][1:])))