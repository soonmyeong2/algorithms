def solution(msg):
    ans = []
    words = {chr(i+65) : i+1 for i in range(26)}
    
    i = 0 
    while i < len(msg):
        j = i + 1
        while msg[i:j] in words and j <= len(msg):
            j += 1
        ans.append(words[msg[i:j-1]])
        words[msg[i:j]] = len(words) + 1
        i = j - 1   
        
    return ans
        
