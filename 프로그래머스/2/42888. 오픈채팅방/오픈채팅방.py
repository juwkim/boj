def solution(record):
    nick = {}
    for l in record:
        if l[0] in 'EC':
            _, uid, nickname = l.split()
            nick[uid] = nickname
    ans = []
    for l in record:
        if l[0] == 'E':
            _, uid, nickname = l.split()
            ans.append(f"{nick.get(uid, nickname)}님이 들어왔습니다.")
        elif l[0] == 'L':
            _, uid = l.split()
            ans.append(f"{nick[uid]}님이 나갔습니다.")
    return ans