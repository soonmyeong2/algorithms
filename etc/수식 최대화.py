import re

def solution(expression):
    prior = ["+-*", "+*-", "-+*", "-*+", "*+-", "*-+"]
    ans = 0

    for op_cand in prior:
        temp = re.compile("(\D)").split('' + expression)
        for exp in op_cand:
            while exp in temp:
                idx = temp.index(exp)
                temp = temp[:idx-1] + [str(eval(''.join(temp[idx-1:idx+2])))] + temp[idx+2:]  
        ans = abs(int(temp[0])) if abs(int(temp[0])) > ans else ans
    return ans
