dic = {'2D': 0, '2C': 1, '2H': 2, '2S': 3, '3D': 4, '3C': 5, '3H': 6, '3S': 7, '4D': 8, '4C': 9, '4H': 10, '4S': 11, '5D': 12, '5C': 13, '5H': 14, '5S': 15, '6D': 16, '6C': 17, '6H': 18, '6S': 19, '7D': 20, '7C': 21, '7H': 22, '7S': 23, '8D': 24, '8C': 25, '8H': 26, '8S': 27, '9D': 28, '9C': 29, '9H': 30, '9S': 31, 'TD': 32, 'TC': 33, 'TH': 34, 'TS': 35, 'JD': 36, 'JC': 37, 'JH': 38, 'JS': 39, 'QD': 40, 'QC': 41, 'QH': 42, 'QS': 43, 'KD': 44, 'KC': 45, 'KH': 46, 'KS': 47, 'AD': 48, 'AC': 49, 'AH': 50, 'AS': 51}
for _ in range(int(input())):
    me = sorted(dic[c] for c in input().split())
    gf = [*filter(lambda x: x not in me, range(52))]
    ans, idx = 0, 0
    for num in me:
        if num > gf[idx]:
            ans += 1
            idx += 1
    print(ans)