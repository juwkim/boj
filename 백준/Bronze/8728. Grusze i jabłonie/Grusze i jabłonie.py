_,l=open(0)
f=lambda x,y:abs(l.find(x)-l.rfind(y))//2
print(max(f(*'01'),f(*'10')))