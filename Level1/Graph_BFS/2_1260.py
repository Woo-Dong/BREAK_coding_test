
from collections import deque 

n, m, v = map(int, input().split()) 
arr = [[0]*(n+1) for _ in range(n+1)] 

for _ in range(m): 
    a, b = map(int, input().split()) 
    arr[a][b] = arr[b][a] = 1 

ans = [v]
check = [False]*(n+1) 
check[v] = True 
def dfs(node): 
    for i in range(1, n+1): 
        if arr[node][i] == 1 and not check[i]: 
            ans.append(i) 
            check[i] = True 
            dfs(i) 
dfs(v) 
print(' '.join(map(str, ans))) 

def bfs(): 
    ans = [v] 
    check = [False]*(n+1) 

    queue = deque() 
    queue.append(v) 
    check[v] = True 

    while queue: 
        now = queue.popleft() 
        for i in range(1, n+1): 
            if arr[now][i] == 0 or check[i]: continue 
            check[i] = True 
            queue.append(i) 
            ans.append(i) 
    print(' '.join(map(str, ans))) 
bfs() 