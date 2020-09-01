def solution(numbers, hand):
    l, r = 10, 12
    ans = []
    
    for number in numbers:
        number = number if number != 0 else 11
        if number % 3 == 0:
            ans.append("R")
            r = number
        elif number % 3 == 1:
            ans.append("L")
            l = number
        elif number % 3 == 2:
            dl = abs((number-1)//3 - (l-1)//3) + abs((number-1)%3 - (l-1)%3)
            dr = abs((number-1)//3 - (r-1)//3) + abs((number-1)%3 - (r-1)%3)
            if dl < dr:
                ans.append("L")
                l = number
            elif dl > dr:
                ans.append("R")
                r = number
            elif dl == dr:
                ans.append(hand[0].upper())
                if hand[0] == 'r':
                    r = number
                else:
                    l = number
    return ''.join(ans)
