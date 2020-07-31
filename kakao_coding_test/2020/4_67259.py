from collections import deque 

def solution(board):
    answer = 0
    queue = deque() 
    dx, dy = [1, 0, -1, 0], [0, 1, 0, -1] 
    n = len(board) 
    check = [[-1]*n for _ in range(n)]
    check[0][0] = 0 

    if board[1][0] == 0: 
        queue.append((1, 0, 0))
        check[1][0] = 100
    if board[0][1] == 0: 
        queue.append((0, 1, 1))
        check[0][1] = 100

    while queue: 
        x, y, prev = queue.popleft() 

        for i in range(4): 
            nx, ny = x+dx[i], y+dy[i] 
            if 0 <= nx < n and 0 <= ny < n: 
                if board[nx][ny] == 1: continue 
                if (i+2)%4 == prev: continue

                if check[nx][ny] == -1: 
                    if i == prev: 
                        check[nx][ny] = check[x][y] + 100
                        queue.appendleft((nx, ny, i)) 
                    else: 
                        check[nx][ny] = check[x][y] + 600 
                        queue.append((nx, ny, i)) 
                else: 
                    if i == prev and check[x][y] + 100 <= check[nx][ny]: 
                        queue.appendleft((nx, ny, i)) 
                        check[nx][ny] = check[x][y] + 100 
                    elif i != prev and check[x][y] + 600 <= check[nx][ny]: 
                        queue.append((nx, ny, i)) 
                        check[nx][ny] = check[x][y] + 600 
    for elem in check: print(elem)
    return check[n-1][n-1] 


# print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
print(solution([[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0]]))
# print(solution([[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]))
# print(solution([[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 1], [0, 1, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0]]))
# print(solution([[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 1], [0, 1, 0, 1, 1, 1], [0, 0, 0, 0, 0, 0]]))
