import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

'''
Aries	March 21 --- April 19
Taurus	April 20 --- May 20
Gemini	May 21 --- June 20
Cancer	June 21 --- July 22
Leo	July 23 --- August 22
Virgo	August 23 --- September 22
Libra	September 23 --- October 22
Scorpio	October 23 --- November 22
Sagittarius	November 23 --- December 21
Capricorn	December 22 --- January 19
Aquarius	January 20 --- February 18
Pisces	February 19 --- March 20
'''

y, m, d = map(int, input().split('-'))
if (m == 1 and d >= 20) or (m == 2 and d <= 18):
    print('Aquarius')
elif (m == 2 and d >= 19) or (m == 3 and d <= 20):
    print('Pisces')
elif (m == 3 and d >= 21) or (m == 4 and d <= 19):
    print('Aries')
elif (m == 4 and d >= 20) or (m == 5 and d <= 20):
    print('Taurus')
elif (m == 5 and d >= 21) or (m == 6 and d <= 20):
    print('Gemini')
elif (m == 6 and d >= 21) or (m == 7 and d <= 22):
    print('Cancer')
elif (m == 7 and d >= 23) or (m == 8 and d <= 22):
    print('Leo')
elif (m == 8 and d >= 23) or (m == 9 and d <= 22):
    print('Virgo')
elif (m == 9 and d >= 23) or (m == 10 and d <= 22):
    print('Libra')
elif (m == 10 and d >= 23) or (m == 11 and d <= 22):
    print('Scorpio')
elif (m == 11 and d >= 23) or (m == 12 and d <= 21):
    print('Sagittarius')
elif (m == 12 and d >= 22) or (m == 1 and d <= 19):
    print('Capricorn')