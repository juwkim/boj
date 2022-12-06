import hashlib
print(hashlib.new('sha', input().encode()).hexdigest())