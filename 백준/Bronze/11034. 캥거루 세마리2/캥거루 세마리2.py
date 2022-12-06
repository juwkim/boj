while True:
    try:
        a, b, c = sorted(map(int, input().split()))
        print(max(b-a,c-b)-1)
    except:
        break