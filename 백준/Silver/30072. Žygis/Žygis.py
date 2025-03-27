E0, Eu, En, Eg, N, *h = map(int, open(0).read().split())
need, time, prv = 0, 0, 0
for num in h + [0]:
    if num > prv:
        time += num - prv
        need += Eu * (num - prv)
    elif num < prv:
        time += prv - num
        need += En * (prv - num)
    else:
        time += 1
    prv = num
time += max(0, (need - E0 + Eg - 1) // Eg)
print(time)