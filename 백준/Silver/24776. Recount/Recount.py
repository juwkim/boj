Map = {}
while (s:= input()) != '***':
    if s in Map:
        Map[s] += 1
    else:
        Map[s] = 1
Max = max(Map.values())
names = [k for k in Map if Map[k] == Max]
if len(names) == 1:
    print(*names)
else:
    print('Runoff!')