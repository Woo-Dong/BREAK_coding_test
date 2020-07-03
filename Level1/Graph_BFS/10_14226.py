
# Not Solved
from collections import deque 

s = int(input()) 

MAXIMUM = 1001 
check = [-1]*MAXIMUM
queue = deque() 
queue.append(1) 
check[1] = 0 


while queue: 
    now = queue.popleft() 

    nxt = now*2 
    if nxt < MAXIMUM:
        if check[nxt] == -1: 
            queue.append(nxt) 
            check[nxt] = check[now] + 2 
        elif check[now] + 2 < check[nxt]: 
            queue.append(nxt) 
            check[nxt] = check[now] + 2
    
    nxt = now - 1 
    if 0 <= nxt: 
        if check[nxt] == -1: 
            queue.append(nxt) 
            check[nxt] = check[now] + 1 
        elif check[now] + 1 < check[nxt]: 
            queue.append(nxt) 
            check[nxt] = check[now] + 1 

print(check[s]) 


