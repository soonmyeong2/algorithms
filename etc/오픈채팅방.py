def solution(record):
    ans = list()
    userName = dict()
    comment = {"Enter" : "님이 들어왔습니다.", "Leave" : "님이 나갔습니다."}
    
    for log in record:
        if log[0] == "E" or log[0] == "C":
            _, uid, name = log.split(' ')
            userName[uid] = name

    for log in record:        
        if log[0] == "E" or log[0] == "L":
            ans.append(userName[log.split(' ')[1]] + comment[log.split(' ')[0]])
            
    return ans
