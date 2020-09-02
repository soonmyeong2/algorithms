def solution(p):
    if p == "": 
        return ""
    
    valid, s = 1, 0
    for i, c in enumerate(p):
        s += int(c.replace("(", "1").replace(")", "-1"))
        if s < 0:
            valid = 0
        if s == 0: 
            break
            
    if valid:
        return p[:i+1] + solution(p[i+1:])
    else:
        return "(" + solution(p[i+1:]) + ")" + p[:i+1][1:-1].replace("(", ".").replace(")", "(").replace(".", ")")