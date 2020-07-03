
from collections import deque 

n, k = map(int, input().split()) 
MAXIMUM = 100001 

check = [-1]*MAXIMUM 
check[n] = 0 
queue = deque() 
queue.append(n) 

while queue: 
    now = queue.popleft() 
    nxt = now*2 
    if nxt < MAXIMUM:
        if check[nxt] == -1: 
            check[nxt] = check[now]
            queue.append(nxt)
        elif check[now] < check[nxt]: 
            check[nxt] = check[now] 
            queue.append(nxt) 
        if nxt == k: break 
    
    for i in [1, -1]: 
        nxt = now + i 
        if 0 <= nxt < MAXIMUM:
            if check[nxt] == -1: 
                check[nxt] = check[now] + 1 
                queue.append(nxt) 
            elif check[now] + 1 < check[nxt]: 
                check[nxt] = check[now] + 1 
                queue.append(nxt) 
            if nxt == k: break

print(check[k])