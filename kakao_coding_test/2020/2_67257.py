def operate(n1, n2, oper): 
    if oper == '*': return n1*n2 
    elif oper == '+': return n1+n2 
    else: return n1-n2 

def solution(expression):
    answer = 0
    oper = '*+-'

    prev = ''
    stack = list() 
    i = 0
    while i < len(expression): 
        if expression[i].isnumeric(): prev += expression[i]
        else: 
            stack.append(int(prev)) 
            stack.append(expression[i]) 
            prev = ''
        i += 1 
    stack.append(int(prev))

    for i in range(3): 
        for j in range(3): 
            if i == j: continue 
            for k in range(3): 
                if i == k or j == k: continue 
                tmp_stack = stack[:]
                tmp_order = [oper[i], oper[j], oper[k]]
                t = 0  
                while len(tmp_stack) != 1: 
                    if tmp_order[t] in tmp_stack: 
                        idx = tmp_stack.index(tmp_order[t]) 
                        tmp_stack[idx-1] = operate(tmp_stack[idx-1], tmp_stack[idx+1], tmp_order[t]) 
                        tmp_stack.pop(idx) 
                        tmp_stack.pop(idx) 
                    else: t += 1

                answer = max(answer, abs(tmp_stack[0]))
    
    return answer

print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))