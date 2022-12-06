names, scores = [], {}
N = int(input())
for _ in range(N):
    name, *l = input().split()
    l = [-int(l[0]), int(l[1]), -int(l[2])]
    
    names.append(name)
    scores[name] = l

names.sort(key=lambda name: (scores[name], name))
print(*names)