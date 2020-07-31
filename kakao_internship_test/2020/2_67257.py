def solution(expression):
    answer = 0
    operations = '*+-'

    res = list() 
    for i in range(3): 
        for j in range(3): 
            for k in range(3): 
                if i == j or j == k or i ==k: continue 

                stack = list() 
                for elem in expression.split(operations[i]): 
                    for eelem in elem.split(operations[j]): 
                        for eeelem in eelem.split(operations[k]): 
                            pass  

    return answer