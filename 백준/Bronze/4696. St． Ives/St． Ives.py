while n:= float(input()):
    if n == 1:
        print("5.00")
    else:
        print("%.2f" % ((n ** 5 - 1) / (n - 1)))