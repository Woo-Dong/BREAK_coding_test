
n, m = map(int, input().split()) 
alist = list(map(int, input().split())) 
alist.sort() 

check = [False]*n

ans = list() 
def go(idx, tmp): 
    if len(tmp) == m: 
        ans.append(tuple(tmp))
        return 

    if idx >= n: return 

    for i in range(n): 
        if check[i]: continue 
        check[i] = True 
        tmp.append(alist[i]) 
        go(idx+1, tmp) 
        check[i] = False 
        tmp.pop() 

go(0, []) 

ans = sorted(list(set(ans)))
for elem in ans: print(' '.join(map(str, elem))) 
