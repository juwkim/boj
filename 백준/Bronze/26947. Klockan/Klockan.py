dic = {}
for t in range(720):
    h, m = divmod(t, 60)
    angle1 = h * 300 + m * 5
    angle2 = m * 60
    angle = (angle2 - angle1) % 3600
    dic[str(angle)] = "%02d:%02d" % (h, m)
print(dic[input()])