p={0:0,1:395,2:200}
for _ in range(int(input())):
    Y,M,D=map(int,input().split())
    print((Y-997)//3*-590+p[Y%3]-D+221-20*M+(M//-2*39+(M+M%2)*20-6)*(Y%3!=0))