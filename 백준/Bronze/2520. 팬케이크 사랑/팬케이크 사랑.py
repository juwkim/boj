for _ in range(int(input())):
    input()
    m, y, su, sa, f = map(int, input().split())
    b, gs, gc, w = map(int, input().split())
    dough = int(min(m/8, y/8, su/4, sa, f/9) * 16)
    topping = sum([b, gs//30, gc//25, w//10])
    print(min(dough, topping))