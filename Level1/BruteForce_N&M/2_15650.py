
n, m = map(int, input().split()) 

alist = [i for i in range(1, n+1)] 
check = [False]*n 
ans = [0]*m

def go(idx, k): 
    if idx == m: 
        print(' '.join(map(str, ans))) 
        return 

    for i in range(k, n): 
        if check[i]: continue 
        check[i] = True 
        ans[idx] = alist[i]  
        go(idx+1, i) 
        check[i] = False 

go(0, 0) 
