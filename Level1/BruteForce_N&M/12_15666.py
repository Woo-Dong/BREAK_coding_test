
n, m = map(int, input().split()) 
alist = sorted(list(map(int, input().split()))) 

ans = list() 
def go(idx, k, tmp): 
    if len(tmp) == m: 
        ans.append(tuple(tmp)) 
        return 

    if idx >= n: return 

    for i in range(k, n): 
        tmp.append(alist[i]) 
        go(idx+1, i, tmp) 
        tmp.pop() 

go(0, 0, []) 
ans = sorted(list(set(ans))) 
for elem in ans: print(' '.join(map(str, elem))) 
