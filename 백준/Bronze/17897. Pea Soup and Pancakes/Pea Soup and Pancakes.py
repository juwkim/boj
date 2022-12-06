state = 0
for _ in range(int(input())):
    res = [input() for _ in range(int(input())+1)]
    if 'pea soup' in res[1:] and 'pancakes' in res[1:]:
        state = 1
        break
print(res[0] if state else 'Anywhere is fine I guess')