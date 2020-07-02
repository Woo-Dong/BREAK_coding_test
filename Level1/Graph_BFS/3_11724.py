
from collections import deque 

n, m = map(int, input().split()) 

arr = [[0]*n for _ in range(n)] 

for _ in range(m): 
    x, y = map(int, input().split()) 
    x -= 1
    y -= 1 
    arr[x][y] = arr[y][x] = 1

check = [False]*n 
ans = 0 
queue = deque() 

for i in range(n): 
    if check[i]: continue
    ans += 1
    for j in range(n): 
        if arr[i][j] == 0 or check[j] or i == j: continue 
        queue.append(j) 
        check[i] = check[j] = True 
        while queue: 
            now = queue.popleft() 
            for k in range(n): 
                if k == now or check[k] or arr[now][k] == 0: continue 
                queue.append(k)
                check[k] = True 
print(ans)         
