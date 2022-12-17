x = int(input())
m = int(input())
try:
    ans = pow(x, -1, m)
except:
    ans = 'No such integer exists.'
print(ans)