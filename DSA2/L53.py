from cmath import sqrt
import math
n = int(input())
a = list(map(int,(input().strip("()")).split(",")))
b = list(map(int,(input().strip("()")).split(",")))
c = list(map(int,(input().strip("()")).split(",")))
x = []
y = []
x.append(a[0])
y.append(a[1])
x.append(b[0])
y.append(b[1])
x.append(c[0])
y.append(c[1])

def find_circumcenter(vertices, angles):
    
    midpoints = [((vertices[i][0] + vertices[(i + 1) % 3][0]) / 2, (vertices[i][1] + vertices[(i + 1) % 3][1]) / 2) for i in range(3)]

    slopes = [math.tan(math.radians(angles[i])) for i in range(3)]

    x_circumcenter = (midpoints[2][1] - midpoints[0][1] + slopes[0] * midpoints[0][0] - slopes[2] * midpoints[2][0]) / (slopes[0] - slopes[2])
    y_circumcenter = midpoints[0][1] + slopes[0] * (x_circumcenter - midpoints[0][0])

    return (x_circumcenter, y_circumcenter)
def dist(a,b,c,d):
    return sqrt((a-b)**2+(c-d)**2)
def circumcenter1(x1, y1, x2, y2, x3, y3):
    
    M1_x = (x1 + x2) / 2
    M1_y = (y1 + y2) / 2
    M2_x = (x1 + x3) / 2
    M2_y = (y1 + y3) / 2
    
    if(x2==x1):
        m1 = 0
    else:
        mAB = (y2 - y1) / (x2 - x1)
        m1 = -1 / mAB
    if(x3==x1):
        m2 = 0
    else:
        mAC = (y3 - y1) / (x3 - x1)
        m2 = -1 / mAC


    xO = round((M2_y - M1_y + m1 * M1_x - m2 * M2_x) / (m1 - m2),1)
    yO = M1_y + m1 * (xO - M1_x)

    return xO, yO

if(n==2):
    m1x = (x[0]+x[1])/2
    m1y = (y[0]+y[1])/2
    m2x = (x[0]+x[2])/2
    m2y = (y[0]+y[2])/2
    M1 = -(x[1] - x[0]) / (y[1] - y[0])
    M2 = -(x[2] - x[0]) / (y[2] - y[0])
    xO = (m2y - m1y + M1 * m1x - M2 * m2x) / (M1 - M2)
    yO = m1y + M1 * (xO - m1x)
    print(f"({xO},{yO})")

elif(n==3):
    k = int(input())
    l = int(input())
    m = int(input())
    if(k+l+m>180):
        print("Invalid Input")
    elif(k==90 or l==90 or m==90):
        if(k==90):
            on = (x[1]+x[2])/2
            no = (y[1]+y[2])/2
            print(f"({on},{no})")
        elif(l==90):
            on = (x[0]+x[2])/2
            no = (y[0]+y[2])/2
            print(f"({on},{no})")
        elif(m==90):
            on = (x[1]+x[0])/2
            no = (y[1]+y[0])/2
            print(f"({on},{no})")
        
        
    else:
        vertices = [(x[0],y[0]),(x[1],y[1]),(x[2],y[2])]
        angles = [k, l, m]
        circumcenter = find_circumcenter(vertices, angles)
        print(circumcenter)
elif(n==1):
    if(x[0]==x[1]==x[2]==y[0]==y[1]==y[2]):
        print("No Circumcenter")
    else:
        circumcenter = circumcenter1(x[0], y[0], x[1], y[1], x[2], y[2])
        print(circumcenter)