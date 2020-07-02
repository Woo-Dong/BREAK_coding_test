
import sys 
sys.setrecursionlimit(100000000)

k = int(input()) 
for _ in range(k): 
    v, e = map(int, sys.stdin.readline().split())  
    
    adict = dict() 

    for _ in range(e): 
        a, b = map(int, sys.stdin.readline().split()) 
        if a not in adict: adict[a] = [b] 
        else: adict[a].append(b) 

        if b not in adict: adict[b] = [a] 
        else: adict[b].append(a) 

    color = [0] * (v+1) 

    def dfs(x, c): 
        color[x] = c 
        if x not in adict: return True 
        for elem in adict[x]: 
            if color[elem] == 0 and not dfs(elem, 3-c): return False 
            elif color[elem] == color[x]: return False 
        return True 
    
    ans = True 
    for i in range(1, v+1): 
        if color[i] == 0 and not dfs(i, 1): 
            ans = False 
            break 
    
    if ans: print("YES")
    else: print("NO")