import numpy as np
i = int(input())
c1 = input()
c2 = input()
c3 = input()

def parse_coordinate(coord_str):
    coord_str = coord_str.replace('(', '').replace(')', '')
    x, y = map(int, coord_str.split(','))
    return x, y

x1, y1 = parse_coordinate(c1)
x2, y2 = parse_coordinate(c2)
x3, y3 = parse_coordinate(c3)

if i == 1:
    slope1 = (y2 - y1) / (x2 - x1)
    slope2 = (y3 - y2) / (x3 - x2)

   
    if slope1 == slope2:
        print("Collinear Slope condition value = 0, Collinear = True")
    else:
        print("Collinear: False")

elif i == 2:
   
    area = 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
    if area<=0:
        print("Area of Triangle = 0, Collinear = True")
    elif area>0:
        print("Area of Triangle = 12.5, Collinear = False")
        
elif i == 3:
    d1 =  np.sqrt(((y2-y1)**2) + (x2-x1)**2 )
    d2 = np.sqrt(((y3-y2)**2) + (x3-x2)**2 )
    d3 =  np.sqrt(((y3-y1)**2) + (x3-x1)**2 )
    if d1 +d2 == d3:
        print("Smallest distance =",round(d3/2,2),"Collinear = True")