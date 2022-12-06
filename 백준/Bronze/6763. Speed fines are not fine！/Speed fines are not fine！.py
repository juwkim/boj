a, b = int(input()), int(input())
diff = b - a
expr = 'You are speeding and your fine is $%d.'
if diff <= 0:
    print('Congratulations, you are within the speed limit!')
elif 0 < diff <= 20:
    print(expr % 100)
elif 20 < diff <= 30:
    print(expr % 270)
else:
    print(expr % 500)