
import sys 

n, m = map(int, input().split()) 

edges = list() 
node_dict = dict() 

for _ in range(m): 
    a, b = map(int, input().split()) 
    edges.append((a, b)) 
    edges.append((b, a)) 
    if a not in node_dict: node_dict[a] = [b] 
    else: node_dict[a].append(b) 

    if b not in node_dict: node_dict[b] = [a] 
    else: node_dict[b].append(a) 

for i in range(2*m): 
    a, b = edges[i] 
    for j in range(2*m): 
        c, d = edges[j] 
        tmp_set = set([a, b, c, d]) 
        if len(tmp_set) < 4 or c not in node_dict[b]: continue 
        for e in node_dict[d]: 
            if e in tmp_set: continue 
            print(1) 
            sys.exit() 
print(0) 