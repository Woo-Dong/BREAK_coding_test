
# Not solved
import sys 

n, m = map(int, input().split()) 

adict = dict() 

check = [False]*n 
def dfs(node, cnt): 
    for elem in adict[node]: 
        if not check[elem]:
            check[elem] = True
            if cnt == 3: 
                print(1) 
                exit() 
            dfs(elem, cnt+1) 

for _ in range(m): 
    x, y = map(int, input().split()) 
    if x not in adict: adict[x] = [y] 
    else: adict[x].append(y) 

    if y not in adict: adict[y] = [x] 
    else: adict[y].append(x) 

for elem in adict:
    check = [False]*n 
    check[elem] = True 
    dfs(elem, 0) 

print(0)