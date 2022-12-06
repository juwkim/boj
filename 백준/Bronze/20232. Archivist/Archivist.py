year = int(input())
print('PetrSU, ITMO' if year == 2006
      else 'SPbSU' if year in [1996, 1997, 2000, 2007, 2008, 2013, 2018]
      else 'ITMO')