a = open(0).read().lower()
print('English' if a.count('t') > a.count('s') else 'French')