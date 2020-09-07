import datetime

def solution(lines):
    ans = 0
    stack = 0
    times = []
    for line in lines:
        date, time = line.rsplit(' ', 1)
        parser = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f')
        times.append(('s', str((parser - datetime.timedelta(seconds = float(time.replace('s', '')) + 0.999)))))
        times.append(('e', str(parser)))
    times = sorted(times, key = lambda x : x[1])

    for time in times:
        if time[0] == "s":
            stack += 1
            ans = max(ans, stack)
        else:
            stack -= 1
    return ans
