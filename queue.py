import sys

n = int(input())
que = []

for _ in range(n):
    a = sys.stdin.readline().split()
    
    if a[0]== 'push' :
        que.append(a[1])
        
    elif a[0]== 'pop' :
        if que :
            print(que.pop(0))
        else :
            print(-1)
            
    elif a[0]== 'size' :
        print(len(que))
    
    elif a[0]== 'empty' :
        if que :
            print(0)
        else :
            print(1)
            
    elif a[0]== 'front' :
        if que :
            print(que[0])
        else :
            print(-1)
            
    elif a[0]== 'back' :
        if que :
            print(que[-1])
        else :
            print(-1)