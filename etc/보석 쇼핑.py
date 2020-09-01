def solution(gems):
    maxLen = len(set(gems))
    used = {gems[0] : 1}
    ans = [1, len(gems)]
    start = end = 0
    
    while start < len(gems):
        if len(used) != maxLen:
            end += 1
            if end == len(gems) : break
            if gems[end] not in used:
                used[gems[end]] = 1
            else:
                used[gems[end]] += 1
        else:
            ans = [start +1, end + 1] if ans[1] - ans[0] > end - start else ans
            if used[gems[start]] == 1:
                used.pop(gems[start])
            else:
                used[gems[start]] -= 1
            start += 1
    return ans
