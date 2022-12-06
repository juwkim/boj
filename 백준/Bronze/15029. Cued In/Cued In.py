import statistics as s
dic = {'red': 1, 'yellow': 2, 'green': 3, 'brown': 4,
       'blue': 5, 'pink': 6, 'black': 7}
res = s.Counter([dic[input()] for _ in range(int(input()))])

if len(res) == 1 and res[1]:
    print(1)
else:
    print(res[1] * max(res) + sum(k * v for k, v in res.items()))