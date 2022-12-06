n=int(input())
g=lambda x:(n+x*10)%2400
print(n,"in Ottawa")
print(g(-30),"in Victoria")
print(g(-20),"in Edmonton")
print(g(-10),"in Winnipeg")
print(n,"in Toronto")
print(g(10),"in Halifax")
print(g(13+((n%100)>=30)*4),"in St. John's")