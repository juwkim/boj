while (z:= int(input())):
    z_cubic = pow(z, 3)
    ans = 0
    for x in range(1, z):
        x_cubic = pow(x, 3)
        y = int(pow(z_cubic - x_cubic, 1/3))
        y_cubic = pow(y, 3)
        ans = max(ans, x_cubic + y_cubic)
    print(z_cubic - ans)