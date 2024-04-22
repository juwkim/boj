_,S=open(0)
l="I II III IV V VI VII VIII IX X XI XII".split()
print(*[i+1 for i in range(12)if l[i]in S])