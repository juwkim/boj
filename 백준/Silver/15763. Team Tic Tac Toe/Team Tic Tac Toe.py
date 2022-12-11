Map = [input() for _ in range(3)]
Map.extend(tuple(zip(*Map)))
Map.append(Map[0][0] + Map[1][1] + Map[2][2])
Map.append(Map[0][2] + Map[1][1] + Map[2][0])
Map = [sorted(i) for i in Map]
ans = len(set(i[0] for i in Map if i[0] == i[1] == i[2]))
print(ans)
ans = len(set(i[0] + i[2] for i in Map if ((i[0] == i[1] and i[1] != i[2]) or (i[0] != i[1] and i[1] == i[2]))))
print(ans)