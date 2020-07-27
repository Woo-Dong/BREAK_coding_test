
n, m = map(int, input().split()) 

alist = [i for i in range(1, n+1)] 

def go(idx, tmp): 
    if len(tmp) == m: 
        print(' '.join(map(str, tmp))) 
        return 
    if idx >= n: return 

    for i in range(n): 
        tmp.append(alist[i]) 
        go(idx+1, tmp) 
        tmp.pop() 

go(0, []) 
        