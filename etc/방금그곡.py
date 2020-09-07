def solution(m, musicinfos):
    repl = {'C#':'c', 'D#':'d', 'E#':'e', 'F#':'f', 'G#':'g', 'A#':'a'}
    ans = ['', '']
    
    for r in repl:
        m = m.replace(r, repl[r])
    
    for i, musicinfo in enumerate(musicinfos):
        start, end, name, contents = musicinfo.split(',')
        
        for r in repl:
            contents = contents.replace(r, repl[r])
            
        cnt = (int(end[0:2]) * 60 + int(end[3:5])) - (int(start[0:2]) * 60 + int(start[3:5]))
        full = ''
        for i in range(cnt):
            full += contents[i%len(contents)]
        if m in full and len(ans[0]) < len(full):
            ans[0], ans[1] = full, name
            
    return ans[1] if ans[1] != '' else '(None)'
