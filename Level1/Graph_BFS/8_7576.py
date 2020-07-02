
from collections import deque 
m, n = map(int, input().split()) 

dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1] 

arr = [list(map(int, input().split())) for _ in range(n)] 

check = [[-1]*m for _ in range(n)] 

queue = deque() 

for i in range(n): 
    for j in range(m): 
        if arr[i][j] == 1: 
            check[i][j] = 0
            queue.append((i, j)) 

while queue: 
    x, y = queue.popleft() 

    for i in range(4): 
        nx, ny = x+dx[i], y+dy[i] 
        if 0 <= nx < n and 0 <= ny < m: 
            if arr[nx][ny] == -1: continue 

            if check[nx][ny] == -1: 
                check[nx][ny] = check[x][y] + 1 
                queue.append((nx, ny)) 
            elif check[x][y] + 1 < check[nx][ny]: 
                check[nx][ny] = check[x][y] + 1 
                queue.append((nx, ny)) 

ans = -1 
for i in range(n): 
    for j in range(m): 
        if arr[i][j] != -1:
            if check[i][j] == -1: 
                print(-1) 
                exit() 
            ans = max(ans, check[i][j]) if ans != -1 else check[i][j]
print(ans) 