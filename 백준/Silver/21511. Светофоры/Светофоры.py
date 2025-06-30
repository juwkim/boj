a, b, x = map(int, input().split())
if x <= 1000 * a:
    print(1000)
else:
    print(min(1000,x/((x+1000*b-1)//(1000*(a+b))*(a+b)-a)))