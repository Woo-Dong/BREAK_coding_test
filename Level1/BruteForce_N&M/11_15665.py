
n, m = map(int, input().split()) 
alist = sorted(list(map(int, input().split())))

ans = list() 
def go(idx, tmp): 
    if len(tmp) == m: 
        ans.append(tuple(tmp)) 
        return 

    if idx >= n: return 

    for i in range(n): 
        tmp.append(alist[i]) 
        go(idx+1, tmp) 
        tmp.pop() 

go(0, []) 
ans = sorted(list(set(ans))) 
for elem in ans: print(' '.join(map(str, elem))) 