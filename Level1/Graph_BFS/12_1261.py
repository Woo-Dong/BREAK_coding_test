
from collections import deque 

m, n = map(int, input().split()) 
arr = [list(map(int, input())) for _ in range(n)] 

check = [[-1]*m for _ in range(n)]
check[0][0] = 0 

dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1] 
queue = deque() 
queue.append((0, 0)) 

while queue: 
    x, y = queue.popleft() 

    for i in range(4): 
        nx, ny = x+dx[i], y+dy[i] 
        if 0 <= nx < n and 0 <= ny < m: 
            if check[nx][ny] != -1: continue 
            if arr[nx][ny] == 0: 
                queue.appendleft((nx, ny)) 
                check[nx][ny] = check[x][y] 
            else: 
                queue.append((nx, ny)) 
                check[nx][ny] = check[x][y] + 1

print(check[n-1][m-1])