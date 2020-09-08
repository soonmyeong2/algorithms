def solution(n, t, m, timetable):
    timetable = sorted([int(time[:2]) * 60 + int(time[3:]) for time in timetable], reverse=True)
    curTime, lastTime = 540, 540 + ((n - 1) * t)
    
    for i in range(n-1):
        for j in range(m):
            if len(timetable) and timetable[-1] <= curTime:
                timetable.pop()
        curTime += t
        
    userCnt = 0
    for time in sorted(list(set(timetable))):
        if time <= lastTime:
            userCnt += timetable.count(time)
        if userCnt >= m:
            return str((time-1) // 60).rjust(2, "0") + ":" + str((time-1) % 60).rjust(2, "0")
        
    return str(lastTime // 60).rjust(2, "0") + ":" + str(lastTime % 60).rjust(2, "0")