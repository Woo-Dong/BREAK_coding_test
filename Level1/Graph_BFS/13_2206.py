
from collections import deque 

n, m = map(int, input().split()) 

arr = [list(map(int, input())) for _ in range(n)] 

dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1] 
queue = deque() 

check = [[[-1]*2 for _ in range(m)] for _ in range(n)] 

queue.append((0, 0, 0)) 
check[0][0][0] = 1 

while queue: 
    x, y, cnt = queue.popleft() 

    for i in range(4): 
        nx, ny = x+dx[i], y+dy[i] 
        if 0 <= nx < n and 0 <= ny < m and check[nx][ny][cnt] == -1: 
            if arr[nx][ny] == 0: 
                check[nx][ny][cnt] = check[x][y][cnt] + 1 
                queue.append((nx, ny, cnt)) 
            else: 
                if cnt < 1: 
                    check[nx][ny][cnt+1] = check[x][y][cnt] + 1 
                    queue.append((nx, ny, cnt+1)) 
        
ans = -1 
for elem in check[n-1][m-1]: 
    if elem != -1: 
        ans = elem 
    elif ans < elem: ans = elem 
print(ans) 

