a,b,c,d=zip(*[map(int,input().split())for _ in range(int(input()))])
print(max(min(b)-max(a),0)*max(min(d)-max(c),0))