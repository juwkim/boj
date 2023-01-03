ans = set()
for _ in range(int(input())):
    
    s = input().split('@')
    if len(s) != 2:
        continue
    username, domain = map(str.lower, s)
    if username.startswith('.') or username.endswith('.'):
        continue
    
    if '..' in username or '-' in username:
        continue
    
    username = username.replace('.', '')
    if not (6 <= len(username) <= 30):
        continue
    
    if domain.startswith('.') or domain.endswith('.'):
        continue
    
    if '..' in domain or '_' in domain:
        continue
    
    if not (3 <= len(domain) <= 30):
        continue
    
    ans.add((username, domain))

print(len(ans))