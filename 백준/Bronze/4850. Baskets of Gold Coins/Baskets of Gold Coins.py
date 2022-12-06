while True:
    try:
        N,w,d,t=map(int,input().split())
        print((N*(N-1)*w-2*t)//(2*d)or N)
    except:
        break