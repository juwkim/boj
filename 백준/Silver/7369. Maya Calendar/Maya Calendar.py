dic = {'pop': 0, 'no': 1, 'zip': 2, 'zotz': 3, 'tzec': 4, 'xul': 5, 'yoxkin': 6,
       'mol': 7, 'chen': 8, 'yax': 9, 'zac': 10, 'ceh': 11, 'mac': 12, 'kankin': 13,
       'muan': 14, 'pax': 15, 'koyab': 16, 'cumhu': 17, 'uayet': 18}
names = ['imix', 'ik', 'akbal', 'kan', 'chicchan', 'cimi', 'manik', 'lamat', 'muluk', 'ok',
         'chuen', 'eb', 'ben', 'ix', 'mem', 'cib', 'caban', 'eznab', 'canac', 'ahau']

print(N:=int(input()))
for _ in range(N):
    D, M, Y = input().split()   
    t = 365 * int(Y) + 20 * dic[M] + int(D[:-1])
    y, t = divmod(t, 260)
    print(t % 13 + 1, names[t%20], y)