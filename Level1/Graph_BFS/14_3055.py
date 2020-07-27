
from collections import deque 
r, c = map(int, input().split()) 

dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]

d_coord, s_coord = None, None
pools = list() 
arr = list() 

for i in range(r): 
    alist = input() 
    for j in range(c): 
        if alist[j] == 'D': d_coord = [i, j] 
        elif alist[j] == 'S': s_coord = [i, j] 
        elif alist[j] == '*': pools.append((i, j)) 
    arr.append(alist)  
    
queue = deque() 
pool = [[-1]*c for _ in range(r)] 
for x, y in pools: 
    pool[x][y] = 0 
    queue.append((x, y)) 

while queue: 
    x, y = queue.popleft() 

    for i in range(4): 
        nx, ny = x+dx[i], y+dy[i] 

        if 0 <= nx < r and 0 <= ny < c: 
            if pool[nx][ny] == -1 and arr[nx][ny] == '.': 
                queue.append((nx, ny)) 
                pool[nx][ny] = pool[x][y] + 1 


check = [[-1]*c for _ in range(r)] 
sx, sy = s_coord
check[sx][sy] = 0 
queue.append((sx, sy)) 

while queue: 
    x, y = queue.popleft() 

    for i in range(4): 
        nx, ny = x+dx[i], y+dy[i] 
        if 0 <= nx < r and 0 <= ny < c: 
            if check[nx][ny] == -1:
                if arr[nx][ny] == '.': 
                    if check[x][y] + 1 < pool[nx][ny] or pool[nx][ny] == -1: 
                        check[nx][ny] = check[x][y] + 1 
                        queue.append((nx, ny)) 
                elif arr[nx][ny] == 'D': 
                    check[nx][ny] = check[x][y] + 1 
                    break 
                
fx, fy = d_coord
print(check[fx][fy] if check[fx][fy] != -1 else "KAKTUS")