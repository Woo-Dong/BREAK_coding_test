
from collections import deque 

dx, dy = [-1, 0, 1, 0, 1, 1, -1, -1], [0, -1, 0, 1, 1, -1, 1, -1] 

while True: 

    w, h = map(int, input().split()) 
    if w == h == 0: break 

    arr = [list(map(int, input().split())) for _ in range(h)] 

    queue = deque() 
    check = [[False]*w for _ in range(h)] 

    ans = 0 
    for i in range(h): 
        for j in range(w): 
            if arr[i][j] == 0 or check[i][j]: continue 

            ans += 1 
            queue.append((i, j)) 
            check[i][j] = True 
            while queue: 
                x, y = queue.popleft() 
                for k in range(8): 
                    nx, ny = x+dx[k], y+dy[k] 

                    if 0 <= nx < h and 0 <= ny < w: 
                        if check[nx][ny] or arr[nx][ny] == 0: continue 
                        queue.append((nx, ny)) 
                        check[nx][ny] = True 
    print(ans) 


