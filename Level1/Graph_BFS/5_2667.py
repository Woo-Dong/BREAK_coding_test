
from collections import deque 

n = int(input()) 
arr = [list(map(int, input())) for _ in range(n)] 

check = [[False]*n for _ in range(n)] 
dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]
queue = deque() 

ans_list = list() 
for i in range(n): 
    for j in range(n): 
        if arr[i][j] == 0 or check[i][j]: continue 

        check[i][j] = True 
        tmp_ans = 1 
        queue.append((i, j))

        while queue: 
            x, y = queue.popleft() 

            for k in range(4): 
                nx, ny = x+dx[k], y+dy[k] 

                if 0 <= nx < n and 0 <= ny < n: 
                    if check[nx][ny] or arr[nx][ny] == 0: continue 
                    check[nx][ny] = True 
                    tmp_ans += 1 
                    queue.append((nx, ny)) 
        ans_list.append(tmp_ans) 

print(len(ans_list)) 
ans_list.sort() 
for elem in ans_list: print(elem) 