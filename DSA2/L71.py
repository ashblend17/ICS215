import math
n = int(input())
ans=0
rect =[]
for i in range(1,int(math.sqrt(n))+1):
    for j in range(i,n//i+1):
        rect.append((i,j))
        ans+=1
        
        
print(ans)
for i, rect in enumerate(rect):
    if i != len(rect) - 1:
        print(f"{rect[0]} x {rect[1]},", end=" ")
    else:
        print(f"{rect[0]} x {rect[1]}")