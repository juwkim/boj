Y, N = 0, 0
vaccinated = [0, 0, 0]
controlled = [0, 0, 0]
for _ in range(int(input())):
    vaccine, *l = input()
    if vaccine == 'Y':
        Y += 1
        for i in range(3):
            vaccinated[i] += (l[i] == 'Y')   
    else:
        N += 1
        for i in range(3):
            controlled[i] += (l[i] == 'Y')
for i in range(3):
    ans = 1 - vaccinated[i] * N / (controlled[i] * Y)
    print(ans * 100 if ans > 0 else 'Not Effective')