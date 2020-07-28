
n, m = map(int, input().split()) 
alist = list(map(int, input().split())) 
alist.sort() 

check = [False]*n 

def go(idx, k, tmp): 
    if len(tmp) == m: 
        print(' '.join(map(str, tmp))) 
        return 

    if idx >= n: return 


    for i in range(k, n): 
        if check[i]: continue 
        check[i] = True 
        tmp.append(alist[i]) 
        go(idx+1, i, tmp) 
        check[i] = False 
        tmp.pop() 

go(0, 0, []) 
         