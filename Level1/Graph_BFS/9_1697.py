
from collections import deque 

n, k = map(int, input().split()) 
MAXIMUM = int(10e5)
check = [-1]*(MAXIMUM+1) 
check[n] = 0 
queue = deque() 
queue.append(n) 

while queue: 
    now = queue.popleft() 

    if now*2 <= MAXIMUM and check[now*2] == -1: 
        queue.append(now*2) 
        check[now*2] = check[now] + 1
        if now*2 == k: break 
    
    for i in [-1, 1]: 
        nxt = now + i 
        if 0 <= nxt <= MAXIMUM and check[nxt] == -1: 
            queue.append(nxt) 
            check[nxt] = check[now] + 1 
            if nxt == k: break
    
print(check[k])
