while True:
    try:
        n = bin(int(input()))[2:]
        zero, one = n.count('0'), n.count('1')
        print(["straight", "left", "right"][(zero > one) - (one > zero)])
    except:
        break