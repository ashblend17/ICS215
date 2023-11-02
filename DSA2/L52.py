def gcd(a, b):
    if (b == 0):
        return a
         
    return gcd(b, a % b)
    
def getBoundaryCount(x1, x2, y1, y2):
    if (x1 == x2):
        return abs(y1 - y2) - 1
    if (y1 == y2):
        return abs(x1 - x2) - 1
 
    return gcd(abs(x1 - x2),
               abs(y1 - y2)) - 1
x = input()
a = list(map(int,(input().strip("()")).split(",")))
b = list(map(int,(input().strip("()")).split(",")))
c = list(map(int,(input().strip("()")).split(",")))
x1 = a[0]
y1 = a[1]
x2 = b[0]
y2 = b[1]
x3 = c[0]
y3 = c[1]

area = (abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)))

BoundaryPoints = (getBoundaryCount(x1, x2, y1, y2) +
                      getBoundaryCount(x2, x3, y2, y3) +
                      getBoundaryCount(x1, x3, y1, y3) + 3)
ans = (area - BoundaryPoints + 2) // 2
print(ans)