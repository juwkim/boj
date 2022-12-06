rank = [i[0] for i in input().split()]
print(max(rank.count(k) for k in set(rank)))