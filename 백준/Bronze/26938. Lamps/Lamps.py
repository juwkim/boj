def check(k):
    
    a = 49 * h * p * k / 100000 
    b = (k * h + 999) // 1000 * 5
    return a + b > 60
    

h, p = map(int, input().split())
k = 1
while check(k) == False:
    k += 1
print(k)