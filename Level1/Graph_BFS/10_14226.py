
from collections import deque 

s = int(input()) 

check = [[-1]*(s+1) for _ in range(s+1)] 
queue = deque() 
queue.append((1, 0)) 
check[1][0] = 0 

while queue: 
    i, j = queue.popleft() 
    if check[i][i] == -1: 
        check[i][i] = check[i][j] + 1 
        queue.append((i, i)) 
    
    if i+j <= s and check[i+j][j] == -1: 
        check[i+j][j] = check[i][j] + 1
        queue.append((i+j, j)) 

    if i-1 >= 0 and check[i-1][j] == -1: 
        check[i-1][j] = check[i][j] + 1
        queue.append((i-1, j)) 

ans = -1 
for i in range(s+1): 
    if check[s][i] != -1: 
        if ans == -1 or ans > check[s][i]: ans = check[s][i] 

print(ans)
