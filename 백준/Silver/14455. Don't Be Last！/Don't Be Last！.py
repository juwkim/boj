dic = {'Bessie': 0, 'Elsie': 0, 'Daisy': 0, 'Gertie': 0, 'Annabelle': 0, 'Maggie': 0, 'Henrietta': 0}
for _ in range(int(input())):
    name, amount = input().split()
    dic[name] += int(amount)
Min = min(dic.values())

buf = []
for name, val in dic.items():
    if val != Min:
        buf.append((name, val))
if not buf:
    print('Tie')
else:
    Min = min([val for name, val in buf])
    buf = [name for name, val in dic.items() if val == Min]
    if len(buf) == 1:
        print(buf[0])
    else:
        print('Tie')