
k = int(input()) 
for _ in range(k): 
    v, e = map(int, input().split()) 
    
    arr = [[0]*v for _ in range(v)] 

    for _ in range(e): 
        a, b = map(int, input().split()) 
        a -= 1
        b -= 1
        arr[a][b] = arr[b][a] = 1 
    
    
