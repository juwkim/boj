input()
s = input()
c = s.count
print(c('A')*c('C')*c('G')*c('T')%1000000007)