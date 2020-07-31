def solution(numbers, hand):
    answer = ''
    adict = dict()
    adict[0] = [3, 1]

    for i in range(1, 10): adict[i] = [(i-1)//3, (i+2)%3]

    left, right = [3, 0], [3, 2]

    for num in numbers:
        if num in [1, 4, 7]: 
            answer += 'L' 
            left = adict[num] 
        elif num in [3, 6, 9]: 
            answer += 'R' 
            right = adict[num] 
        else: 
            left_cost = sum([abs(a-b) for a, b in zip(adict[num], left)])
            right_cost = sum([abs(a-b) for a, b in zip(adict[num], right)])

            if left_cost < right_cost: 
                answer += 'L' 
                left = adict[num] 
            elif left_cost > right_cost: 
                answer += 'R' 
                right = adict[num] 
            else: 
                if hand == 'right': 
                    answer += 'R' 
                    right = adict[num] 
                else:
                    answer += 'L' 
                    left = adict[num]
    return answer