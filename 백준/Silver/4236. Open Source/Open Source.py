from collections import defaultdict
while (project := input()) != '0':

    dic = {project: set()}
    dic_name = defaultdict(set)
    while (s:= input()) != '1':
        if s.isupper():
            project = s
            dic[project] = set()
        else:
            dic[project].add(s)
            dic_name[s].add(project)
    
    for name in dic_name:
        if len(dic_name[name]) >= 2:
            for project in dic_name[name]:
                dic[project].remove(name)
    
    for project in sorted(dic, key=lambda x: (-len(dic[x]), x)):
        print(project, len(dic[project]))