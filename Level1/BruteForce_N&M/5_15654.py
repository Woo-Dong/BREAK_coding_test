
n, m = map(int, input().split()) 
alist = list(map(int, input().split())) 
alist.sort()
check = [False]*n 

def go(idx, ans): 
    if len(ans) == m: 
        print(' '.join(map(str, ans))) 
        return 
    
    if idx > n : return 

    for i in range(n): 
        if check[i]: continue 
        check[i] = True 
        ans.append(alist[i]) 
        go(idx+1, ans) 
        check[i] = False 
        ans.pop() 

go(0, []) 
