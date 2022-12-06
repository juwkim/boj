import re
N,S=6-int(input()),input()
print(max(N,sum(1 for x in['[\d]','[a-z]','[A-Z]','[!@#$%^&*()-+]']if not re.search(x,S))))