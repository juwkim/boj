h1, m1, s1 = map(int, input().split(':'))
h2, m2, s2 = map(int, input().split(':'))
seconds = ((h2 - h1) * 3600 + (m2 - m1) * 60 + s2 - s1) % 86400
print(f'{seconds//3600:02d}:{seconds%3600//60:02d}:{seconds%3600%60:02d}')