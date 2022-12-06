check = {'W': 1, 'H': 1/2, 'Q': 1/4, 'E': 1/8, 'S': 1/16, 'T': 1/32, 'X': 1/64}
while (s:=input()) != '*':
    print(sum(sum(check[i] for i in a) == 1 for a in s.split('/')))