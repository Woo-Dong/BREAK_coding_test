
n, m = map(int, input().split()) 

alist = [i for i in range(1, n+1)] 
ans = [0]*m 
check = [False]*n 

def go(idx): 
    if idx == m: 
        print(' '.join(map(str, ans))) 
        return 
    
    for i in range(n): 
        if check[i]: continue 
        check[i] = True 
        ans[idx] = alist[i] 
        go(idx + 1) 
        check[i] = False 
go(0) 